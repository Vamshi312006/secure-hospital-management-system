from app.validators.fields import (
    EmailField,
    PhoneField,
    TextField,
)

from app.validators.schema import validate


SETTING_SCHEMA = {

    "hospital_name": TextField(
        min_length=2,
        max_length=150,
    ),

    "hospital_address": TextField(
        required=False,
        max_length=500,
    ),

    "hospital_phone": PhoneField(
        required=False,
    ),

    "hospital_email": EmailField(
        required=False,
    ),

    "timezone": TextField(
        min_length=2,
        max_length=100,
    ),

}


class SettingValidator:

    @staticmethod
    def validate(data):

        return validate(
            data,
            SETTING_SCHEMA,
        )

