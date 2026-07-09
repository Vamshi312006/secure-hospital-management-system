# 🏥 Secure Healthcare Platform

> A security-first healthcare management platform built with **Flask**, **PostgreSQL**, and **SQLAlchemy**, emphasizing secure authentication, role-based access control, audit logging, and maintainable software architecture.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Status](https://img.shields.io/badge/Status-V1.0.0-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Key Highlights](#key-highlights)
- [Technology Stack](#technology-stack)
- [Architecture Overview](#architecture-overview)

---

# Overview

Secure Healthcare Platform is a security-focused Hospital Management System developed as a flagship cybersecurity engineering project. The application combines healthcare workflows with secure software engineering practices to demonstrate how authentication, authorization, auditing, and modular backend architecture can be integrated into a modern web application.

Unlike a traditional CRUD-based hospital system, this project was designed with security as a primary objective from the beginning. Security mechanisms are implemented as core architectural components rather than being treated as optional additions.

The project follows a layered architecture using Flask Blueprints, SQLAlchemy ORM, PostgreSQL, service-based business logic, schema validation, and security-focused middleware to create a maintainable and extensible backend.

---

# Objectives

The primary goals of this project are:

- Build a secure healthcare management platform.
- Apply secure software engineering principles.
- Demonstrate enterprise-inspired backend architecture.
- Implement authentication and authorization using industry-recommended practices.
- Provide a maintainable codebase through layered design and modular components.
- Serve as a portfolio project showcasing practical cybersecurity engineering skills.

---

# Key Highlights

- Security-first application architecture
- Layered backend design (Routes → Services → Validators → Models)
- Flask Blueprint–based modular architecture
- PostgreSQL database with SQLAlchemy ORM
- Flask-Migrate (Alembic) database migrations
- Secure authentication using Argon2id password hashing
- Role-Based Access Control (RBAC)
- Audit logging and login activity tracking
- Security Center dashboard
- CSRF protection
- Session-based authentication
- Authentication hardening against username enumeration
- Combined IP + username rate limiting
- Enterprise-inspired user interface

---

# Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Backend Framework | Flask |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Database Migration | Flask-Migrate (Alembic) |
| Frontend | HTML, CSS, JavaScript, Jinja2 |
| Authentication | Session-based Authentication |
| Password Hashing | Argon2id |
| Authorization | Role-Based Access Control (RBAC) |
| Rate Limiting | Flask-Limiter |
| CSRF Protection | Flask-WTF |
| Version Control | Git |

---

# Architecture Overview

The project follows a layered architecture to separate responsibilities across the application.

```text
                   User
                     │
                     ▼
             Flask Blueprints
                     │
                     ▼
                 Route Layer
                     │
                     ▼
                Service Layer
                     │
                     ▼
              Validation Layer
                     │
                     ▼
           SQLAlchemy Model Layer
                     │
                     ▼
                PostgreSQL
```

### Architectural Principles

- Separation of concerns
- Modular Blueprints
- Business logic isolated within services
- Centralized validation
- ORM-based database interactions
- Security integrated throughout the application lifecycle
- Maintainable and extensible project structure

---

> **Current Release:** **V1.0.0**  
> This version delivers the complete core healthcare platform with integrated security features, modular architecture, and enterprise-inspired design. Future enhancements are planned for V2 while maintaining compatibility with the V1 foundation.

---

# Core Features

The Secure Healthcare Platform is organized into modular components, each responsible for a specific healthcare workflow. Every module follows a consistent architecture using Routes, Services, Validators, and SQLAlchemy Models to improve maintainability and security.

---

# Application Modules

## Authentication

Provides secure authentication and session management for all users.

### Features

- Secure user login
- Secure logout
- Session-based authentication
- Role-aware authentication
- Last login tracking
- Failed login tracking
- Password verification using Argon2id

---

## Dashboard

Provides a centralized overview of hospital operations.

### Features

- Enterprise-style dashboard
- Quick navigation
- Operational overview
- Security summary
- Activity overview

---

## Patient Management

Manages patient information throughout the healthcare system.

### Features

- Create patient records
- View patient information
- Update patient details
- Delete patient records
- Search patients
- Data validation
- Department integration

---

## Doctor Management

Maintains healthcare professional information.

### Features

- Doctor registration
- Doctor profile management
- Department assignment
- Contact information
- Experience tracking
- Qualification management

---

## Department Management

Organizes hospital departments and their associated doctors.

### Features

- Create departments
- Edit departments
- Delete departments
- View department details
- Doctor relationships

---

## Insurance Management

Maintains insurance provider information.

### Features

- Insurance provider management
- Policy information
- Provider records
- CRUD operations

---

## Appointment Management

Coordinates patient appointments.

### Features

- Appointment scheduling
- Appointment updates
- Appointment cancellation
- Doctor assignment
- Patient assignment
- Appointment status tracking

---

## Medical Records

Stores and manages patient medical history.

### Features

- Medical history
- Diagnosis records
- Clinical notes
- Record management
- Patient linkage
- Doctor linkage

---

## Medicine Management

Maintains the hospital medicine catalog.

### Features

- Medicine inventory records
- Medicine details
- Search medicines
- Prescription integration
- CRUD operations

---

## Prescription Management

Creates and manages prescriptions for patients.

### Features

- Prescription creation
- Multiple medicines per prescription
- Dosage scheduling
- Morning / Afternoon / Night schedules
- Treatment duration
- Quantity management
- Clinical notes
- Prescription history

---

## Billing System

Handles financial operations.

### Features

- Invoice generation
- Invoice management
- Invoice items
- Payment recording
- Billing history
- Payment tracking

---

## Audit Logging

Maintains accountability across the platform.

### Features

- User activity logging
- Resource tracking
- Action tracking
- Success and failure logging
- Timestamp recording

---

## Security Center

Provides operational visibility into security-related events.

### Features

- Login attempt monitoring
- Active session overview
- Audit activity overview
- Recent security events
- Authentication monitoring

---

## Settings

Provides centralized application configuration.

### Features

- Hospital information
- Contact information
- Time zone configuration
- System configuration

---

# Database Design

The application currently contains models representing the major entities of a hospital information system.

| Category | Models |
|-----------|--------|
| User Management | User, Role, Permission, Session |
| Hospital | Department, Doctor, Patient |
| Clinical | Appointment, PatientRecord, Prescription, PrescriptionItem, Medicine |
| Billing | Invoice, InvoiceItem, Payment, Insurance |
| Security | AuditLog, LoginAttempt |
| Configuration | Setting |
| Additional | Notification, UploadedFile, Admission |

---

# Project Structure

```text
app/
├── models/
├── routes/
├── services/
├── validators/
├── middleware/
├── security/
├── rules/
├── utils/
├── enums/
└── errors/

templates/
static/
migrations/
docs/
design/
```

Each module follows a consistent layered architecture:

```text
Blueprint
    │
    ▼
Route
    │
    ▼
Service
    │
    ▼
Validator
    │
    ▼
Model
    │
    ▼
PostgreSQL
```

This structure keeps presentation logic, business logic, validation, and persistence independent, making the application easier to maintain and extend.

---

---

# Security Architecture

Security was treated as a primary design objective throughout the development of this platform. Authentication, authorization, auditing, validation, and secure coding practices were integrated into the application architecture rather than being implemented as afterthoughts.

---

# Authentication

The platform uses session-based authentication with secure password storage using Argon2id.

## Authentication Workflow

```text
User
   │
   ▼
Login Request
   │
   ▼
Input Validation
   │
   ▼
User Lookup
   │
   ▼
Argon2id Password Verification
   │
   ▼
Authentication Successful
   │
   ▼
Session Creation
   │
   ▼
Dashboard
```

### Implemented Features

- Session-based authentication
- Secure login
- Secure logout
- Last login tracking
- Failed login tracking
- Secure password verification
- Automatic password hash upgrades (rehashing)

---

# Password Security

Passwords are never stored in plaintext.

The application uses **Argon2id**, a modern password hashing algorithm designed to resist brute-force and GPU-based attacks.

### Implemented

- Argon2id password hashing
- Automatic salt generation
- Password verification
- Automatic password rehashing when parameters change

---

# Authentication Hardening

Several defensive mechanisms were implemented to strengthen the login process.

## Username Enumeration Resistance

The application performs password verification using a precomputed dummy hash when a username does not exist. This reduces timing differences that could otherwise reveal whether a user account exists.

### Benefits

- Consistent authentication timing
- Reduced information disclosure
- Improved resistance to username enumeration

---

## Generic Authentication Responses

Authentication failures always return the same response regardless of the cause.

```text
Invalid username or password.
```

This prevents attackers from distinguishing between invalid usernames and incorrect passwords.

---

## Rate Limiting

Login requests are protected using Flask-Limiter.

The rate limiting strategy combines both the client's IP address and the submitted username.

```text
Rate Limit Key

IP Address
      +
Username
      ↓

192.168.1.20:administrator
```

### Benefits

- Reduces brute-force attacks
- Prevents excessive authentication attempts
- Limits collateral blocking between different usernames

---

# Authorization

The platform implements **Role-Based Access Control (RBAC)**.

Permissions are assigned to roles, and users inherit permissions through their assigned role.

```text
User
   │
   ▼
Role
   │
   ▼
Permissions
   │
   ▼
Protected Routes
```

### Example Permissions

```text
patient:view
patient:create
patient:update
patient:delete

doctor:view
doctor:create
doctor:update
doctor:delete

billing:payment

audit:view

security:view

setting:update
```

Route protection is enforced using permission decorators before executing application logic.

---

# Session Security

Authenticated users receive server-side sessions.

### Session Information

- User ID
- Username
- Assigned Role
- Session creation
- Last activity
- Expiration timestamp
- Session revocation support

---

# Cross-Site Request Forgery (CSRF)

The application uses **Flask-WTF CSRF Protection**.

All state-changing requests require a valid CSRF token.

### Benefits

- Prevents forged requests
- Protects authenticated users
- Integrates automatically with Flask forms

---

# Audit Logging

Security-relevant actions are recorded for accountability.

Logged information includes:

- User
- Action
- Resource
- Resource ID
- IP Address
- User-Agent
- Status
- Timestamp

Audit logs provide an activity history that supports operational monitoring and incident investigation.

---

# Login Attempt Monitoring

Authentication attempts are recorded separately from audit events.

Recorded information includes:

- Username
- Source IP Address
- Login Status
- Timestamp

This information is displayed within the Security Center.

---

# Security Center

The Security Center provides a consolidated operational view of security-related information.

### Current Features

- Recent login attempts
- Active sessions
- Recent audit events
- Authentication activity overview

---

# Validation Layer

All user input is validated before reaching business logic.

The platform uses centralized validators to enforce:

- Required fields
- Data types
- Length restrictions
- Email validation
- Phone validation
- Date validation
- Choice validation

This reduces duplication and improves consistency across modules.

---

# Database Security

The application follows secure ORM practices using SQLAlchemy.

### Security Measures

- ORM-based database access
- Parameterized SQL generated by SQLAlchemy
- Database migrations managed with Alembic
- Structured relationships using foreign keys

---

# Secure Development Practices

The project follows several secure software engineering principles.

- Layered architecture
- Separation of concerns
- Service-oriented business logic
- Centralized validation
- Least-privilege authorization through RBAC
- Auditability of critical operations
- Security-first authentication design
- Modular and maintainable project organization

---

---

# Installation

## Prerequisites

Before running the application, ensure the following software is installed:

- Python 3.11+
- PostgreSQL
- Git
- pip
- Virtual Environment (recommended)

---

# Clone the Repository

```bash
git clone https://github.com/Vamshi312006/secure-healthcare-platform.git

cd secure-healthcare-platform
```

---

# Create a Virtual Environment

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure PostgreSQL

Create a PostgreSQL database.

Example

```sql
CREATE DATABASE secure_healthcare;
```

Configure your database connection in the application configuration.

Example

```python
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/secure_healthcare"
```

---

# Apply Database Migrations

```bash
flask db upgrade
```

---

# Seed Initial Data

Create the default application data.

```bash
python seed.py

python seed_roles.py

python seed_permissions.py

python seed_departments.py

python seed_rbac.py
```

---

# Run the Application

```bash
python run.py
```

The application will be available at

```
http://127.0.0.1:5000
```

---

# Project Structure

```
secure-healthcare-platform/
│
├── app/
│   ├── enums/
│   ├── errors/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── rules/
│   ├── security/
│   ├── services/
│   ├── utils/
│   ├── validators/
│   ├── extensions.py
│   └── __init__.py
│
├── migrations/
│
├── static/
│
├── templates/
│
├── docs/
│
├── design/
│
├── requirements.txt
│
├── run.py
│
└── README.md
```

---

# Documentation

Additional documentation is available in the `docs/` directory.

| Documentation | Description |
|---------------|-------------|
| Architecture | Overall system architecture |
| Authentication | Authentication design |
| Authorization | RBAC implementation |
| Database | Database design |
| Deployment | Deployment notes |
| Audit | Audit logging |
| API | Backend APIs |
| Detection | Detection engineering notes |
| Decisions | Design decisions |

---

# Testing

The project should be verified after deployment.

Recommended verification steps:

- Login with Administrator account
- Verify CRUD operations for each module
- Verify permission enforcement
- Verify audit log creation
- Verify Security Center
- Verify billing workflow
- Verify prescription workflow
- Verify session creation
- Verify authentication hardening

---

# Current Status

| Component | Status |
|-----------|--------|
| Authentication | ✅ Complete |
| RBAC | ✅ Complete |
| Dashboard | ✅ Complete |
| Patients | ✅ Complete |
| Doctors | ✅ Complete |
| Departments | ✅ Complete |
| Insurance | ✅ Complete |
| Appointments | ✅ Complete |
| Medical Records | ✅ Complete |
| Medicines | ✅ Complete |
| Prescriptions | ✅ Complete |
| Billing | ✅ Complete |
| Audit Logging | ✅ Complete |
| Security Center | ✅ Complete |
| Settings | ✅ Complete |

---

# Known Limitations

Current V1 intentionally focuses on the core healthcare platform.

The following capabilities are planned for future versions:

- Multi-Factor Authentication (MFA)
- Email notifications
- SMS notifications
- Reporting and analytics
- File upload enhancements
- Advanced search
- Real-time notifications
- SIEM integration
- Detection engineering dashboards

---

---

# Screenshots

The following screenshots demonstrate the current V1 user interface.

| Module | Preview |
|----------|---------|
| Login | *Coming Soon* |
| Dashboard | *Coming Soon* |
| Patients | *Coming Soon* |
| Doctors | *Coming Soon* |
| Departments | *Coming Soon* |
| Insurance | *Coming Soon* |
| Appointments | *Coming Soon* |
| Medical Records | *Coming Soon* |
| Medicines | *Coming Soon* |
| Prescriptions | *Coming Soon* |
| Billing | *Coming Soon* |
| Security Center | *Coming Soon* |
| Settings | *Coming Soon* |

> Screenshots will be added under the `design/screenshots/` directory.

---

# Roadmap

## ✅ Version 1.0 (Completed)

### Core Platform

- Authentication
- Dashboard
- Patient Management
- Doctor Management
- Department Management
- Insurance Management
- Appointment Management
- Medical Records
- Medicine Management
- Prescription Management
- Billing System
- Audit Logging
- Security Center
- Settings

### Security

- Argon2id Password Hashing
- Role-Based Access Control (RBAC)
- Session Authentication
- CSRF Protection
- Username Enumeration Resistance
- Combined IP + Username Rate Limiting
- Automatic Password Rehashing
- Audit Logging
- Login Attempt Tracking
- Active Session Tracking

### Backend

- Flask Blueprints
- SQLAlchemy ORM
- PostgreSQL
- Alembic Migrations
- Layered Architecture
- Service Layer
- Validation Layer

---

# Version 2 Roadmap

Future development is planned in the following areas.

## Security

- Multi-Factor Authentication (MFA)
- Password Reset Workflow
- Email Verification
- Account Lockout Policies
- Security Notifications
- API Authentication
- Device Management

---

## Healthcare

- Admission Management
- Room Management
- Laboratory Module
- Pharmacy Inventory
- Nurse Management
- Staff Management
- Discharge Workflow

---

## Analytics

- Administrative Dashboard
- Hospital Reports
- Financial Reports
- Appointment Analytics
- Patient Statistics
- Operational Metrics

---

## Detection Engineering

- Detection Rule Management
- Sigma Rule Integration
- Security Alert Dashboard
- Threat Hunting Views
- Security Event Correlation
- Detection Metrics

---

## Platform

- Docker Deployment
- CI/CD Pipeline
- Unit Testing
- Integration Testing
- API Documentation
- Performance Monitoring

---

# Contributing

This project is currently maintained as a personal cybersecurity engineering portfolio project.

Bug reports, suggestions, and constructive feedback are welcome through GitHub Issues.

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

# Author

**Vamshi Krishna K P**

B.Tech Cyber Security

Amrita Vishwa Vidyapeetham

GitHub:
https://github.com/Vamshi312006

LinkedIn:
https://www.linkedin.com/in/vamshi-krishna-13223366

---

# Acknowledgements

This project was developed as part of a cybersecurity engineering portfolio with the objective of applying secure software engineering principles to a real-world healthcare management system.

Special emphasis was placed on:

- Secure Authentication
- Secure Authorization
- Defensive Programming
- Secure Database Design
- Modular Backend Architecture
- Auditability
- Maintainability

---

# Repository Statistics

| Metric | Value |
|---------|------:|
| Version | **1.0.0** |
| Status | ✅ Feature Complete |
| Backend | Flask |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | Session-Based |
| Authorization | RBAC |
| Password Hashing | Argon2id |
| License | MIT |

---

⭐ If you found this project useful or interesting, consider giving the repository a star.

It helps support the project and encourages future development.
