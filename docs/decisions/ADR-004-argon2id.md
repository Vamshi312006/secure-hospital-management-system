# ADR-004: Use Argon2id for Password Hashing

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

User passwords are among the most sensitive assets within the application. If the database is compromised, stored passwords must remain computationally difficult to recover.

The project requires a password hashing algorithm that is resistant to modern password-cracking techniques, including GPU-accelerated and ASIC-based attacks.

---

## Decision

The Secure Healthcare Platform uses Argon2id as its password hashing algorithm.

Password hashing and verification are performed using Argon2id before authentication succeeds.

Passwords are never stored, transmitted, or logged in plaintext.

---

## Rationale

Argon2id was selected because it is the winner of the Password Hashing Competition (PHC) and is widely recommended for new applications.

Advantages include:

- Memory-hard design.
- GPU-resistant.
- ASIC-resistant.
- Configurable time and memory cost.
- Built-in salting.
- Strong protection against offline attacks.

These properties significantly increase the computational cost of password cracking after a database compromise.

---

## Alternatives Considered

### bcrypt

Advantages:

- Mature.
- Widely supported.
- Proven in production.

Disadvantages:

- Limited memory hardness.
- Less resistant to modern GPU hardware.

---

### PBKDF2

Advantages:

- Standardized.
- Broad compatibility.

Disadvantages:

- CPU-intensive only.
- Less effective against specialized hardware.

---

### scrypt

Advantages:

- Memory-hard.
- Better than bcrypt against GPU attacks.

Disadvantages:

- Less commonly recommended than Argon2id for new applications.

---

## Consequences

Positive:

- Strong password protection.
- Increased resistance to brute-force attacks.
- Better long-term security.
- Alignment with current security recommendations.

Negative:

- Higher computational cost during login.
- Slightly increased server resource usage.

These trade-offs are acceptable because authentication occurs infrequently compared to normal application requests.

---

## Security Implications

Using Argon2id helps protect against:

- Database compromise.
- Offline password cracking.
- Dictionary attacks.
- Rainbow table attacks.
- GPU-based brute-force attacks.

---

## Related Documentation

- docs/authentication/password_hashing.md
- docs/authentication/login.md

