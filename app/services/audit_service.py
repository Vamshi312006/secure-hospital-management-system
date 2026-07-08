from flask import request, session

from app.extensions import db
from app.models.audit_log import AuditLog


class AuditService:

    @staticmethod
    def log(
        action,
        resource,
        resource_id=None,
        status="SUCCESS",
    ):

        audit = AuditLog(

            user_id=session.get("user_id"),

            action=action,

            resource=resource,

            resource_id=resource_id,

            ip_address=request.remote_addr,

            user_agent=request.user_agent.string,

            status=status,
        )

        db.session.add(audit)

        db.session.commit()

        return audit


    # ------------------------------------------------------
    # Read Operations
    # ------------------------------------------------------

    @staticmethod
    def get_all():

        return (
            AuditLog.query
            .order_by(
                AuditLog.created_at.desc()
            )
            .all()
        )


    @staticmethod
    def get_by_id(audit_id):

        return db.session.get(
            AuditLog,
            audit_id,
        )


    @staticmethod
    def search(query):

        if not query:
            return AuditService.get_all()

        return (
            AuditLog.query
            .filter(
                db.or_(
                    AuditLog.action.ilike(f"%{query}%"),
                    AuditLog.resource.ilike(f"%{query}%"),
                    AuditLog.status.ilike(f"%{query}%"),
                )
            )
            .order_by(
                AuditLog.created_at.desc()
            )
            .all()
        )

