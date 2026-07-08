import re
from datetime import date, datetime


class ValidationError(Exception):
    pass


class Validator:

    @staticmethod
    def required(data, field, label=None):

        value = data.get(field)

        if value is None or str(value).strip() == "":
            raise ValidationError(f"{label or field} is required.")

        return str(value).strip()


    @staticmethod
    def integer(data, field, label=None, minimum=None, maximum=None):

        value = Validator.required(data, field, label)

        try:
            value = int(value)
        except ValueError:
            raise ValidationError(f"{label or field} must be an integer.")

        if minimum is not None and value < minimum:
            raise ValidationError(
                f"{label or field} must be at least {minimum}."
            )

        if maximum is not None and value > maximum:
            raise ValidationError(
                f"{label or field} must not exceed {maximum}."
            )

        return value


    @staticmethod
    def email(data, field="email"):

        value = Validator.required(data, field, "Email")

        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(pattern, value):
            raise ValidationError("Invalid email address.")

        return value


    @staticmethod
    def phone(data, field="phone"):

        value = Validator.required(data, field, "Phone")

        pattern = r"^[0-9+\-\s]{7,20}$"

        if not re.fullmatch(pattern, value):
            raise ValidationError("Invalid phone number.")

        return value


    @staticmethod
    def date(data, field, label=None):

        value = Validator.required(data, field, label)

        try:
            return datetime.strptime(
                value,
                "%Y-%m-%d",
            ).date()

        except ValueError:

            raise ValidationError(
                f"{label or field} has an invalid date."
            )


    @staticmethod
    def past_date(data, field, label=None):

        value = Validator.date(
            data,
            field,
            label,
        )

        if value > date.today():
            raise ValidationError(
                f"{label or field} cannot be in the future."
            )

        return value
