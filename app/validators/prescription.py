from app.validators.fields import (
    IntegerField,
    TextField,
)

from app.validators.schema import validate


PRESCRIPTION_SCHEMA = {

    "patient_id": IntegerField(
        minimum=1,
    ),

    "doctor_id": IntegerField(
        minimum=1,
    ),

    "record_id": IntegerField(
        minimum=1,
    ),

    "instructions": TextField(
        required=False,
        max_length=2000,
    ),

}


PRESCRIPTION_ITEM_SCHEMA = {

    "medicine_id": IntegerField(
        minimum=1,
    ),

    "quantity": TextField(
        min_length=1,
        max_length=50,
    ),

    "days": IntegerField(
        minimum=1,
        maximum=365,
    ),

}


class PrescriptionValidator:

    @staticmethod
    def validate_create(data):

        return validate(
            data,
            PRESCRIPTION_SCHEMA,
        )

    @staticmethod
    def validate_update(data):

        return validate(
            data,
            PRESCRIPTION_SCHEMA,
        )

    @staticmethod
    def validate_item(data):

        return validate(
            data,
            PRESCRIPTION_ITEM_SCHEMA,
        )

    @staticmethod
    def validate_items(items):

        validated = []

        for item in items:

            validated.append(
                PrescriptionValidator.validate_item(
                    item
                )
            )

        return validated
