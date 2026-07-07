# Database Migrations

## Overview

The Secure Healthcare Platform uses Flask-Migrate with Alembic to manage database schema changes.

Rather than modifying the database manually, every schema change is recorded as a version-controlled migration. This ensures that all environments remain synchronized and that database changes are reproducible.

---

## Migration Toolchain

| Component | Purpose |
|-----------|---------|
| Flask-Migrate | Integrates Alembic with Flask |
| Alembic | Generates and applies schema migrations |
| SQLAlchemy | Defines database models |

---

## Migration Workflow

The typical workflow is:

1. Modify SQLAlchemy models.
2. Generate a migration.
3. Review the generated migration.
4. Apply the migration.
5. Commit both the migration and model changes.

---

## Common Commands

Initialize migrations (performed once):

```bash
flask db init
```

Generate a migration:

```bash
flask db migrate -m "Describe the change"
```

Apply pending migrations:

```bash
flask db upgrade
```

Rollback the most recent migration:

```bash
flask db downgrade
```

Display migration history:

```bash
flask db history
```

Show the current migration version:

```bash
flask db current
```

---

## Migration Files

Migration scripts are stored in the `migrations/` directory.

Each migration records:

- Schema changes.
- Upgrade operations.
- Downgrade operations.
- Revision identifiers.

These files are committed to version control.

---

## Best Practices

- Never modify production tables manually.
- Review generated migrations before applying them.
- Keep migrations small and focused.
- Test migrations before deployment.
- Commit migration files together with model changes.

---

## Current State

The project tracks database schema versions using the `alembic_version` table. This allows Flask-Migrate to determine which migrations have already been applied.

---

## Future Considerations

As the platform evolves, migrations will manage changes related to:

- Authentication enhancements.
- RBAC improvements.
- Audit logging.
- Detection engine.
- Incident management.
- Healthcare data model expansion.

