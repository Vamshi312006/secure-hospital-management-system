# ==========================================================
# Imports
# ==========================================================

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

from app.services.record_service import RecordService


# ==========================================================
# Blueprint
# ==========================================================

record_bp = Blueprint(
    "record",
    __name__,
    url_prefix="/records",
)


# ==========================================================
# List Records
# ==========================================================

@record_bp.route("/")
@login_required
@permission_required("record:view")
def index():

    query = request.args.get(
        "q",
        "",
    ).strip()

    if query:

        records = RecordService.search(
            query
        )

    else:

        records = RecordService.get_all()

    return render_template(
        "records/index.html",
        records=records,
        query=query,
    )


# ==========================================================
# Create Record
# ==========================================================

@record_bp.route("/new", methods=["GET"])
@login_required
@permission_required("record:create")
def new():

    return render_template(
        "records/form.html",
        patients=RecordService.get_patients(),
        doctors=RecordService.get_doctors(),
    )


@record_bp.route("/new", methods=["POST"])
@login_required
@permission_required("record:create")
def create():

    try:

        RecordService.create(

            patient_id=int(
                request.form["patient_id"]
            ),

            doctor_id=int(
                request.form["doctor_id"]
            ),

            diagnosis=request.form[
                "diagnosis"
            ],

            symptoms=request.form[
                "symptoms"
            ],

            treatment=request.form[
                "treatment"
            ],

            notes=request.form[
                "notes"
            ],
        )

        flash(
            "Medical record created successfully.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

        return redirect(
            url_for("record.new")
        )

    return redirect(
        url_for("record.index")
    )


# ==========================================================
# View Record
# ==========================================================

@record_bp.route("/<int:record_id>")
@login_required
@permission_required("record:view")
def view(record_id):

    record = RecordService.get_by_id(
        record_id
    )

    if record is None:

        flash(
            "Medical record not found.",
            "danger",
        )

        return redirect(
            url_for("record.index")
        )

    return render_template(
        "records/view.html",
        record=record,
    )


# ==========================================================
# Edit Record
# ==========================================================

@record_bp.route("/<int:record_id>/edit", methods=["GET"])
@login_required
@permission_required("record:update")
def edit(record_id):

    record = RecordService.get_by_id(
        record_id
    )

    if record is None:

        flash(
            "Medical record not found.",
            "danger",
        )

        return redirect(
            url_for("record.index")
        )

    return render_template(
        "records/form.html",
        record=record,
        patients=RecordService.get_patients(),
        doctors=RecordService.get_doctors(),
        edit_mode=True,
    )


@record_bp.route("/<int:record_id>/edit", methods=["POST"])
@login_required
@permission_required("record:update")
def update(record_id):

    record = RecordService.get_by_id(
        record_id
    )

    if record is None:

        flash(
            "Medical record not found.",
            "danger",
        )

        return redirect(
            url_for("record.index")
        )

    try:

        RecordService.update(

            record=record,

            patient_id=int(
                request.form["patient_id"]
            ),

            doctor_id=int(
                request.form["doctor_id"]
            ),

            diagnosis=request.form[
                "diagnosis"
            ],

            symptoms=request.form[
                "symptoms"
            ],

            treatment=request.form[
                "treatment"
            ],

            notes=request.form[
                "notes"
            ],
        )

        flash(
            "Medical record updated successfully.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

        return redirect(
            url_for(
                "record.edit",
                record_id=record.id,
            )
        )

    return redirect(
        url_for("record.index")
    )


# ==========================================================
# Delete Record
# ==========================================================

@record_bp.route("/<int:record_id>/delete", methods=["POST"])
@login_required
@permission_required("record:delete")
def delete(record_id):

    record = RecordService.get_by_id(
        record_id
    )

    if record is None:

        flash(
            "Medical record not found.",
            "danger",
        )

        return redirect(
            url_for("record.index")
        )

    RecordService.delete(
        record
    )

    flash(
        "Medical record deleted successfully.",
        "success",
    )

    return redirect(
        url_for("record.index")
    )

