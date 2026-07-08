from app.extensions import db


class InvoiceItem(db.Model):
    __tablename__ = "invoice_items"

    id = db.Column(db.Integer, primary_key=True)

    invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("invoices.id"),
        nullable=False,
    )

    category = db.Column(
        db.String(50),
        nullable=False,
    )

    description = db.Column(
        db.String(255),
        nullable=False,
    )

    quantity = db.Column(
        db.Integer,
        nullable=False,
        default=1,
    )

    unit_price = db.Column(
        db.Numeric(10,2),
        nullable=False,
    )

    total = db.Column(
        db.Numeric(10,2),
        nullable=False,
    )

    invoice = db.relationship(
        "Invoice",
        backref="items",
    )
