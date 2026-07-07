# ADR-002: Adopt PostgreSQL as the Primary Database

- **Status:** Accepted
- **Date:** 2026-07-07

## Context

The Secure Healthcare Platform stores sensitive healthcare information, user accounts, audit logs, appointments, and authorization data. The database must provide strong consistency, reliability, transactional integrity, and support for future scalability.

SQLite was sufficient during early prototyping but was not appropriate for the long-term goals of this project.

---

## Decision

PostgreSQL was selected as the primary relational database management system.

All persistent application data is stored within PostgreSQL, and database access is performed through SQLAlchemy ORM.

---

## Rationale

PostgreSQL was selected because it provides:

- Full ACID compliance.
- Strong transactional guarantees.
- Mature security features.
- Excellent performance.
- Rich indexing capabilities.
- Advanced SQL support.
- High reliability.
- Excellent SQLAlchemy compatibility.

These characteristics make PostgreSQL suitable for applications that manage sensitive healthcare data.

---

## Alternatives Considered

### SQLite

Advantages:

- Zero configuration.
- Easy local development.

Disadvantages:

- Limited concurrency.
- Not intended for production-scale applications.
- Fewer advanced database features.

---

### MySQL

Advantages:

- Mature ecosystem.
- Good performance.

Disadvantages:

- PostgreSQL offers more advanced SQL features.
- PostgreSQL aligns better with the project's long-term engineering goals.

---

## Consequences

Positive:

- Improved scalability.
- Better concurrency.
- Strong transactional integrity.
- Production-ready database platform.
- Easier future expansion.

Negative:

- Requires database server installation.
- More administration than SQLite.
- Additional configuration during deployment.

---

## Related Documentation

- docs/database/schema.md
- docs/architecture/overview.md

