from app.validators.fields import (
    EmailField,
    PhoneField,
    TextField,
)

from app.validators.schema import validate


INSURANCE_SCHEMA = {

    "provider": TextField(
        min_length=2,
        max_length=150,
    ),

    "policy_number": TextField(
        min_length=2,
        max_length=150,
    ),

    "coverage_type": TextField(
        required=False,
        max_length=100,
    ),

    "contact_number": PhoneField(
        required=False,
    ),

    "email": EmailField(
        required=False,
    ),

}


class InsuranceValidator:

    @staticmethod
    def validate_create(data):

        return validate(
            data,
            INSURANCE_SCHEMA,
        )

    @staticmethod
    def validate_update(data):

        return validate(
            data,
            INSURANCE_SCHEMA,
        )

