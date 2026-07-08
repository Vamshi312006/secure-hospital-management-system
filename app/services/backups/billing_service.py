# ==========================================================
# Imports
# ==========================================================

from app.extensions import db

from app.models.billing import Billing
from app.models.patient import Patient

from app.services.audit_service import AuditService


# ==========================================================
# Billing Service
# ==========================================================

class BillingService:

    # ------------------------------------------------------
    # Read Operations
    # ------------------------------------------------------

    @staticmethod
    def get_all():

        return (
            Billing.query
            .order_by(
                Billing.created_at.desc()
            )
            .all()
        )


    @staticmethod
    def get_by_id(bill_id):

        return db.session.get(
            Billing,
            bill_id,
        )


    @staticmethod
    def search(query):

        if not query:
            return BillingService.get_all()

        return (
            Billing.query
            .join(Billing.patient)
            .filter(
                db.or_(
                    Patient.first_name.ilike(f"%{query}%"),
                    Patient.last_name.ilike(f"%{query}%"),
                    Billing.status.ilike(f"%{query}%"),
                )
            )
            .order_by(
                Billing.created_at.desc()
            )
            .all()
        )


    @staticmethod
    def get_patients():

        return (
            Patient.query
            .order_by(
                Patient.first_name,
                Patient.last_name,
            )
            .all()
        )


    # ------------------------------------------------------
    # Create Operations
    # ------------------------------------------------------

    @staticmethod
    def create(
        patient_id,
        amount,
        status,
        payment_method,
        description,
    ):

        patient = db.session.get(
            Patient,
            patient_id,
        )

        if patient is None:
            raise ValueError(
                "Patient not found."
            )

        try:

            bill = Billing(

                patient_id=patient_id,

                amount=amount,

                status=status,

                payment_method=payment_method,

                description=description,

            )

            db.session.add(
                bill
            )

            db.session.commit()

            AuditService.log(
                action="CREATE",
                resource="Billing",
                resource_id=bill.id,
            )

            return bill

        except Exception:

            db.session.rollback()

            raise


    # ------------------------------------------------------
    # Update Operations
    # ------------------------------------------------------

    @staticmethod
    def update(
        bill,
        patient_id,
        amount,
        status,
        payment_method,
        description,
    ):

        patient = db.session.get(
            Patient,
            patient_id,
        )

        if patient is None:
            raise ValueError(
                "Patient not found."
            )

        bill.patient_id = patient_id
        bill.amount = amount
        bill.status = status
        bill.payment_method = payment_method
        bill.description = description

        db.session.commit()

        AuditService.log(
            action="UPDATE",
            resource="Billing",
            resource_id=bill.id,
        )

        return bill


    # ------------------------------------------------------
    # Delete Operations
    # ------------------------------------------------------

    @staticmethod
    def delete(bill):

        bill_id = bill.id

        db.session.delete(
            bill
        )

        db.session.commit()

        AuditService.log(
            action="DELETE",
            resource="Billing",
            resource_id=bill_id,
        )

