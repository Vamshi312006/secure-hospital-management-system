from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.routes.auth import login_required
from app.security.decorators import permission_required

from app.services.setting_service import SettingService

from app.validators import (
    SettingValidator,
    ValidationError,
)


setting_bp = Blueprint(
    "setting",
    __name__,
    url_prefix="/settings",
)


@setting_bp.route(
    "/",
    methods=["GET", "POST"],
)
@login_required
@permission_required("setting:update")
def index():

    setting = SettingService.get()

    if request.method == "POST":

        try:

            data = SettingValidator.validate(
                request.form
            )

            SettingService.update(data)

            flash(
                "Settings updated successfully.",
                "success",
            )

            return redirect(
                url_for("setting.index")
            )

        except ValidationError as e:

            flash(
                str(e),
                "danger",
            )

    return render_template(
        "settings/index.html",
        setting=setting,
    )

