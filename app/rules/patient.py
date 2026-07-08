from datetime import date

from app.rules.base import BusinessRuleError


class PatientRules:

    @staticmethod
    def validate(data):

        dob = data["dob"]

        age = (
            date.today().year
            - dob.year
            - (
                (date.today().month, date.today().day)
                <
                (dob.month, dob.day)
            )
        )

        if age > 120:
            raise BusinessRuleError(
                "Patient age cannot exceed 120 years."
            )

        if age < 0:
            raise BusinessRuleError(
                "Invalid patient age."
            )

        return data
