from app import create_app
from app.extensions import db
from app.models.permission import Permission

PERMISSIONS = [

    # Doctor
    ("doctor:view", "View doctors"),
    ("doctor:create", "Create doctors"),
    ("doctor:update", "Update doctors"),
    ("doctor:delete", "Delete doctors"),

    # Patient
    ("patient:view", "View patients"),
    ("patient:create", "Create patients"),
    ("patient:update", "Update patients"),
    ("patient:delete", "Delete patients"),

    # Appointment
    ("appointment:view", "View appointments"),
    ("appointment:create", "Create appointments"),
    ("appointment:update", "Update appointments"),
    ("appointment:delete", "Delete appointments"),

    # Medical Records
    ("record:view", "View records"),
    ("record:create", "Create records"),
    ("record:update", "Update records"),
    ("record:delete", "Delete records"),

    # Billing
    ("billing:view", "View billing"),
    ("billing:create", "Create billing"),
    ("billing:update", "Update billing"),
    ("billing:delete", "Delete billing"),
    ("billing:payment", "Receive payments"),

    # Administration
    ("admin:access", "Administrative access"),

    # Audit
    ("audit:view", "View audit logs"),
]

app = create_app()

with app.app_context():

    for name, description in PERMISSIONS:

        permission = Permission.query.filter_by(
            name=name
        ).first()

        if permission is None:

            db.session.add(
                Permission(
                    name=name,
                    description=description,
                )
            )

            print(f"[+] {name}")

        else:

            print(f"[=] {name}")

    db.session.commit()

print("Done.")
