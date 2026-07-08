from datetime import datetime

from app.extensions import db


class Invoice(db.Model):
    __tablename__ = "invoices"

    id = db.Column(db.Integer, primary_key=True)

    invoice_number = db.Column(
        db.String(30),
        unique=True,
        nullable=False,
    )

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False,
    )

    created_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    issued_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    due_date = db.Column(
        db.DateTime,
    )

    subtotal = db.Column(
        db.Numeric(10,2),
        nullable=False,
        default=0,
    )

    discount = db.Column(
        db.Numeric(10,2),
        nullable=False,
        default=0,
    )

    tax = db.Column(
        db.Numeric(10,2),
        nullable=False,
        default=0,
    )

    total = db.Column(
        db.Numeric(10,2),
        nullable=False,
        default=0,
    )

    amount_paid = db.Column(
        db.Numeric(10,2),
        nullable=False,
        default=0,
    )

    balance = db.Column(
        db.Numeric(10,2),
        nullable=False,
        default=0,
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Draft",
    )

    notes = db.Column(
        db.Text,
    )

    patient = db.relationship("Patient")

    creator = db.relationship("User")
