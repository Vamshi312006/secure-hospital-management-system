from datetime import datetime

from app.extensions import db


class Appointment(db.Model):
    __tablename__ = "appointments"

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

    appointment_date = db.Column(
        db.Date,
        nullable=False,
    )

    appointment_time = db.Column(
        db.Time,
        nullable=False,
    )

    status = db.Column(
        db.String(30),
        default="Booked",
        nullable=False,
    )

    reason = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
    )

    patient = db.relationship(
        "Patient",
        back_populates="appointments",
    )

    doctor = db.relationship(
        "Doctor",
        back_populates="appointments",
    )

    def __repr__(self):
        return f"<Appointment {self.id}>"
