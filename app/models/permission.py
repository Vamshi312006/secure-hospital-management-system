from app.extensions import db


role_permissions = db.Table(
    "role_permissions",

    db.Column(
        "role_id",
        db.Integer,
        db.ForeignKey("roles.id"),
        primary_key=True,
    ),

    db.Column(
        "permission_id",
        db.Integer,
        db.ForeignKey("permissions.id"),
        primary_key=True,
    ),
)


class Permission(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), unique=True, nullable=False)

    description = db.Column(db.Text)

    roles = db.relationship(
        "Role",
        secondary=role_permissions,
        backref="permissions",
    )

    def __repr__(self):
        return f"<Permission {self.name}>"
