from sqlalchemy import or_

from app.extensions import db

from app.models.medicine import Medicine


class MedicineService:

    @staticmethod
    def get_all(search=None):

        query = Medicine.query

        if search:

            pattern = f"%{search.strip()}%"

            query = query.filter(
                or_(
                    Medicine.name.ilike(pattern),
                    Medicine.manufacturer.ilike(pattern),
                    Medicine.dosage.ilike(pattern),
                )
            )

        return (
            query
            .order_by(Medicine.name.asc())
            .all()
        )

    @staticmethod
    def get_by_id(medicine_id):

        return Medicine.query.get(
            medicine_id
        )

    @staticmethod
    def exists(name):

        return (
            Medicine.query.filter(
                Medicine.name.ilike(
                    name.strip()
                )
            ).first()
            is not None
        )


    @staticmethod
    def create(data):

        existing = (
            Medicine.query.filter(
                Medicine.name.ilike(
                    data["name"]
                )
            ).first()
        )

        if existing:

            raise ValueError(
                "Medicine already exists."
            )

        medicine = Medicine(
            name=data["name"],
            manufacturer=data["manufacturer"],
            dosage=data["dosage"],
            description=data["description"],
        )

        db.session.add(
            medicine
        )

        db.session.commit()

        return medicine

    @staticmethod
    def update(
        medicine,
        data,
    ):

        duplicate = (
            Medicine.query.filter(
                Medicine.id != medicine.id,
                Medicine.name.ilike(
                    data["name"]
                ),
            ).first()
        )

        if duplicate:

            raise ValueError(
                "Medicine already exists."
            )

        medicine.name = data["name"]
        medicine.manufacturer = data["manufacturer"]
        medicine.dosage = data["dosage"]
        medicine.description = data["description"]

        db.session.commit()

        return medicine

    @staticmethod
    def delete(
        medicine,
    ):

        if medicine.prescription_items:

            raise ValueError(
                "Medicine is referenced by prescriptions and cannot be deleted."
            )

        db.session.delete(
            medicine
        )

        db.session.commit()

