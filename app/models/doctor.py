from datetime import datetime

from app.extensions import db


class Doctor(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True,
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False,
    )

    license_number = db.Column(
        db.String(100),
        unique=True,
        nullable=False,
    )

    specialization = db.Column(
        db.String(100),
        nullable=False,
    )

    phone = db.Column(
        db.String(20),
    )

    qualification = db.Column(
        db.String(255),
    )

    experience = db.Column(
        db.Integer,
        default=0,
    )

    availability = db.Column(
        db.String(255),
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
    )

    user = db.relationship(
        "User",
        backref="doctor_profile",
    )

    department = db.relationship(
        "Department",
        back_populates="doctors",
    )

    appointments = db.relationship(
        "Appointment",
        back_populates="doctor",
    )

    records = db.relationship(
        "PatientRecord",
        back_populates="doctor",
    )

    def __repr__(self):
        return f"<Doctor {self.license_number}>"
