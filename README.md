# Secure Hospital Management System

A security-focused Hospital Management System built with Flask and MySQL. This is Version 0.1 and will evolve into an application security showcase featuring secure authentication, RBAC, audit logging, and secure deployment.

## Live Demo

[https://secure-hospital-management-system.onrender.com](https://secure-hospital-management-system.onrender.com)

## Features

- Patient login and dashboard
- Appointment booking, tracking, and rescheduling
- Doctor profiles
- Medical records, prescriptions, billing, admissions, rooms, insurance, medicines, and staff views

## Tech Stack

- Python
- Flask
- MySQL
- HTML/CSS
- Gunicorn for production serving

## Project Structure

```text
.
|-- app.py
|-- database.py
|-- requirements.txt
|-- render.yaml
|-- static/
|   |-- images/
|   `-- style.css
`-- templates/
```

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and fill in your local MySQL values.
4. Run the app:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000`.

## Environment Variables

| Variable | Description |
| --- | --- |
| `SECRET_KEY` | Flask session secret |
| `FLASK_DEBUG` | Set to `1` for local debug mode |
| `FLASK_RUN_HOST` | Local host binding |
| `PORT` | Application port |
| `DB_HOST` | MySQL host |
| `DB_PORT` | MySQL port |
| `DB_USER` | MySQL username |
| `DB_PASSWORD` | MySQL password |
| `DB_NAME` | MySQL database name |

## Deployment

This project includes `render.yaml` for Render deployment.

Render start command:

```bash
gunicorn app:app
```

Set the database environment variables in the Render dashboard before deploying.

## Screenshots

Add screenshots after deployment:

- Home page
- Login
- Dashboard
- Appointment booking
- Patient profile

## Version

Version 0.1
