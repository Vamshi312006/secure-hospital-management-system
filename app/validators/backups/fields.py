import re
from datetime import date, datetime

from app.validators.base import ValidationError


class Field:

    def __init__(
        self,
        *,
        required=True,
        min_length=None,
        max_length=None,
        choices=None,
    ):
        self.required = required
        self.min_length = min_length
        self.max_length = max_length
        self.choices = choices

    def validate(self, name, value):
        return value


class TextField(Field):

    def validate(self, name, value):

        value = "" if value is None else str(value).strip()

        if self.required and not value:
            raise ValidationError(f"{name} is required.")

        if not value:
            return value

        if self.min_length and len(value) < self.min_length:
            raise ValidationError(
                f"{name} must contain at least {self.min_length} characters."
            )

        if self.max_length and len(value) > self.max_length:
            raise ValidationError(
                f"{name} must not exceed {self.max_length} characters."
            )

        return value


class EmailField(TextField):

    def validate(self, name, value):

        value = super().validate(name, value)

        if value:

            pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

            if not re.fullmatch(pattern, value):
                raise ValidationError("Invalid email address.")

        return value


class PhoneField(TextField):

    def validate(self, name, value):

        value = super().validate(name, value)

        if value:

            pattern = r"^[0-9+\-\s]{7,20}$"

            if not re.fullmatch(pattern, value):
                raise ValidationError("Invalid phone number.")

        return value


class IntegerField(Field):

    def __init__(
        self,
        *,
        minimum=None,
        maximum=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.minimum = minimum
        self.maximum = maximum

    def validate(self, name, value):

        if value in ("", None):

            if self.required:
                raise ValidationError(f"{name} is required.")

            return None

        try:
            value = int(value)
        except ValueError:
            raise ValidationError(f"{name} must be an integer.")

        if self.minimum is not None and value < self.minimum:
            raise ValidationError(f"{name} is too small.")

        if self.maximum is not None and value > self.maximum:
            raise ValidationError(f"{name} is too large.")

        return value


class DateField(Field):

    def __init__(
        self,
        *,
        past=False,
        future=False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.past = past
        self.future = future

    def validate(self, name, value):

        if value in ("", None):

            if self.required:
                raise ValidationError(f"{name} is required.")

            return None

        try:
            value = datetime.strptime(
                value,
                "%Y-%m-%d",
            ).date()

        except ValueError:
            raise ValidationError(f"Invalid {name.lower()}.")

        if self.past and value > date.today():
            raise ValidationError(
                f"{name} cannot be in the future."
            )

        if self.future and value < date.today():
            raise ValidationError(
                f"{name} cannot be in the past."
            )

        return value


class ChoiceField(TextField):

    def validate(self, name, value):

        value = super().validate(name, value)

        if value and self.choices and value not in self.choices:
            raise ValidationError(f"Invalid {name.lower()}.")

        return value
