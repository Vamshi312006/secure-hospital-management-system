# Development Environment

## Overview

The Secure Healthcare Platform is developed in a local development environment using Flask and PostgreSQL. Environment-specific configuration is separated from the application code through environment variables.

---

## Development Stack

| Component | Technology |
|-----------|------------|
| Operating System | Kali Linux |
| Programming Language | Python 3 |
| Web Framework | Flask |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migration Tool | Flask-Migrate |
| Password Hashing | Argon2id |
| Version Control | Git |

---

## Environment Variables

Application configuration is loaded from a `.env` file.

Current variables include:

```env
SECRET_KEY=<application secret>
DATABASE_URL=postgresql://secure_admin:********@localhost:5432/secure_healthcare
```

Sensitive configuration should never be committed to version control.

---

## Running the Application

Typical startup sequence:

1. Activate the Python environment.
2. Start the PostgreSQL service.
3. Apply pending migrations.
4. Launch the Flask application.

---

## Database

The application uses PostgreSQL.

Database Name:

- secure_healthcare

Database Owner:

- secure_admin

Schema changes are managed through Flask-Migrate.

---

## Development Principles

The development environment follows these principles:

- Configuration separated from source code.
- Database migrations under version control.
- Reproducible setup.
- Modular architecture.
- Security-first development.

---

## Future Improvements

The development environment will eventually include:

- Docker Compose
- Redis
- Nginx
- Gunicorn
- CI/CD pipeline
- Automated testing
- Security scanning

