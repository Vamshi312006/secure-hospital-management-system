from app import create_app
from app.extensions import db
from app.models.role import Role

ROLES = [
    (
        "Administrator",
        "Full system access",
    ),
    (
        "Doctor",
        "Doctor account",
    ),
    (
        "Patient",
        "Patient account",
    ),
    (
        "Receptionist",
        "Reception desk",
    ),
    (
        "Pharmacist",
        "Pharmacy operations",
    ),
]


app = create_app()

with app.app_context():

    for name, description in ROLES:

        role = Role.query.filter_by(
            name=name,
        ).first()

        if role is None:

            db.session.add(
                Role(
                    name=name,
                    description=description,
                )
            )

            print(f"[+] Added {name}")

        else:

            print(f"[=] {name} already exists")

    db.session.commit()

print("Done.")
