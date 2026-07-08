from app import create_app
from app.extensions import db
from app.models.department import Department

DEPARTMENTS = [
    (
        "Cardiology",
        "Heart and cardiovascular care",
    ),
    (
        "Neurology",
        "Brain and nervous system",
    ),
    (
        "Orthopedics",
        "Bones and joints",
    ),
    (
        "Pediatrics",
        "Children healthcare",
    ),
    (
        "General Medicine",
        "General healthcare",
    ),
    (
        "Emergency",
        "Emergency services",
    ),
    (
        "Radiology",
        "Medical imaging",
    ),
    (
        "Oncology",
        "Cancer treatment",
    ),
    (
        "Dermatology",
        "Skin care",
    ),
    (
        "Pharmacy",
        "Medicine management",
    ),
]

app = create_app()

with app.app_context():

    for name, description in DEPARTMENTS:

        department = Department.query.filter_by(
            name=name,
        ).first()

        if department is None:

            db.session.add(
                Department(
                    name=name,
                    description=description,
                )
            )

            print(f"[+] Added {name}")

        else:

            print(f"[=] {name} already exists")

    db.session.commit()

print("Departments seeded.")
