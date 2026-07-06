from datetime import datetime

from app.extensions import db


class Prescription(db.Model):
    __tablename__ = "prescriptions"

    id = db.Column(db.Integer, primary_key=True)

    record_id = db.Column(
        db.Integer,
        db.ForeignKey("patient_records.id"),
        nullable=False,
    )

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctors.id"),
        nullable=False,
    )

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False,
    )

    prescription_date = db.Column(
        db.DateTime,
        default=datetime.utcnow,
    )

    instructions = db.Column(db.Text)

    record = db.relationship(
        "PatientRecord",
        back_populates="prescriptions",
    )

    items = db.relationship(
        "PrescriptionItem",
        back_populates="prescription",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Prescription {self.id}>"
