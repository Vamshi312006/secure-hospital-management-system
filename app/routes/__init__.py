from .home import home_bp
from .auth import auth_bp
from .dashboard import dashboard_bp
from .dev import dev_bp
from .patient import patient_bp
from .doctor import doctor_bp

__all__ = [
    "home_bp",
    "auth_bp",
    "dashboard_bp",
    "dev_bp",
    "patient_bp",
    "doctor_bp",
]
