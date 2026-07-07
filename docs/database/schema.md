# Database Schema

## Overview

The Secure Healthcare Platform uses PostgreSQL as its primary relational database. Database access is managed through SQLAlchemy, while schema evolution is handled using Flask-Migrate and Alembic.

The database is designed to separate authentication, authorization, healthcare operations, and security monitoring into independent but related entities.

---

## Database Information

| Property | Value |
|----------|-------|
| Database | secure_healthcare |
| Database Engine | PostgreSQL |
| ORM | SQLAlchemy |
| Migration Tool | Flask-Migrate (Alembic) |

---

## Current Tables

### Authentication

- users
- sessions
- login_attempts

These tables manage user identities, active sessions, and authentication events.

---

### Authorization

- roles
- permissions
- role_permissions

These tables implement Role-Based Access Control (RBAC) by associating permissions with roles rather than individual users.

---

### Healthcare

- patients
- doctors
- departments
- appointments
- patient_records
- prescriptions
- prescription_items
- medicines

These tables store operational healthcare information used by the application.

---

### Security

- audit_logs

This table records security-sensitive actions performed within the system to provide accountability and support future forensic analysis.

---

### Migration Management

- alembic_version

Maintains the current migration version for Flask-Migrate.

---

## Entity Groups

The schema is organized into four logical domains:

### Identity Management

Responsible for authentication and session management.

Tables:

- users
- sessions
- login_attempts

---

### Access Control

Responsible for authorization.

Tables:

- roles
- permissions
- role_permissions

---

### Healthcare Operations

Responsible for clinical workflows.

Tables:

- patients
- doctors
- departments
- appointments
- patient_records
- prescriptions
- prescription_items
- medicines

---

### Security Monitoring

Responsible for accountability and security auditing.

Tables:

- audit_logs

---

## Design Principles

The database follows the following principles:

- Normalized relational design.
- Foreign-key relationships.
- Separation of authentication and authorization.
- Auditability.
- Scalability.
- Security-first architecture.

Additional tables may be introduced as new security capabilities such as detection engineering, alerting, and incident management are implemented.

