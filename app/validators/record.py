from app.validators.fields import (
    IntegerField,
    TextField,
)

from app.validators.schema import validate


RECORD_SCHEMA = {

    "patient_id": IntegerField(minimum=1),

    "doctor_id": IntegerField(minimum=1),

    "diagnosis": TextField(
        min_length=3,
        max_length=500,
    ),

    "treatment": TextField(
        min_length=3,
        max_length=2000,
    ),

    "notes": TextField(
        required=False,
        max_length=5000,
    ),

}


class RecordValidator:

    @staticmethod
    def validate_create(data):
        return validate(data, RECORD_SCHEMA)

    @staticmethod
    def validate_update(data):
        return validate(data, RECORD_SCHEMA)
