from app.validators.fields import (
    ChoiceField,
    EmailField,
    IntegerField,
    PhoneField,
    TextField,
)

from app.validators.schema import validate


DOCTOR_SCHEMA = {

    "first_name": TextField(min_length=2, max_length=50),

    "last_name": TextField(min_length=2, max_length=50),

    "email": EmailField(),

    "phone": PhoneField(),

    "specialization": TextField(min_length=2, max_length=100),

    "qualification": TextField(min_length=2, max_length=150),

    "experience": IntegerField(
        minimum=0,
        maximum=60,
    ),

    "department_id": IntegerField(
        minimum=1,
    ),

    "gender": ChoiceField(
        choices={
            "Male",
            "Female",
            "Other",
        },
    ),

}


class DoctorValidator:

    @staticmethod
    def validate_create(data):
        return validate(data, DOCTOR_SCHEMA)

    @staticmethod
    def validate_update(data):
        return validate(data, DOCTOR_SCHEMA)
