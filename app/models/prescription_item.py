from app.extensions import db


class PrescriptionItem(db.Model):
    """
    Represents a single medicine entry inside a prescription.
    """

    __tablename__ = "prescription_items"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    prescription_id = db.Column(
        db.Integer,
        db.ForeignKey("prescriptions.id"),
        nullable=False,
        index=True,
    )

    medicine_id = db.Column(
        db.Integer,
        db.ForeignKey("medicines.id"),
        nullable=False,
        index=True,
    )

    quantity = db.Column(
        db.String(50),
        nullable=False,
    )

    morning = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    afternoon = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    night = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    days = db.Column(
        db.Integer,
        nullable=False,
    )

    notes = db.Column(
        db.Text,
    )

    prescription = db.relationship(
        "Prescription",
        back_populates="items",
    )

    medicine = db.relationship(
        "Medicine",
        back_populates="prescription_items",
    )

    @property
    def frequency(self):
        slots = []

        if self.morning:
            slots.append("Morning")

        if self.afternoon:
            slots.append("Afternoon")

        if self.night:
            slots.append("Night")

        return ", ".join(slots)

    def __repr__(self):
        return (
            f"<PrescriptionItem "
            f"id={self.id} "
            f"medicine={self.medicine_id}>"
        )
