from datetime import datetime

from app.extensions import db


class Billing(db.Model):
    __tablename__ = "billing"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False,
    )

    amount = db.Column(
        db.Numeric(10, 2),
        nullable=False,
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Pending",
    )

    payment_method = db.Column(
        db.String(50),
    )

    description = db.Column(
        db.Text,
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

    patient = db.relationship(
        "Patient",
        backref="bills",
    )

    def __repr__(self):

        return (
            f"<Billing {self.id}>"
        )
