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

from app.services.medicine_service import MedicineService

from app.validators import (
    MedicineValidator,
    ValidationError,
)


medicine_bp = Blueprint(
    "medicine",
    __name__,
    url_prefix="/medicines",
)


@medicine_bp.route("/")
@login_required
@permission_required("medicine:view")
def index():

    query = request.args.get(
        "q",
        "",
    )

    medicines = MedicineService.get_all(
        query
    )

    return render_template(
        "medicines/index.html",
        medicines=medicines,
        query=query,
    )


@medicine_bp.route(
    "/new",
    methods=["GET"],
)
@login_required
@permission_required("medicine:create")
def new():

    return render_template(
        "medicines/form.html",
        medicine=None,
        edit_mode=False,
    )


@medicine_bp.route(
    "/new",
    methods=["POST"],
)
@login_required
@permission_required("medicine:create")
def create():

    try:

        data = MedicineValidator.validate_create(
            request.form
        )

        medicine = MedicineService.create(
            data
        )

        flash(
            "Medicine created successfully.",
            "success",
        )

        return redirect(
            url_for(
                "medicine.view",
                medicine_id=medicine.id,
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
                "medicine.new"
            )
        )


@medicine_bp.route(
    "/<int:medicine_id>",
)
@login_required
@permission_required("medicine:view")
def view(
    medicine_id,
):

    medicine = MedicineService.get_by_id(
        medicine_id
    )

    if medicine is None:

        flash(
            "Medicine not found.",
            "danger",
        )

        return redirect(
            url_for(
                "medicine.index"
            )
        )

    return render_template(
        "medicines/view.html",
        medicine=medicine,
    )


@medicine_bp.route(
    "/<int:medicine_id>/edit",
    methods=["GET"],
)
@login_required
@permission_required("medicine:update")
def edit(
    medicine_id,
):

    medicine = MedicineService.get_by_id(
        medicine_id
    )

    if medicine is None:

        flash(
            "Medicine not found.",
            "danger",
        )

        return redirect(
            url_for(
                "medicine.index"
            )
        )

    return render_template(
        "medicines/form.html",
        medicine=medicine,
        edit_mode=True,
    )


@medicine_bp.route(
    "/<int:medicine_id>/edit",
    methods=["POST"],
)
@login_required
@permission_required("medicine:update")
def update(
    medicine_id,
):

    medicine = MedicineService.get_by_id(
        medicine_id
    )

    if medicine is None:

        flash(
            "Medicine not found.",
            "danger",
        )

        return redirect(
            url_for(
                "medicine.index"
            )
        )

    try:

        data = MedicineValidator.validate_update(
            request.form
        )

        MedicineService.update(
            medicine,
            data,
        )

        flash(
            "Medicine updated successfully.",
            "success",
        )

        return redirect(
            url_for(
                "medicine.view",
                medicine_id=medicine.id,
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
                "medicine.edit",
                medicine_id=medicine.id,
            )
        )


@medicine_bp.route(
    "/<int:medicine_id>/delete",
    methods=["POST"],
)
@login_required
@permission_required("medicine:delete")
def delete(
    medicine_id,
):

    medicine = MedicineService.get_by_id(
        medicine_id
    )

    if medicine is None:

        flash(
            "Medicine not found.",
            "danger",
        )

        return redirect(
            url_for(
                "medicine.index"
            )
        )

    try:

        MedicineService.delete(
            medicine
        )

        flash(
            "Medicine deleted successfully.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for(
            "medicine.index"
        )
    )

