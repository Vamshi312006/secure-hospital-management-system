from sqlalchemy import or_

from app.extensions import db

from app.models.department import Department


class DepartmentService:

    @staticmethod
    def get_all(search=None):

        query = Department.query

        if search:

            pattern = f"%{search.strip()}%"

            query = query.filter(
                or_(
                    Department.name.ilike(pattern),
                    Department.description.ilike(pattern),
                )
            )

        return (
            query
            .order_by(Department.name.asc())
            .all()
        )

    @staticmethod
    def get_by_id(department_id):

        return db.session.get(
            Department,
            department_id,
        )


    @staticmethod
    def create(data):

        name = data["name"].strip()

        duplicate = (
            Department.query.filter(
                Department.name.ilike(name)
            ).first()
        )

        if duplicate:

            raise ValueError(
                "Department already exists."
            )

        department = Department(
            name=name,
            description=data["description"],
        )

        db.session.add(
            department
        )

        db.session.commit()

        return department

    @staticmethod
    def update(
        department,
        data,
    ):

        name = data["name"].strip()

        duplicate = (
            Department.query.filter(
                Department.id != department.id,
                Department.name.ilike(name),
            ).first()
        )

        if duplicate:

            raise ValueError(
                "Department already exists."
            )

        department.name = name
        department.description = data["description"]

        db.session.commit()

        return department

    @staticmethod
    def delete(
        department,
    ):

        if department.doctors:

            raise ValueError(
                "Department contains doctors and cannot be deleted."
            )

        db.session.delete(
            department
        )

        db.session.commit()

