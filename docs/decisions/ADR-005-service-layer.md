# ADR-005: Adopt a Service Layer Architecture

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

As the Secure Healthcare Platform grows, implementing business logic directly inside Flask routes would result in large, difficult-to-maintain route handlers. This approach also increases code duplication and makes testing more difficult.

The application requires a clear separation between request handling, business logic, and data persistence.

---

## Decision

The project adopts a dedicated Service Layer architecture.

Routes are responsible for handling HTTP requests and responses, while services contain business logic and coordinate interactions with database models.

---

## Rationale

The Service Layer was selected because it provides:

- Separation of concerns.
- Reusable business logic.
- Cleaner route handlers.
- Easier unit testing.
- Improved maintainability.
- Better scalability as features are added.

Business logic should exist in one place instead of being duplicated across multiple routes.

---

## Responsibilities

### Routes

- Receive HTTP requests.
- Validate request data.
- Call the appropriate service.
- Return HTTP responses.

Routes should remain lightweight.

---

### Services

- Implement business rules.
- Execute workflows.
- Coordinate database operations.
- Perform security-related processing.
- Return results to routes.

Most application logic belongs in this layer.

---

### Models

- Represent database entities.
- Define relationships.
- Handle persistence through SQLAlchemy.

Models should avoid implementing complex business workflows.

---

## Alternatives Considered

### Fat Routes

Advantages:

- Faster to develop for very small projects.
- Fewer files.

Disadvantages:

- Poor maintainability.
- Difficult testing.
- Code duplication.
- Mixing presentation and business logic.

---

### Fat Models

Advantages:

- Centralizes some logic with data.

Disadvantages:

- Large model classes.
- Reduced flexibility.
- Difficult to separate complex workflows.

---

## Consequences

Positive:

- Modular architecture.
- Easier debugging.
- Better code reuse.
- Improved testing.
- Cleaner project organization.

Negative:

- Additional project structure.
- Slight increase in development overhead for small features.

The long-term maintainability benefits outweigh these costs.

---

## Security Implications

Keeping business logic within services allows security controls to be implemented consistently.

Examples include:

- Authentication.
- Authorization.
- Audit logging.
- Session validation.
- Account lockout.
- Detection event generation.

Centralizing these operations reduces the likelihood of inconsistent security behavior across the application.

---

## Related Documentation

- docs/architecture/service_layer.md
- docs/architecture/request_flow.md
- docs/architecture/project_structure.md

