from .home import home_bp
from .auth import auth_bp
from .dashboard import dashboard_bp
from .dev import dev_bp

from .patient import patient_bp
from .doctor import doctor_bp
from .department import department_bp
from .insurance import insurance_bp
from .setting import setting_bp
from .security import security_bp
from .appointment import appointment_bp
from .record import record_bp
from .billing import billing_bp
from .medicine import medicine_bp
from .prescription import prescription_bp
from .audit import audit_bp

__all__ = [
    "home_bp",
    "auth_bp",
    "dashboard_bp",
    "dev_bp",
    "patient_bp",
    "doctor_bp",
    "department_bp",
    "insurance_bp",
    "setting_bp",
    "security_bp",
    "appointment_bp",
    "record_bp",
    "billing_bp",
    "medicine_bp",
    "prescription_bp",
    "audit_bp",
]
