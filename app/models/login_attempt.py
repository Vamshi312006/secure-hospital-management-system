from datetime import datetime

from app.extensions import db


class LoginAttempt(db.Model):
    __tablename__ = "login_attempts"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        nullable=False,
    )

    ip_address = db.Column(
        db.String(45),
        nullable=False,
    )

    status = db.Column(
        db.String(20),
        nullable=False,
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow,
    )

    def __repr__(self):
        return f"<LoginAttempt {self.username}>"
