# Password Hashing

## Overview

The Secure Healthcare Platform stores user passwords using Argon2id, a modern password hashing algorithm designed to resist brute-force attacks, GPU acceleration, and specialized password-cracking hardware.

Passwords are never stored in plaintext or encrypted form. Instead, only their cryptographic hashes are stored in the database.

---

## Why Argon2id?

Argon2id was selected because it is currently considered the recommended password hashing algorithm for new applications.

Advantages include:

- Memory-hard design.
- Resistance to GPU attacks.
- Resistance to ASIC attacks.
- Configurable computational cost.
- Protection against brute-force attacks.

---

## Password Storage

When a user creates or changes a password:

1. The plaintext password is received.
2. Argon2id generates a random salt.
3. The password is hashed using Argon2id.
4. Only the resulting hash is stored in the database.

The original password is never stored.

---

## Password Verification

During login:

1. The user submits a password.
2. The stored hash is retrieved.
3. Argon2id hashes the submitted password using the stored parameters.
4. The generated hash is compared with the stored hash.
5. Authentication succeeds only if both hashes match.

---

## Security Benefits

Using Argon2id provides protection against:

- Database compromise.
- Offline password cracking.
- Rainbow table attacks.
- Dictionary attacks.
- High-speed GPU password cracking.

---

## Security Considerations

The application follows these security practices:

- Passwords are never logged.
- Passwords are never recoverable.
- Password verification is performed server-side.
- Plaintext passwords exist only in memory during authentication.

---

## Future Improvements

Future password-related enhancements include:

- Password complexity policies.
- Password history enforcement.
- Password expiration policies.
- Password reset workflow.
- Breached password detection.
- Multi-Factor Authentication (MFA).

