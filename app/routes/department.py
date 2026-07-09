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

from app.services.department_service import DepartmentService

from app.validators import (
    DepartmentValidator,
    ValidationError,
)


department_bp = Blueprint(
    "department",
    __name__,
    url_prefix="/departments",
)


@department_bp.route("/")
@login_required
@permission_required("department:view")
def index():

    query = request.args.get(
        "q",
        "",
    )

    departments = DepartmentService.get_all(
        query
    )

    return render_template(
        "departments/index.html",
        departments=departments,
        query=query,
    )


@department_bp.route(
    "/new",
    methods=["GET"],
)
@login_required
@permission_required("department:create")
def new():

    return render_template(
        "departments/form.html",
        department=None,
        edit_mode=False,
    )


@department_bp.route(
    "/new",
    methods=["POST"],
)
@login_required
@permission_required("department:create")
def create():

    try:

        data = DepartmentValidator.validate_create(
            request.form
        )

        department = DepartmentService.create(
            data
        )

        flash(
            "Department created successfully.",
            "success",
        )

        return redirect(
            url_for(
                "department.view",
                department_id=department.id,
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
                "department.new"
            )
        )


@department_bp.route(
    "/<int:department_id>",
)
@login_required
@permission_required("department:view")
def view(
    department_id,
):

    department = DepartmentService.get_by_id(
        department_id
    )

    if department is None:

        flash(
            "Department not found.",
            "danger",
        )

        return redirect(
            url_for(
                "department.index"
            )
        )

    return render_template(
        "departments/view.html",
        department=department,
    )


@department_bp.route(
    "/<int:department_id>/edit",
    methods=["GET"],
)
@login_required
@permission_required("department:update")
def edit(
    department_id,
):

    department = DepartmentService.get_by_id(
        department_id
    )

    if department is None:

        flash(
            "Department not found.",
            "danger",
        )

        return redirect(
            url_for(
                "department.index"
            )
        )

    return render_template(
        "departments/form.html",
        department=department,
        edit_mode=True,
    )


@department_bp.route(
    "/<int:department_id>/edit",
    methods=["POST"],
)
@login_required
@permission_required("department:update")
def update(
    department_id,
):

    department = DepartmentService.get_by_id(
        department_id
    )

    if department is None:

        flash(
            "Department not found.",
            "danger",
        )

        return redirect(
            url_for(
                "department.index"
            )
        )

    try:

        data = DepartmentValidator.validate_update(
            request.form
        )

        DepartmentService.update(
            department,
            data,
        )

        flash(
            "Department updated successfully.",
            "success",
        )

        return redirect(
            url_for(
                "department.view",
                department_id=department.id,
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
                "department.edit",
                department_id=department.id,
            )
        )


@department_bp.route(
    "/<int:department_id>/delete",
    methods=["POST"],
)
@login_required
@permission_required("department:delete")
def delete(
    department_id,
):

    department = DepartmentService.get_by_id(
        department_id
    )

    if department is None:

        flash(
            "Department not found.",
            "danger",
        )

        return redirect(
            url_for(
                "department.index"
            )
        )

    try:

        DepartmentService.delete(
            department
        )

        flash(
            "Department deleted successfully.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for(
            "department.index"
        )

    )

