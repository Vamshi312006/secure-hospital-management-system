from decimal import Decimal

from app.rules.base import RuleViolation


class InvoiceRules:

    @staticmethod
    def ensure_not_paid(invoice):

        if invoice.status == "Paid":
            raise RuleViolation(
                "Paid invoices cannot be modified."
            )


    @staticmethod
    def ensure_not_cancelled(invoice):

        if invoice.status == "Cancelled":
            raise RuleViolation(
                "Cancelled invoices cannot be modified."
            )


    @staticmethod
    def ensure_has_items(invoice):

        if len(invoice.items) == 0:
            raise RuleViolation(
                "Invoice must contain at least one item."
            )


class PaymentRules:

    @staticmethod
    def validate_payment(invoice, amount):

        amount = Decimal(str(amount))

        if amount <= 0:

            raise RuleViolation(
                "Payment amount must be greater than zero."
            )

        if invoice.status == "Cancelled":

            raise RuleViolation(
                "Cannot receive payment for a cancelled invoice."
            )

        if amount > invoice.balance:

            raise RuleViolation(
                "Payment exceeds outstanding balance."
            )


    @staticmethod
    def update_status(invoice):

        if invoice.balance <= 0:

            invoice.status = "Paid"

        elif invoice.amount_paid > 0:

            invoice.status = "Partially Paid"

        else:

            invoice.status = "Pending"
