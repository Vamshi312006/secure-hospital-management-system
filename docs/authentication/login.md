# User Authentication

## Overview

Authentication is the first security boundary of the Secure Healthcare Platform. Every user must successfully authenticate before accessing protected resources.

The platform currently supports username/email and password-based authentication using secure password hashing with Argon2id.

---

## Authentication Flow

The login process follows these steps:

1. User opens the login page.
2. User enters a username (or email) and password.
3. The server validates the submitted data.
4. The application searches for the corresponding user account.
5. The submitted password is verified against the stored Argon2id hash.
6. If authentication succeeds, a session is created.
7. The user is redirected to the dashboard.
8. If authentication fails, access is denied and the attempt may be logged.

---

## Authentication Components

Current authentication consists of:

- User credentials
- Password verification
- Session creation
- Protected routes

Future enhancements include:

- Account lockout
- Multi-Factor Authentication (MFA)
- Password reset
- Session expiration
- Device tracking

---

## Security Goals

Authentication is designed to:

- Verify user identity.
- Prevent unauthorized access.
- Protect stored passwords.
- Support future audit logging.
- Support secure session management.

---

## Authentication Process

```text
User
  │
  ▼
Login Form
  │
  ▼
Input Validation
  │
  ▼
User Lookup
  │
  ▼
Password Verification (Argon2id)
  │
  ▼
Authentication Successful?
  │
 ├─────────────── No ───────────────► Reject Request
 │
 ▼
Create Session
 │
 ▼
Redirect to Dashboard
```

---

## Current Security Controls

Current implementation includes:

- Argon2id password hashing.
- Server-side authentication.
- Session-based authentication.
- Input validation.

Future versions will introduce additional defensive controls such as login attempt monitoring, account lockout, audit logging, and anomaly detection.

