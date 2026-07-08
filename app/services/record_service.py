# ==========================================================
# Imports
# ==========================================================

from app.extensions import db

from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.patient_record import PatientRecord

from app.services.audit_service import AuditService


# ==========================================================
# Record Service
# ==========================================================

class RecordService:

    # ------------------------------------------------------
    # Read Operations
    # ------------------------------------------------------

    @staticmethod
    def get_all():

        return (
            PatientRecord.query
            .order_by(
                PatientRecord.created_at.desc()
            )
            .all()
        )


    @staticmethod
    def get_by_id(record_id):

        return db.session.get(
            PatientRecord,
            record_id,
        )


    @staticmethod
    def search(query):

        if not query:
            return RecordService.get_all()

        return (
            PatientRecord.query
            .join(PatientRecord.patient)
            .join(PatientRecord.doctor)
            .join(Doctor.user)
            .filter(
                db.or_(
                    Patient.first_name.ilike(f"%{query}%"),
                    Patient.last_name.ilike(f"%{query}%"),
                    Doctor.specialization.ilike(f"%{query}%"),
                    PatientRecord.diagnosis.ilike(f"%{query}%"),
                )
            )
            .order_by(
                PatientRecord.created_at.desc()
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


    @staticmethod
    def get_doctors():

        return (
            Doctor.query
            .order_by(
                Doctor.specialization
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
        diagnosis,
        symptoms,
        treatment,
        notes,
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

        try:

            record = PatientRecord(

                patient_id=patient_id,

                doctor_id=doctor_id,

                diagnosis=diagnosis,

                symptoms=symptoms,

                treatment=treatment,

                notes=notes,

            )

            db.session.add(
                record
            )

            db.session.commit()

            AuditService.log(
                action="CREATE",
                resource="PatientRecord",
                resource_id=record.id,
            )

            return record

        except Exception:

            db.session.rollback()

            raise


    # ------------------------------------------------------
    # Update Operations
    # ------------------------------------------------------

    @staticmethod
    def update(
        record,
        patient_id,
        doctor_id,
        diagnosis,
        symptoms,
        treatment,
        notes,
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

        record.patient_id = patient_id
        record.doctor_id = doctor_id
        record.diagnosis = diagnosis
        record.symptoms = symptoms
        record.treatment = treatment
        record.notes = notes

        db.session.commit()

        AuditService.log(
            action="UPDATE",
            resource="PatientRecord",
            resource_id=record.id,
        )

        return record


    # ------------------------------------------------------
    # Delete Operations
    # ------------------------------------------------------

    @staticmethod
    def delete(record):

        record_id = record.id

        db.session.delete(
            record
        )

        db.session.commit()

        AuditService.log(
            action="DELETE",
            resource="PatientRecord",
            resource_id=record_id,
        )

