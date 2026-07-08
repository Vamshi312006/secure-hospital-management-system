from app.validators.fields import (
    DateField,
    IntegerField,
    TextField,
)

from app.validators.schema import validate


APPOINTMENT_SCHEMA = {

    "patient_id": IntegerField(minimum=1),

    "doctor_id": IntegerField(minimum=1),

    "appointment_date": DateField(),

    "appointment_time": TextField(),

    "reason": TextField(
        min_length=3,
        max_length=500,
    ),

    "status": TextField(),

}


class AppointmentValidator:

    @staticmethod
    def validate_create(data):
        return validate(data, APPOINTMENT_SCHEMA)

    @staticmethod
    def validate_update(data):
        return validate(data, APPOINTMENT_SCHEMA)
