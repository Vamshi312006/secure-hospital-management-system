from app import create_app
from app.extensions import db
from app.models.role import Role
from app.models.permission import Permission


ROLE_PERMISSIONS = {

    "Administrator": [
        "*",
    ],

    "Doctor": [
        "doctor:view",
        "patient:view",
        "patient:update",
        "appointment:view",
        "appointment:update",
        "billing:view",
        "billing:create",
        "billing:payment",
        "record:view",
        "record:create",
        "record:update",
    ],

    "Receptionist": [
        "doctor:view",
        "patient:view",
        "patient:create",
        "patient:update",
        "appointment:view",
        "appointment:create",
        "appointment:update",
    ],

    "Pharmacist": [
        "patient:view",
        "record:view",
        "billing:view",
    ],


    "Accountant": [
        "billing:view",
        "billing:create",
        "billing:update",
        "billing:delete",
        "billing:payment",
    ],

    "Patient": [
        "patient:view",
    ],
}


app = create_app()

with app.app_context():

    all_permissions = Permission.query.all()

    for role_name, permissions in ROLE_PERMISSIONS.items():

        role = Role.query.filter_by(name=role_name).first()

        if role is None:
            print(f"[-] Role not found: {role_name}")
            continue

        role.permissions.clear()

        if "*" in permissions:

            role.permissions.extend(all_permissions)

        else:

            for permission_name in permissions:

                permission = Permission.query.filter_by(
                    name=permission_name
                ).first()

                if permission is not None:
                    role.permissions.append(permission)

        print(f"[+] Updated {role_name}")

    db.session.commit()

print("RBAC seeding complete.")
