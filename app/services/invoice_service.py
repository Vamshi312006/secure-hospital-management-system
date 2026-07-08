from datetime import datetime
from decimal import Decimal

from sqlalchemy import or_

from app.extensions import db

from app.models.invoice import Invoice
from app.models.invoice_item import InvoiceItem
from app.models.payment import Payment
from app.models.patient import Patient

from app.rules.invoice import (
    InvoiceRules,
    PaymentRules,
)

from app.validators.invoice import (
    InvoiceValidator,
    InvoiceItemValidator,
    PaymentValidator,
)

from app.services.audit_service import AuditService


class InvoiceService:

    @staticmethod
    def generate_invoice_number():

        today = datetime.utcnow().strftime("%Y")

        count = Invoice.query.count() + 1

        return f"INV-{today}-{count:06d}"


    @staticmethod
    def get_all():

        return (
            Invoice.query
            .order_by(
                Invoice.issued_at.desc()
            )
            .all()
        )


    @staticmethod
    def get_by_id(invoice_id):

        return db.session.get(
            Invoice,
            invoice_id,
        )


    @staticmethod
    def search(query):

        if not query:
            return InvoiceService.get_all()

        return (
            Invoice.query
            .join(Invoice.patient)
            .filter(
                or_(
                    Invoice.invoice_number.ilike(f"%{query}%"),
                    Patient.first_name.ilike(f"%{query}%"),
                    Patient.last_name.ilike(f"%{query}%"),
                    Invoice.status.ilike(f"%{query}%"),
                )
            )
            .all()
        )


    @staticmethod
    def create_invoice(data, created_by):

        InvoiceValidator.validate(data)

        invoice = Invoice(

            invoice_number=InvoiceService.generate_invoice_number(),

            patient_id=data["patient_id"],

            created_by=created_by,

            due_date=data.get("due_date"),

            discount=Decimal(
                str(data.get("discount",0))
            ),

            tax=Decimal(
                str(data.get("tax",0))
            ),

            notes=data.get("notes",""),

            status="Draft",

        )

        db.session.add(invoice)

        db.session.commit()

        AuditService.log(
            action="CREATE",
            resource="Invoice",
            resource_id=invoice.id,
        )

        return invoice


    @staticmethod
    def update_invoice(invoice,data):

        InvoiceRules.ensure_not_paid(invoice)
        InvoiceRules.ensure_not_cancelled(invoice)

        InvoiceValidator.validate(data)

        invoice.discount = Decimal(
            str(data.get("discount",0))
        )

        invoice.tax = Decimal(
            str(data.get("tax",0))
        )

        invoice.notes = data.get(
            "notes",
            "",
        )

        db.session.commit()

        InvoiceService.calculate_totals(invoice)

        AuditService.log(
            action="UPDATE",
            resource="Invoice",
            resource_id=invoice.id,
        )

        return invoice


    @staticmethod
    def cancel_invoice(invoice):

        InvoiceRules.ensure_not_paid(invoice)

        invoice.status = "Cancelled"

        db.session.commit()

        AuditService.log(
            action="CANCEL",
            resource="Invoice",
            resource_id=invoice.id,
        )


    @staticmethod
    def delete_invoice(invoice):

        InvoiceRules.ensure_not_paid(invoice)

        db.session.delete(invoice)

        db.session.commit()

        AuditService.log(
            action="DELETE",
            resource="Invoice",
            resource_id=invoice.id,
        )


    @staticmethod
    def add_item(invoice,data):

        InvoiceRules.ensure_not_cancelled(invoice)

        InvoiceItemValidator.validate(data)

        total = (
            Decimal(str(data["quantity"]))
            *
            Decimal(str(data["unit_price"]))
        )

        item = InvoiceItem(

            invoice_id=invoice.id,

            category=data["category"],

            description=data["description"],

            quantity=data["quantity"],

            unit_price=data["unit_price"],

            total=total,

        )

        db.session.add(item)

        db.session.commit()

        InvoiceService.calculate_totals(invoice)

        AuditService.log(
            action="ADD ITEM",
            resource="Invoice",
            resource_id=invoice.id,
        )

        return item


    @staticmethod
    def remove_item(item):

        invoice = item.invoice

        db.session.delete(item)

        db.session.commit()

        InvoiceService.calculate_totals(invoice)

        AuditService.log(
            action="REMOVE ITEM",
            resource="Invoice",
            resource_id=invoice.id,
        )


    @staticmethod
    def calculate_totals(invoice):

        subtotal = sum(
            Decimal(str(item.total))
            for item in invoice.items
        )

        invoice.subtotal = subtotal

        invoice.total = (
            subtotal
            + invoice.tax
            - invoice.discount
        )

        invoice.balance = (
            invoice.total
            - invoice.amount_paid
        )

        PaymentRules.update_status(invoice)

        db.session.commit()

        return invoice


    @staticmethod
    def register_payment(invoice,data,user_id):

        PaymentValidator.validate(data)

        PaymentRules.validate_payment(
            invoice,
            data["amount"],
        )

        payment = Payment(

            invoice_id=invoice.id,

            amount=data["amount"],

            method=data["method"],

            reference_number=data.get(
                "reference_number"
            ),

            received_by=user_id,

            remarks=data.get(
                "remarks"
            ),

        )

        db.session.add(payment)

        invoice.amount_paid += Decimal(
            str(data["amount"])
        )

        InvoiceService.calculate_totals(invoice)

        AuditService.log(
            action="PAYMENT",
            resource="Invoice",
            resource_id=invoice.id,
        )

        return payment


    @staticmethod
    def revenue_today():

        today = datetime.utcnow().date()

        total = Decimal("0")

        for payment in Payment.query.all():

            if payment.paid_at.date() == today:

                total += Decimal(
                    str(payment.amount)
                )

        return total


    @staticmethod
    def outstanding_balance():

        total = Decimal("0")

        for invoice in Invoice.query.all():

            total += Decimal(
                str(invoice.balance)
            )

        return total
