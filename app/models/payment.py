from datetime import datetime

from app.extensions import db


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)

    invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("invoices.id"),
        nullable=False,
    )

    amount = db.Column(
        db.Numeric(10,2),
        nullable=False,
    )

    method = db.Column(
        db.String(30),
        nullable=False,
    )

    reference_number = db.Column(
        db.String(100),
    )

    received_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    paid_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
    )

    remarks = db.Column(
        db.Text,
    )

    invoice = db.relationship(
        "Invoice",
        backref="payments",
    )

    receiver = db.relationship("User")
