from app import create_app
from app.extensions import db
from app.models.role import Role
from app.models.user import User
from app.services.auth_service import hash_password

app = create_app()

with app.app_context():
    # Create Administrator role
    admin_role = Role.query.filter_by(name="Administrator").first()

    if admin_role is None:
        admin_role = Role(
            name="Administrator",
            description="System Administrator"
        )
        db.session.add(admin_role)
        db.session.commit()
        print("[+] Administrator role created")
    else:
        print("[=] Administrator role already exists")

    # Create admin user
    admin = User.query.filter_by(username="admin").first()

    if admin is None:
        admin = User(
            username="admin",
            email="admin@hospital.local",
            password_hash=hash_password("Admin@123"),
            role_id=admin_role.id,
            is_active=True,
        )

        db.session.add(admin)
        db.session.commit()
        print("[+] Admin user created")
    else:
        print("[=] Admin user already exists")

    print()
    print("Username : admin")
    print("Password : Admin@123")
