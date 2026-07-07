from datetime import date

from app.extensions import db
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.appointment import Appointment


class DashboardService:

    @staticmethod
    def get_metrics():

        patient_count = db.session.query(Patient).count()

        doctor_count = db.session.query(Doctor).count()

        today_appointments = (
            db.session.query(Appointment)
            .filter(
                Appointment.appointment_date == date.today()
            )
            .count()
        )

        # Placeholder until session tracking is implemented
        active_sessions = 1

        return {
            "patient_count": patient_count,
            "doctor_count": doctor_count,
            "today_appointments": today_appointments,
            "active_sessions": active_sessions,
            "security_alerts": 0,
        }

