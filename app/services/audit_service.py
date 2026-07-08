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

