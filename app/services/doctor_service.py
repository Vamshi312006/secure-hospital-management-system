from app.extensions import db

from app.models.user import User
from app.models.role import Role
from app.models.doctor import Doctor
from app.models.department import Department

from app.services.auth_service import hash_password
from app.services.audit_service import AuditService


class DoctorService:

    @staticmethod
    def get_all():
        return (
            Doctor.query
            .order_by(Doctor.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_id(doctor_id):
        return db.session.get(Doctor, doctor_id)

    @staticmethod
    def search(query):

        if not query:
            return DoctorService.get_all()

        return (
            Doctor.query
            .join(Doctor.department)
            .filter(
                db.or_(
                    Doctor.license_number.ilike(f"%{query}%"),
                    Doctor.specialization.ilike(f"%{query}%"),
                )
            )
            .all()
        )

    @staticmethod
    def get_departments():
        return (
            Department.query
            .order_by(Department.name)
            .all()
        )

    @staticmethod
    def create(
        username,
        email,
        password,
        license_number,
        specialization,
        phone,
        qualification,
        experience,
        department_id,
    ):

        if User.query.filter_by(username=username).first():
            raise ValueError("Username already exists.")

        if User.query.filter_by(email=email).first():
            raise ValueError("Email already exists.")

        if Doctor.query.filter_by(
            license_number=license_number
        ).first():
            raise ValueError("License number already exists.")

        role = Role.query.filter_by(
            name="Doctor"
        ).first()

        if role is None:
            raise ValueError("Doctor role not found.")

        try:

            user = User(
                username=username,
                email=email,
                password_hash=hash_password(password),
                role_id=role.id,
            )

            db.session.add(user)
            db.session.flush()

            doctor = Doctor(
                user_id=user.id,
                department_id=department_id,
                license_number=license_number,
                specialization=specialization,
                phone=phone,
                qualification=qualification,
                experience=experience,
            )

            db.session.add(doctor)

            db.session.commit()

            AuditService.log(
                action="CREATE",
                resource="Doctor",
                resource_id=doctor.id,
            )

            return doctor

        except Exception:
            db.session.rollback()
            raise

    @staticmethod
    def update(
        doctor,
        specialization,
        phone,
        qualification,
        experience,
        department_id,
    ):

        doctor.specialization = specialization
        doctor.phone = phone
        doctor.qualification = qualification
        doctor.experience = experience
        doctor.department_id = department_id

        db.session.commit()

        AuditService.log(
            action="UPDATE",
            resource="Doctor",
            resource_id=doctor.id,
        )

        return doctor


    @staticmethod
    def delete(doctor):

        user = doctor.user
        doctor_id = doctor.id

        db.session.delete(doctor)

        if user:
            db.session.delete(user)

        db.session.commit()

        AuditService.log(
            action="DELETE",
            resource="Doctor",
            resource_id=doctor_id,
        )

