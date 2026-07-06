from datetime import datetime, timedelta

from app.extensions import db


class Session(db.Model):
    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    session_token = db.Column(
        db.String(255),
        unique=True,
        nullable=False,
    )

    ip_address = db.Column(
        db.String(45),
        nullable=False,
    )

    user_agent = db.Column(
        db.Text,
        nullable=False,
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
    )

    expires_at = db.Column(
        db.DateTime,
        default=lambda: datetime.utcnow() + timedelta(days=7),
    )

    last_activity = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    is_revoked = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    user = db.relationship(
        "User",
        backref="sessions",
    )

    def __repr__(self):
        return f"<Session {self.id}>"
