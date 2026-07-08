from app.validators.base import ValidationError


def validate(data, schema):

    cleaned = {}

    for name, field in schema.items():

        cleaned[name] = field.validate(
            name.replace("_", " ").title(),
            data.get(name),
        )

    return cleaned
