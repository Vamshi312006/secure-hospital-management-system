from decimal import Decimal

from app.validators.base import ValidationError


class InvoiceValidator:

    @staticmethod
    def validate(data):

        errors = {}

        patient_id = data.get("patient_id")

        if not patient_id:
            errors["patient_id"] = "Patient is required."

        try:

            discount = Decimal(
                str(data.get("discount", 0))
            )

            if discount < 0:
                errors["discount"] = "Discount cannot be negative."

        except Exception:

            errors["discount"] = "Invalid discount."

        try:

            tax = Decimal(
                str(data.get("tax", 0))
            )

            if tax < 0:
                errors["tax"] = "Tax cannot be negative."

        except Exception:

            errors["tax"] = "Invalid tax."

        notes = data.get(
            "notes",
            "",
        )

        if len(notes) > 5000:
            errors["notes"] = "Notes are too long."

        if errors:
            raise ValidationError(errors)

        return True


class InvoiceItemValidator:

    ALLOWED = {
        "Consultation",
        "Laboratory",
        "Medicine",
        "Admission",
        "Room",
        "Miscellaneous",
    }

    @staticmethod
    def validate(data):

        errors = {}

        category = data.get("category")

        if category not in InvoiceItemValidator.ALLOWED:
            errors["category"] = "Invalid category."

        description = data.get(
            "description",
            "",
        ).strip()

        if not description:
            errors["description"] = "Description required."

        try:

            quantity = int(
                data.get("quantity", 0)
            )

            if quantity <= 0:
                errors["quantity"] = "Quantity must be greater than zero."

        except Exception:

            errors["quantity"] = "Invalid quantity."

        try:

            unit_price = Decimal(
                str(data.get("unit_price", 0))
            )

            if unit_price < 0:
                errors["unit_price"] = "Unit price cannot be negative."

        except Exception:

            errors["unit_price"] = "Invalid price."

        if errors:
            raise ValidationError(errors)

        return True


class PaymentValidator:

    METHODS = {
        "Cash",
        "Card",
        "UPI",
        "Bank Transfer",
    }

    @staticmethod
    def validate(data):

        errors = {}

        try:

            amount = Decimal(
                str(data.get("amount", 0))
            )

            if amount <= 0:
                errors["amount"] = "Payment must be greater than zero."

        except Exception:

            errors["amount"] = "Invalid payment."

        method = data.get("method")

        if method not in PaymentValidator.METHODS:
            errors["method"] = "Invalid payment method."

        if method != "Cash":

            reference = (
                data.get(
                    "reference_number",
                    "",
                ).strip()
            )

            if not reference:
                errors["reference_number"] = (
                    "Reference number required."
                )

        remarks = data.get(
            "remarks",
            "",
        )

        if len(remarks) > 2000:
            errors["remarks"] = "Remarks are too long."

        if errors:
            raise ValidationError(errors)

        return True
