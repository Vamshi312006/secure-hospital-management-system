from datetime import date, datetime, timedelta

from app.extensions import db

from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.appointment import Appointment
from app.models.session import Session
from app.models.login_attempt import LoginAttempt
from app.models.audit_log import AuditLog


class DashboardService:

    @staticmethod
    def get_metrics():

        patient_count = (
            db.session.query(Patient)
            .count()
        )

        doctor_count = (
            db.session.query(Doctor)
            .count()
        )

        today_appointments = (
            db.session.query(Appointment)
            .filter(
                Appointment.appointment_date == date.today()
            )
            .count()
        )

        active_sessions = (
            db.session.query(Session)
            .filter(
                Session.is_revoked.is_(False),
                Session.expires_at > datetime.utcnow(),
            )
            .count()
        )

        failed_logins = (
            db.session.query(LoginAttempt)
            .filter(
                LoginAttempt.status == "FAILED"
            )
            .count()
        )

        audit_events = (
            db.session.query(AuditLog)
            .count()
        )

        security_alerts = failed_logins

        brute_force_attempts = (
            db.session.query(LoginAttempt.username)
            .filter(
                LoginAttempt.status == "FAILED",
                LoginAttempt.timestamp >= (
                    datetime.utcnow() - timedelta(minutes=10)
                )
            )
            .group_by(LoginAttempt.username)
            .having(
                db.func.count(LoginAttempt.id) >= 5
            )
            .count()
        )


        recent_audit_events = (
            AuditLog.query
            .order_by(
                AuditLog.created_at.desc()
            )
            .limit(10)
            .all()
        )

        recent_login_attempts = (
            LoginAttempt.query
            .order_by(
                LoginAttempt.timestamp.desc()
            )
            .limit(10)
            .all()
        )

        recent_appointments = (
            Appointment.query
            .order_by(
                Appointment.created_at.desc()
            )
            .limit(10)
            .all()
        )

        return {

            "patient_count": patient_count,

            "doctor_count": doctor_count,

            "today_appointments": today_appointments,

            "active_sessions": active_sessions,

            "failed_logins": failed_logins,

            "audit_events": audit_events,

            "security_alerts": security_alerts,

            "brute_force_attempts": brute_force_attempts,

            "high_risk_sessions": 0,

            "privilege_escalations": 0,

            "critical_events": 0,

            "recent_audit_events": recent_audit_events,

            "recent_login_attempts": recent_login_attempts,

            "recent_appointments": recent_appointments,

        }

