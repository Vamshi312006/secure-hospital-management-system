from app.validators.fields import (
    ChoiceField,
    DateField,
    EmailField,
    PhoneField,
    TextField,
)

from app.validators.schema import validate


PATIENT_SCHEMA = {

    "first_name": TextField(
        min_length=2,
        max_length=50,
    ),

    "last_name": TextField(
        min_length=2,
        max_length=50,
    ),

    "email": EmailField(),

    "phone": PhoneField(),

    "dob": DateField(
        past=True,
    ),

    "gender": ChoiceField(
        choices={
            "Male",
            "Female",
            "Other",
        },
    ),

    "blood_group": ChoiceField(
        choices={
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-",
        },
    ),

    "address": TextField(
        min_length=5,
        max_length=255,
    ),

}


class PatientValidator:

    @staticmethod
    def validate_create(data):

        return validate(
            data,
            PATIENT_SCHEMA,
        )

    @staticmethod
    def validate_update(data):

        return validate(
            data,
            PATIENT_SCHEMA,
        )
