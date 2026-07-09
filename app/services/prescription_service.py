from sqlalchemy.orm import joinedload

from app.extensions import db

from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.medicine import Medicine
from app.models.patient_record import PatientRecord
from app.models.prescription import Prescription
from app.models.prescription_item import PrescriptionItem

from app.services.audit_service import AuditService


class PrescriptionService:

    @staticmethod
    def get_all():

        return (
            Prescription.query
            .options(
                joinedload(Prescription.patient),
                joinedload(Prescription.doctor),
                joinedload(Prescription.record),
                joinedload(Prescription.items)
                .joinedload(PrescriptionItem.medicine),
            )
            .order_by(
                Prescription.prescription_date.desc()
            )
            .all()
        )

    @staticmethod
    def get_by_id(
        prescription_id,
    ):

        return (
            Prescription.query
            .options(
                joinedload(Prescription.patient),
                joinedload(Prescription.doctor),
                joinedload(Prescription.record),
                joinedload(Prescription.items)
                .joinedload(PrescriptionItem.medicine),
            )
            .filter_by(
                id=prescription_id
            )
            .first()
        )

    @staticmethod
    def search(
        query,
    ):

        if not query:
            return PrescriptionService.get_all()

        return (
            Prescription.query
            .join(Patient)
            .join(Doctor)
            .filter(
                db.or_(
                    Patient.first_name.ilike(
                        f"%{query}%"
                    ),
                    Patient.last_name.ilike(
                        f"%{query}%"
                    ),
                    Doctor.license_number.ilike(
                        f"%{query}%"
                    ),
                )
            )
            .order_by(
                Prescription.prescription_date.desc()
            )
            .all()
        )

    @staticmethod
    def get_records():

        return (
            PatientRecord.query
            .options(
                joinedload(
                    PatientRecord.patient
                ),
                joinedload(
                    PatientRecord.doctor
                ),
            )
            .order_by(
                PatientRecord.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_medicines():

        return (
            Medicine.query
            .order_by(
                Medicine.name.asc()
            )
            .all()
        )

    @staticmethod
    def create(
        *,
        patient_id,
        doctor_id,
        record_id,
        instructions,
        items,
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

        record = db.session.get(
            PatientRecord,
            record_id,
        )

        if record is None:
            raise ValueError(
                "Medical record not found."
            )

        if record.patient_id != patient.id:
            raise ValueError(
                "Selected record does not belong to the selected patient."
            )

        if record.doctor_id != doctor.id:
            raise ValueError(
                "Selected record does not belong to the selected doctor."
            )

        if not items:
            raise ValueError(
                "At least one medicine is required."
            )

        try:

            prescription = Prescription(
                patient_id=patient.id,
                doctor_id=doctor.id,
                record_id=record.id,
                instructions=instructions,
            )

            db.session.add(
                prescription
            )

            db.session.flush()

            for item in items:

                medicine = db.session.get(
                    Medicine,
                    item["medicine_id"],
                )

                if medicine is None:
                    raise ValueError(
                        f"Medicine ID {item['medicine_id']} not found."
                    )

                prescription_item = PrescriptionItem(
                    prescription_id=prescription.id,
                    medicine_id=medicine.id,
                    quantity=item["quantity"],
                    morning=item.get(
                        "morning",
                        False,
                    ),
                    afternoon=item.get(
                        "afternoon",
                        False,
                    ),
                    night=item.get(
                        "night",
                        False,
                    ),
                    days=item["days"],
                    notes=item.get(
                        "notes",
                    ),
                )

                db.session.add(
                    prescription_item
                )

            db.session.commit()

            AuditService.log(
                action="CREATE",
                resource="Prescription",
                resource_id=prescription.id,
            )

            return prescription

        except Exception:

            db.session.rollback()
            raise

    @staticmethod
    def update(
        prescription,
        *,
        patient_id,
        doctor_id,
        record_id,
        instructions,
        items,
    ):

        if prescription is None:
            raise ValueError(
                "Prescription not found."
            )

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

        record = db.session.get(
            PatientRecord,
            record_id,
        )

        if record is None:
            raise ValueError(
                "Medical record not found."
            )

        if record.patient_id != patient.id:
            raise ValueError(
                "Selected record does not belong to the selected patient."
            )

        if record.doctor_id != doctor.id:
            raise ValueError(
                "Selected record does not belong to the selected doctor."
            )

        if not items:
            raise ValueError(
                "At least one medicine is required."
            )

        try:

            prescription.patient_id = patient.id
            prescription.doctor_id = doctor.id
            prescription.record_id = record.id
            prescription.instructions = instructions

            PrescriptionItem.query.filter_by(
                prescription_id=prescription.id
            ).delete()

            db.session.flush()

            for item in items:

                medicine = db.session.get(
                    Medicine,
                    item["medicine_id"],
                )

                if medicine is None:
                    raise ValueError(
                        f"Medicine ID {item['medicine_id']} not found."
                    )

                db.session.add(
                    PrescriptionItem(
                        prescription_id=prescription.id,
                        medicine_id=medicine.id,
                        quantity=item["quantity"],
                        morning=item.get(
                            "morning",
                            False,
                        ),
                        afternoon=item.get(
                            "afternoon",
                            False,
                        ),
                        night=item.get(
                            "night",
                            False,
                        ),
                        days=item["days"],
                        notes=item.get(
                            "notes",
                        ),
                    )
                )

            db.session.commit()

            AuditService.log(
                action="UPDATE",
                resource="Prescription",
                resource_id=prescription.id,
            )

            return prescription

        except Exception:

            db.session.rollback()
            raise


    @staticmethod
    def delete(
        prescription,
    ):

        if prescription is None:
            raise ValueError(
                "Prescription not found."
            )

        prescription_id = prescription.id

        try:

            db.session.delete(
                prescription
            )

            db.session.commit()

            AuditService.log(
                action="DELETE",
                resource="Prescription",
                resource_id=prescription_id,
            )

        except Exception:

            db.session.rollback()
            raise


    @staticmethod
    def get_patients():

        return (
            Patient.query
            .order_by(
                Patient.first_name.asc(),
                Patient.last_name.asc(),
            )
            .all()
        )


    @staticmethod
    def get_doctors():

        return (
            Doctor.query
            .order_by(
                Doctor.license_number.asc(),
            )
            .all()
        )

