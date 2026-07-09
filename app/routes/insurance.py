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

from app.services.insurance_service import InsuranceService

from app.validators import (
    InsuranceValidator,
    ValidationError,
)


insurance_bp = Blueprint(
    "insurance",
    __name__,
    url_prefix="/insurance",
)


@insurance_bp.route("/")
@login_required
@permission_required("insurance:view")
def index():

    query = request.args.get(
        "q",
        "",
    )

    insurance = InsuranceService.get_all(
        query
    )

    return render_template(
        "insurance/index.html",
        insurance=insurance,
        query=query,
    )


@insurance_bp.route(
    "/new",
    methods=["GET"],
)
@login_required
@permission_required("insurance:create")
def new():

    return render_template(
        "insurance/form.html",
        insurance=None,
        edit_mode=False,
    )


@insurance_bp.route(
    "/new",
    methods=["POST"],
)
@login_required
@permission_required("insurance:create")
def create():

    try:

        data = InsuranceValidator.validate_create(
            request.form
        )

        insurance = InsuranceService.create(
            data
        )

        flash(
            "Insurance created successfully.",
            "success",
        )

        return redirect(
            url_for(
                "insurance.view",
                insurance_id=insurance.id,
            )
        )

    except (
        ValidationError,
        ValueError,
    ) as e:

        flash(
            str(e),
            "danger",
        )

        return redirect(
            url_for(
                "insurance.new"
            )
        )


@insurance_bp.route("/<int:insurance_id>")
@login_required
@permission_required("insurance:view")
def view(insurance_id):

    insurance = InsuranceService.get_by_id(
        insurance_id
    )

    if insurance is None:

        flash(
            "Insurance not found.",
            "danger",
        )

        return redirect(
            url_for("insurance.index")
        )

    return render_template(
        "insurance/view.html",
        insurance=insurance,
    )


@insurance_bp.route(
    "/<int:insurance_id>/edit",
    methods=["GET", "POST"],
)
@login_required
@permission_required("insurance:update")
def edit(insurance_id):

    insurance = InsuranceService.get_by_id(
        insurance_id
    )

    if insurance is None:

        flash(
            "Insurance not found.",
            "danger",
        )

        return redirect(
            url_for("insurance.index")
        )

    if request.method == "POST":

        try:

            data = InsuranceValidator.validate_update(
                request.form
            )

            InsuranceService.update(
                insurance,
                data,
            )

            flash(
                "Insurance updated successfully.",
                "success",
            )

            return redirect(
                url_for(
                    "insurance.view",
                    insurance_id=insurance.id,
                )
            )

        except (
            ValidationError,
            ValueError,
        ) as e:

            flash(
                str(e),
                "danger",
            )

    return render_template(
        "insurance/form.html",
        insurance=insurance,
        edit_mode=True,
    )


@insurance_bp.route(
    "/<int:insurance_id>/delete",
    methods=["POST"],
)
@login_required
@permission_required("insurance:delete")
def delete(insurance_id):

    insurance = InsuranceService.get_by_id(
        insurance_id
    )

    if insurance is not None:

        InsuranceService.delete(
            insurance
        )

        flash(
            "Insurance deleted successfully.",
            "success",
        )

    return redirect(
        url_for("insurance.index")
    )

