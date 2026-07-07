# Entity Relationship Overview

## Overview

The Secure Healthcare Platform uses a relational database organized into authentication, authorization, healthcare, and security domains. Relationships between entities enforce data integrity and support modular application design.

---

## Authentication

### users

Represents all authenticated users of the system.

Relationships:

- One user may have one role.
- One user may have many sessions.
- One user may have many login attempts.
- One user may generate many audit log entries.

---

## Authorization

### roles

Defines collections of permissions assigned to users.

Relationships:

- One role may be assigned to many users.
- One role may contain many permissions.

### permissions

Defines individual application capabilities.

Relationships:

- Many permissions may belong to many roles.

### role_permissions

Associates roles with permissions.

---

## Healthcare

### departments

Represents hospital departments.

Relationships:

- One department may contain many doctors.

### doctors

Represents healthcare professionals.

Relationships:

- One doctor belongs to one department.
- One doctor may have many appointments.
- One doctor may issue many prescriptions.

### patients

Represents registered patients.

Relationships:

- One patient may have many appointments.
- One patient may have many medical records.
- One patient may have many prescriptions.

### appointments

Represents scheduled consultations.

Relationships:

- One appointment belongs to one patient.
- One appointment belongs to one doctor.

### patient_records

Stores electronic medical records.

Relationships:

- One patient may have many medical records.

### prescriptions

Stores prescriptions issued during treatment.

Relationships:

- One prescription belongs to one patient.
- One prescription belongs to one doctor.
- One prescription may contain many prescription items.

### prescription_items

Represents medicines included within a prescription.

Relationships:

- Many prescription items belong to one prescription.
- One medicine may appear in many prescription items.

### medicines

Stores available medicine information.

---

## Security

### sessions

Tracks authenticated user sessions.

Relationships:

- Many sessions belong to one user.

### login_attempts

Stores login attempt history.

Relationships:

- Many login attempts belong to one user.

### audit_logs

Records security-sensitive application events.

Relationships:

- Many audit log entries may be associated with one user.

---

## Future Expansion

Additional entities planned for future releases include:

- Security alerts
- Detection rules
- Incident cases
- Threat indicators
- Investigation artifacts
- Notification events

These additions will extend the security monitoring capabilities of the platform while preserving the existing relational design.

