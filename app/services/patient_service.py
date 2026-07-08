from app.extensions import db

from app.models.user import User
from app.models.role import Role
from app.models.patient import Patient

from app.services.auth_service import hash_password
from app.services.audit_service import AuditService


class PatientService:

    @staticmethod
    def get_all():
        return (
            Patient.query
            .order_by(Patient.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_id(patient_id):
        return db.session.get(Patient, patient_id)

    @staticmethod
    def search(query):

        if not query:
            return PatientService.get_all()

        return (
            Patient.query
            .filter(
                db.or_(
                    Patient.first_name.ilike(f"%{query}%"),
                    Patient.last_name.ilike(f"%{query}%"),
                    Patient.phone.ilike(f"%{query}%"),
                    Patient.email.ilike(f"%{query}%"),
                )
            )
            .all()
        )

    @staticmethod
    def create(
        username,
        email,
        password,
        first_name,
        last_name,
        dob,
        gender,
        blood_group,
        phone,
        address,
        emergency_contact,
    ):

        if User.query.filter_by(username=username).first():
            raise ValueError("Username already exists.")

        if User.query.filter_by(email=email).first():
            raise ValueError("Email already exists.")

        role = Role.query.filter_by(
            name="Patient"
        ).first()

        if role is None:
            raise ValueError("Patient role not found.")

        try:

            user = User(
                username=username,
                email=email,
                password_hash=hash_password(password),
                role_id=role.id,
            )

            db.session.add(user)
            db.session.flush()

            patient = Patient(
                user_id=user.id,
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                gender=gender,
                blood_group=blood_group,
                phone=phone,
                email=email,
                address=address,
                emergency_contact=emergency_contact,
            )

            db.session.add(patient)

            db.session.commit()

            AuditService.log(
                action="CREATE",
                resource="Patient",
                resource_id=patient.id,
            )

            return patient

        except Exception:

            db.session.rollback()
            raise

    @staticmethod
    def update(patient, **kwargs):

        for key, value in kwargs.items():
            setattr(patient, key, value)

        if patient.user:
            patient.user.email = patient.email

        db.session.commit()

        AuditService.log(
            action="UPDATE",
            resource="Patient",
            resource_id=patient.id,
        )

        return patient

    @staticmethod
    def delete(patient):

        user = patient.user
        patient_id = patient.id

        db.session.delete(patient)

        if user:
            db.session.delete(user)

        db.session.commit()

        AuditService.log(
            action="DELETE",
            resource="Patient",
            resource_id=patient_id,
        )
