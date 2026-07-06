from app.extensions import db


class PrescriptionItem(db.Model):
    __tablename__ = "prescription_items"

    id = db.Column(db.Integer, primary_key=True)

    prescription_id = db.Column(
        db.Integer,
        db.ForeignKey("prescriptions.id"),
        nullable=False,
    )

    medicine_id = db.Column(
        db.Integer,
        db.ForeignKey("medicines.id"),
        nullable=False,
    )

    morning = db.Column(db.Boolean, default=False)

    afternoon = db.Column(db.Boolean, default=False)

    night = db.Column(db.Boolean, default=False)

    days = db.Column(db.Integer, nullable=False)

    prescription = db.relationship(
        "Prescription",
        back_populates="items",
    )

    medicine = db.relationship(
        "Medicine",
        back_populates="prescription_items",
    )

    def __repr__(self):
        return f"<PrescriptionItem {self.id}>"
