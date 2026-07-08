from .base import ValidationError
from .schema import validate

from .patient import PatientValidator
from .doctor import DoctorValidator
from .appointment import AppointmentValidator
from .record import RecordValidator
