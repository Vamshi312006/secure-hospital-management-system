# ==========================================================
# Imports
# ==========================================================

from flask import (
    Blueprint,
    render_template,
    request,
)

from app.routes.auth import login_required
from app.security.decorators import permission_required

from app.services.audit_service import AuditService


# ==========================================================
# Blueprint
# ==========================================================

audit_bp = Blueprint(
    "audit",
    __name__,
    url_prefix="/audit-logs",
)


# ==========================================================
# Audit Log Listing
# ==========================================================

@audit_bp.route("/")
@login_required
@permission_required("audit:view")
def index():

    query = request.args.get(
        "q",
        "",
    ).strip()

    if query:

        logs = AuditService.search(
            query
        )

    else:

        logs = AuditService.get_all()

    return render_template(
        "audit/index.html",
        logs=logs,
        query=query,
    )


# ==========================================================
# View Audit Log
# ==========================================================

@audit_bp.route("/<int:audit_id>")
@login_required
@permission_required("audit:view")
def view(audit_id):

    log = AuditService.get_by_id(
        audit_id
    )

    if log is None:

        from flask import (
            flash,
            redirect,
            url_for,
        )

        flash(
            "Audit log not found.",
            "danger",
        )

        return redirect(
            url_for("audit.index")
        )

    return render_template(
        "audit/view.html",
        log=log,
    )

