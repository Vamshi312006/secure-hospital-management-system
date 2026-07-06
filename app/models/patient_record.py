from datetime import datetime

from app.extensions import db


class PatientRecord(db.Model):
    __tablename__ = "patient_records"

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False,
    )

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        nullable=False,
    )

    diagnosis = db.Column(db.Text, nullable=False)

    symptoms = db.Column(db.Text)

    treatment = db.Column(db.Text)

    notes = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    patient = db.relationship(
        "Patient",
        back_populates="records",
    )

    doctor = db.relationship(
        "Doctor",
        back_populates="records",
    )

    prescriptions = db.relationship(
        "Prescription",
        back_populates="record",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<PatientRecord {self.id}>"
