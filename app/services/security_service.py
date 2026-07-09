from app.models.audit_log import AuditLog
from app.models.login_attempt import LoginAttempt
from app.models.session import Session


class SecurityService:

    @staticmethod
    def dashboard():

        return {

            "active_sessions":
                Session.query.filter_by(
                    is_revoked=False
                ).count(),

            "failed_logins":
                LoginAttempt.query.filter_by(
                    status="FAILED"
                ).count(),

            "successful_logins":
                LoginAttempt.query.filter_by(
                    status="SUCCESS"
                ).count(),

            "audit_events":
                AuditLog.query.count(),

            "recent_logins":
                LoginAttempt.query.order_by(
                    LoginAttempt.timestamp.desc()
                ).limit(10).all(),

            "recent_sessions":
                Session.query.order_by(
                    Session.last_activity.desc()
                ).limit(10).all(),

            "recent_audit":
                AuditLog.query.order_by(
                    AuditLog.created_at.desc()
                ).limit(10).all(),

        }

