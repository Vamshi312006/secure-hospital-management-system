from app.validators.fields import (
    TextField,
)

from app.validators.schema import validate


DEPARTMENT_SCHEMA = {

    "name": TextField(
        min_length=2,
        max_length=100,
    ),

    "description": TextField(
        required=False,
        max_length=1000,
    ),

}


class DepartmentValidator:

    @staticmethod
    def validate_create(data):

        return validate(
            data,
            DEPARTMENT_SCHEMA,
        )

    @staticmethod
    def validate_update(data):

        return validate(
            data,
            DEPARTMENT_SCHEMA,
        )

