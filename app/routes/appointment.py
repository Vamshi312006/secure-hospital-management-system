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
from app.services.appointment_service import AppointmentService


# ==========================================================
# Blueprint
# ==========================================================

appointment_bp = Blueprint(
    "appointment",
    __name__,
    url_prefix="/appointments",
)


# ==========================================================
# List Appointments
# ==========================================================

@appointment_bp.route("/")
@login_required
@permission_required("appointment:view")
def index():

    query = request.args.get(
        "q",
        "",
    ).strip()

    if query:

        appointments = AppointmentService.search(
            query
        )

    else:

        appointments = AppointmentService.get_all()

    return render_template(
        "appointments/index.html",
        appointments=appointments,
        query=query,
    )


# ==========================================================
# Create Appointment
# ==========================================================

@appointment_bp.route("/new", methods=["GET"])
@login_required
@permission_required("appointment:create")
def new():

    return render_template(
        "appointments/form.html",
        doctors=AppointmentService.get_doctors(),
        patients=AppointmentService.get_patients(),
    )


@appointment_bp.route("/new", methods=["POST"])
@login_required
@permission_required("appointment:create")
def create():

    try:

        AppointmentService.create(

            patient_id=int(
                request.form["patient_id"]
            ),

            doctor_id=int(
                request.form["doctor_id"]
            ),

            appointment_date=request.form[
                "appointment_date"
            ],

            appointment_time=request.form[
                "appointment_time"
            ],

            status=request.form[
                "status"
            ],

            reason=request.form[
                "reason"
            ],
        )

        flash(
            "Appointment created successfully.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

        return redirect(
            url_for("appointment.new")
        )

    return redirect(
        url_for("appointment.index")
    )


# ==========================================================
# View Appointment
# ==========================================================

@appointment_bp.route("/<int:appointment_id>")
@login_required
@permission_required("appointment:view")
def view(appointment_id):

    appointment = AppointmentService.get_by_id(
        appointment_id
    )

    if appointment is None:

        flash(
            "Appointment not found.",
            "danger",
        )

        return redirect(
            url_for("appointment.index")
        )

    return render_template(
        "appointments/view.html",
        appointment=appointment,
    )


# ==========================================================
# Edit Appointment
# ==========================================================

@appointment_bp.route("/<int:appointment_id>/edit", methods=["GET"])
@login_required
@permission_required("appointment:update")
def edit(appointment_id):

    appointment = AppointmentService.get_by_id(
        appointment_id
    )

    if appointment is None:

        flash(
            "Appointment not found.",
            "danger",
        )

        return redirect(
            url_for("appointment.index")
        )

    return render_template(
        "appointments/form.html",
        appointment=appointment,
        doctors=AppointmentService.get_doctors(),
        patients=AppointmentService.get_patients(),
        edit_mode=True,
    )


@appointment_bp.route("/<int:appointment_id>/edit", methods=["POST"])
@login_required
@permission_required("appointment:update")
def update(appointment_id):

    appointment = AppointmentService.get_by_id(
        appointment_id
    )

    if appointment is None:

        flash(
            "Appointment not found.",
            "danger",
        )

        return redirect(
            url_for("appointment.index")
        )

    try:

        AppointmentService.update(

            appointment=appointment,

            patient_id=int(
                request.form["patient_id"]
            ),

            doctor_id=int(
                request.form["doctor_id"]
            ),

            appointment_date=request.form[
                "appointment_date"
            ],

            appointment_time=request.form[
                "appointment_time"
            ],

            status=request.form[
                "status"
            ],

            reason=request.form[
                "reason"
            ],
        )

        flash(
            "Appointment updated successfully.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

        return redirect(
            url_for(
                "appointment.edit",
                appointment_id=appointment.id,
            )
        )

    return redirect(
        url_for("appointment.index")
    )


# ==========================================================
# Delete Appointment
# ==========================================================

@appointment_bp.route("/<int:appointment_id>/delete", methods=["POST"])
@login_required
@permission_required("appointment:delete")
def delete(appointment_id):

    appointment = AppointmentService.get_by_id(
        appointment_id
    )

    if appointment is None:

        flash(
            "Appointment not found.",
            "danger",
        )

        return redirect(
            url_for("appointment.index")
        )

    AppointmentService.delete(
        appointment
    )

    flash(
        "Appointment deleted successfully.",
        "success",
    )

    return redirect(
        url_for("appointment.index")
    )

