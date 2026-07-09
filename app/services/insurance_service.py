from sqlalchemy import or_

from app.extensions import db
from app.models.insurance import Insurance


class InsuranceService:

    @staticmethod
    def get_all(search=None):

        query = Insurance.query

        if search:

            pattern = f"%{search.strip()}%"

            query = query.filter(
                or_(
                    Insurance.provider.ilike(pattern),
                    Insurance.policy_number.ilike(pattern),
                    Insurance.coverage_type.ilike(pattern),
                )
            )

        return (
            query
            .order_by(Insurance.provider.asc())
            .all()
        )

    @staticmethod
    def get_by_id(insurance_id):

        return db.session.get(
            Insurance,
            insurance_id,
        )

    @staticmethod
    def create(data):

        insurance = Insurance(**data)

        db.session.add(
            insurance
        )

        db.session.commit()

        return insurance

    @staticmethod
    def update(
        insurance,
        data,
    ):

        for key, value in data.items():
            setattr(
                insurance,
                key,
                value,
            )

        db.session.commit()

        return insurance

    @staticmethod
    def delete(
        insurance,
    ):

        db.session.delete(
            insurance
        )

        db.session.commit()

