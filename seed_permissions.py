from app import create_app
from app.extensions import db
from app.models.permission import Permission

PERMISSIONS = [

    # Doctor
    ("doctor:view", "View doctors"),
    ("doctor:create", "Create doctors"),
    ("doctor:update", "Update doctors"),
    ("doctor:delete", "Delete doctors"),


    # Department
    ("department:view", "View departments"),
    ("department:create", "Create departments"),
    ("department:update", "Update departments"),
    ("department:delete", "Delete departments"),

    # Patient
    ("patient:view", "View patients"),
    ("patient:create", "Create patients"),
    ("patient:update", "Update patients"),
    ("patient:delete", "Delete patients"),


    # Insurance
    ("insurance:view", "View insurance"),
    ("insurance:create", "Create insurance"),
    ("insurance:update", "Update insurance"),
    ("insurance:delete", "Delete insurance"),

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

    # Medicine
    ("medicine:view", "View medicines"),
    ("medicine:create", "Create medicines"),
    ("medicine:update", "Update medicines"),
    ("medicine:delete", "Delete medicines"),

    # Prescription
    ("prescription:view", "View prescriptions"),
    ("prescription:create", "Create prescriptions"),
    ("prescription:update", "Update prescriptions"),
    ("prescription:delete", "Delete prescriptions"),


    # Settings
    ("setting:update", "Manage system settings"),


    # Security
    ("security:view", "View security center"),

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
