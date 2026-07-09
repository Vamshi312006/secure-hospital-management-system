from datetime import datetime

from app.extensions import db


class Setting(db.Model):

    __tablename__ = "settings"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    hospital_name = db.Column(
        db.String(150),
        nullable=False,
        default="Secure Healthcare",
    )

    hospital_address = db.Column(
        db.Text,
    )

    hospital_phone = db.Column(
        db.String(30),
    )

    hospital_email = db.Column(
        db.String(150),
    )

    timezone = db.Column(
        db.String(100),
        default="Asia/Kolkata",
        nullable=False,
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

    def __repr__(self):
        return "<Setting>"
