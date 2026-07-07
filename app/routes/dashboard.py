from flask import Blueprint, render_template

from app.routes.auth import login_required
from app.services.dashboard_service import DashboardService

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    metrics = DashboardService.get_metrics()

    return render_template(
        "dashboard/index.html",
        metrics=metrics,
    )

