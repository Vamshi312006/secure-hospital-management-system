from datetime import datetime

from app.extensions import db


class Prescription(db.Model):
    __tablename__ = "prescriptions"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False,
        index=True,
    )

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        nullable=False,
        index=True,
    )

    record_id = db.Column(
        db.Integer,
        db.ForeignKey("patient_records.id"),
        nullable=False,
        index=True,
    )

    prescription_date = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    instructions = db.Column(
        db.Text,
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    patient = db.relationship(
        "Patient",
        back_populates="prescriptions",
    )

    doctor = db.relationship(
        "Doctor",
        back_populates="prescriptions",
    )

    record = db.relationship(
        "PatientRecord",
        back_populates="prescriptions",
    )

    items = db.relationship(
        "PrescriptionItem",
        back_populates="prescription",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    @property
    def total_items(self):
        return len(self.items)

    def __repr__(self):
        return (
            f"<Prescription "
            f"id={self.id} "
            f"patient={self.patient_id} "
            f"doctor={self.doctor_id}>"
        )
