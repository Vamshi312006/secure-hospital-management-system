from datetime import datetime

from app.extensions import db


class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True,
    )

    first_name = db.Column(
        db.String(100),
        nullable=False,
    )

    last_name = db.Column(
        db.String(100),
        nullable=False,
    )

    dob = db.Column(db.Date)

    gender = db.Column(
        db.String(20),
    )

    blood_group = db.Column(
        db.String(10),
    )

    phone = db.Column(
        db.String(20),
    )

    email = db.Column(
        db.String(255),
    )

    address = db.Column(
        db.Text,
    )

    emergency_contact = db.Column(
        db.String(100),
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    user = db.relationship(
        "User",
        backref="patient_profile",
    )

    appointments = db.relationship(
        "Appointment",
        back_populates="patient",
    )

    records = db.relationship(
        "PatientRecord",
        back_populates="patient",
    )


    prescriptions = db.relationship(
        "Prescription",
        back_populates="patient",
        cascade="all, delete-orphan",
    )



    def __repr__(self):
        return f"<Patient {self.first_name} {self.last_name}>"
