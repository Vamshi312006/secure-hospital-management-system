from app.extensions import db


class Insurance(db.Model):

    __tablename__ = "insurance"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    provider = db.Column(
        db.String(150),
        nullable=False,
        unique=True,
    )

    policy_number = db.Column(
        db.String(150),
        nullable=False,
        unique=True,
    )

    coverage_type = db.Column(
        db.String(100),
    )

    contact_number = db.Column(
        db.String(30),
    )

    email = db.Column(
        db.String(150),
    )

    def __repr__(self):
        return f"<Insurance {self.provider}>"
