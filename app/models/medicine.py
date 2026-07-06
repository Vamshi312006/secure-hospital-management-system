from app.extensions import db


class Medicine(db.Model):
    __tablename__ = "medicines"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(150),
        nullable=False,
        unique=True,
    )

    manufacturer = db.Column(db.String(150))

    dosage = db.Column(db.String(100))

    description = db.Column(db.Text)

    prescription_items = db.relationship(
        "PrescriptionItem",
        back_populates="medicine",
    )

    def __repr__(self):
        return f"<Medicine {self.name}>"
