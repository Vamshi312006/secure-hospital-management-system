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

from app.services.prescription_service import (
    PrescriptionService,
)

from app.validators import (
    PrescriptionValidator,
    ValidationError,
)


prescription_bp = Blueprint(
    "prescription",
    __name__,
    url_prefix="/prescriptions",
)


@prescription_bp.route("/")
@login_required
@permission_required("prescription:view")
def index():

    query = request.args.get(
        "q",
        "",
    ).strip()

    if query:
        prescriptions = (
            PrescriptionService.search(
                query
            )
        )
    else:
        prescriptions = (
            PrescriptionService.get_all()
        )

    return render_template(
        "prescriptions/index.html",
        prescriptions=prescriptions,
        query=query,
    )


@prescription_bp.route(
    "/<int:prescription_id>"
)
@login_required
@permission_required("prescription:view")
def view(
    prescription_id,
):

    prescription = (
        PrescriptionService.get_by_id(
            prescription_id
        )
    )

    if prescription is None:

        flash(
            "Prescription not found.",
            "danger",
        )

        return redirect(
            url_for(
                "prescription.index"
            )
        )

    return render_template(
        "prescriptions/view.html",
        prescription=prescription,
    )


@prescription_bp.route(
    "/new",
    methods=["GET"],
)
@login_required
@permission_required("prescription:create")
def new():

    return render_template(
        "prescriptions/form.html",
        patients=PrescriptionService.get_patients(),
        doctors=PrescriptionService.get_doctors(),
        records=PrescriptionService.get_records(),
        medicines=PrescriptionService.get_medicines(),
        prescription=None,
        edit_mode=False,
    )


@prescription_bp.route(
    "/new",
    methods=["POST"],
)
@login_required
@permission_required("prescription:create")
def create():

    try:

        data = PrescriptionValidator.validate_create(
            request.form
        )

        items = []

        medicine_ids = request.form.getlist(
            "medicine_id"
        )

        quantities = request.form.getlist(
            "quantity"
        )

        mornings = request.form.getlist(
            "morning"
        )

        afternoons = request.form.getlist(
            "afternoon"
        )

        nights = request.form.getlist(
            "night"
        )

        days_list = request.form.getlist(
            "days"
        )

        notes = request.form.getlist(
            "notes"
        )

        for index, medicine_id in enumerate(
            medicine_ids
        ):

            items.append(
                {
                    "medicine_id": int(medicine_id),
                    "quantity": quantities[index],
                    "morning": str(index) in mornings,
                    "afternoon": str(index) in afternoons,
                    "night": str(index) in nights,
                    "days": int(days_list[index]),
                    "notes": notes[index],
                }
            )

        PrescriptionService.create(
            patient_id=data["patient_id"],
            doctor_id=data["doctor_id"],
            record_id=data["record_id"],
            instructions=data["instructions"],
            items=items,
        )

        flash(
            "Prescription created successfully.",
            "success",
        )

        return redirect(
            url_for(
                "prescription.index"
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
                "prescription.new"
            )
        )


@prescription_bp.route(
    "/<int:prescription_id>/edit",
    methods=["GET"],
)
@login_required
@permission_required("prescription:update")
def edit(
    prescription_id,
):

    prescription = PrescriptionService.get_by_id(
        prescription_id
    )

    if prescription is None:

        flash(
            "Prescription not found.",
            "danger",
        )

        return redirect(
            url_for("prescription.index")
        )

    return render_template(
        "prescriptions/form.html",
        prescription=prescription,
        patients=PrescriptionService.get_patients(),
        doctors=PrescriptionService.get_doctors(),
        records=PrescriptionService.get_records(),
        medicines=PrescriptionService.get_medicines(),
        edit_mode=True,
    )


@prescription_bp.route(
    "/<int:prescription_id>/edit",
    methods=["POST"],
)
@login_required
@permission_required("prescription:update")
def update(
    prescription_id,
):

    prescription = PrescriptionService.get_by_id(
        prescription_id
    )

    if prescription is None:

        flash(
            "Prescription not found.",
            "danger",
        )

        return redirect(
            url_for("prescription.index")
        )

    try:

        data = PrescriptionValidator.validate_update(
            request.form
        )

        medicine_ids = request.form.getlist(
            "medicine_id"
        )

        quantities = request.form.getlist(
            "quantity"
        )

        mornings = request.form.getlist(
            "morning"
        )

        afternoons = request.form.getlist(
            "afternoon"
        )

        nights = request.form.getlist(
            "night"
        )

        days_list = request.form.getlist(
            "days"
        )

        notes = request.form.getlist(
            "notes"
        )

        items = []

        for index, medicine_id in enumerate(
            medicine_ids
        ):

            items.append(
                {
                    "medicine_id": int(medicine_id),
                    "quantity": quantities[index],
                    "morning": str(index) in mornings,
                    "afternoon": str(index) in afternoons,
                    "night": str(index) in nights,
                    "days": int(days_list[index]),
                    "notes": notes[index],
                }
            )

        PrescriptionService.update(
            prescription,
            patient_id=data["patient_id"],
            doctor_id=data["doctor_id"],
            record_id=data["record_id"],
            instructions=data["instructions"],
            items=items,
        )

        flash(
            "Prescription updated successfully.",
            "success",
        )

        return redirect(
            url_for(
                "prescription.view",
                prescription_id=prescription.id,
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
                "prescription.edit",
                prescription_id=prescription.id,
            )
        )


@prescription_bp.route(
    "/<int:prescription_id>/delete",
    methods=["POST"],
)
@login_required
@permission_required("prescription:delete")
def delete(
    prescription_id,
):

    prescription = PrescriptionService.get_by_id(
        prescription_id
    )

    if prescription is None:

        flash(
            "Prescription not found.",
            "danger",
        )

        return redirect(
            url_for("prescription.index")
        )

    try:

        PrescriptionService.delete(
            prescription
        )

        flash(
            "Prescription deleted successfully.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for("prescription.index")
    )

