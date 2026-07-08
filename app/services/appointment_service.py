# ==========================================================
# Imports
# ==========================================================

from app.extensions import db

from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient

from app.services.audit_service import AuditService


# ==========================================================
# Appointment Service
# ==========================================================

class AppointmentService:

    # ------------------------------------------------------
    # Read Operations
    # ------------------------------------------------------

    @staticmethod
    def get_all():

        return (
            Appointment.query
            .order_by(
                Appointment.appointment_date.desc(),
                Appointment.appointment_time.desc(),
            )
            .all()
        )


    @staticmethod
    def get_by_id(appointment_id):

        return db.session.get(
            Appointment,
            appointment_id,
        )


    @staticmethod
    def search(query):

        if not query:
            return AppointmentService.get_all()

        return (
            Appointment.query
            .join(Appointment.patient)
            .join(Appointment.doctor)
            .join(Doctor.user)
            .filter(
                db.or_(
                    Patient.first_name.ilike(f"%{query}%"),
                    Patient.last_name.ilike(f"%{query}%"),
                    Doctor.specialization.ilike(f"%{query}%"),
                    Appointment.status.ilike(f"%{query}%"),
                )
            )
            .order_by(
                Appointment.appointment_date.desc(),
                Appointment.appointment_time.desc(),
            )
            .all()
        )


    @staticmethod
    def get_doctors():

        return (
            Doctor.query
            .order_by(
                Doctor.specialization
            )
            .all()
        )


    @staticmethod
    def get_patients():

        return (
            Patient.query
            .order_by(
                Patient.first_name,
                Patient.last_name,
            )
            .all()
        )


    # ------------------------------------------------------
    # Create Operations
    # ------------------------------------------------------

    @staticmethod
    def create(
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time,
        status,
        reason,
    ):

        patient = db.session.get(
            Patient,
            patient_id,
        )

        if patient is None:
            raise ValueError(
                "Patient not found."
            )

        doctor = db.session.get(
            Doctor,
            doctor_id,
        )

        if doctor is None:
            raise ValueError(
                "Doctor not found."
            )

        existing = (
            Appointment.query
            .filter_by(
                doctor_id=doctor_id,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
            )
            .first()
        )

        if existing:
            raise ValueError(
                "Doctor already has an appointment at this time."
            )

        try:

            appointment = Appointment(
                patient_id=patient_id,
                doctor_id=doctor_id,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                status=status,
                reason=reason,
            )

            db.session.add(
                appointment
            )

            db.session.commit()

            AuditService.log(
                action="CREATE",
                resource="Appointment",
                resource_id=appointment.id,
            )

            return appointment

        except Exception:

            db.session.rollback()
            raise


    # ------------------------------------------------------
    # Update Operations
    # ------------------------------------------------------

    @staticmethod
    def update(
        appointment,
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time,
        status,
        reason,
    ):

        patient = db.session.get(
            Patient,
            patient_id,
        )

        if patient is None:
            raise ValueError(
                "Patient not found."
            )

        doctor = db.session.get(
            Doctor,
            doctor_id,
        )

        if doctor is None:
            raise ValueError(
                "Doctor not found."
            )

        existing = (
            Appointment.query
            .filter(
                Appointment.doctor_id == doctor_id,
                Appointment.appointment_date == appointment_date,
                Appointment.appointment_time == appointment_time,
                Appointment.id != appointment.id,
            )
            .first()
        )

        if existing:
            raise ValueError(
                "Doctor already has an appointment at this time."
            )

        appointment.patient_id = patient_id
        appointment.doctor_id = doctor_id
        appointment.appointment_date = appointment_date
        appointment.appointment_time = appointment_time
        appointment.status = status
        appointment.reason = reason

        db.session.commit()

        AuditService.log(
            action="UPDATE",
            resource="Appointment",
            resource_id=appointment.id,
        )

        return appointment


    # ------------------------------------------------------
    # Delete Operations
    # ------------------------------------------------------

    @staticmethod
    def delete(appointment):

        appointment_id = appointment.id

        db.session.delete(
            appointment
        )

        db.session.commit()

        AuditService.log(
            action="DELETE",
            resource="Appointment",
            resource_id=appointment_id,
        )

