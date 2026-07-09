from flask import (
    Blueprint,
    render_template,
)

from app.routes.auth import login_required
from app.security.decorators import permission_required

from app.services.security_service import SecurityService


security_bp = Blueprint(
    "security",
    __name__,
    url_prefix="/security",
)


@security_bp.route("/")
@login_required
@permission_required("security:view")
def index():

    data = SecurityService.dashboard()

    return render_template(
        "security/index.html",
        **data,
    )

