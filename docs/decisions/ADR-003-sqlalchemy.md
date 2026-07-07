# ADR-003: Use SQLAlchemy as the Object-Relational Mapper (ORM)

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

The application requires a reliable method for interacting with PostgreSQL while maintaining clean, maintainable, and database-independent code.

Writing raw SQL for every database operation would increase code duplication, reduce maintainability, and make schema evolution more difficult.

---

## Decision

The project uses SQLAlchemy as its primary Object-Relational Mapper (ORM).

Database models represent application entities, while SQLAlchemy manages object persistence, relationships, and query generation.

---

## Rationale

SQLAlchemy was selected because it provides:

- Mature ORM capabilities.
- Excellent PostgreSQL integration.
- Declarative model definitions.
- Relationship management.
- Transaction support.
- Migration support through Flask-Migrate.
- Strong community adoption.

It allows developers to focus on application logic rather than repetitive SQL.

---

## Alternatives Considered

### Raw SQL

Advantages:

- Complete control over queries.
- Potential optimization for specific operations.

Disadvantages:

- Increased code duplication.
- Reduced maintainability.
- Higher risk of SQL injection if implemented incorrectly.
- More difficult schema evolution.

---

### Other ORMs

Alternative Python ORMs were considered but SQLAlchemy offers the most mature ecosystem and integrates seamlessly with Flask.

---

## Consequences

Positive:

- Cleaner codebase.
- Simplified database interactions.
- Easier relationship management.
- Improved maintainability.
- Better compatibility with Flask-Migrate.

Negative:

- Small learning curve.
- Minor ORM overhead compared to handwritten SQL.
- Complex queries may occasionally require raw SQL.

---

## Related Documentation

- docs/database/schema.md
- docs/architecture/service_layer.md
- docs/architecture/application_factory.md

