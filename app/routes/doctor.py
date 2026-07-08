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
from app.services.doctor_service import DoctorService

doctor_bp = Blueprint(
    "doctor",
    __name__,
    url_prefix="/doctors",
)


@doctor_bp.route("/")
@login_required
@permission_required("doctor:view")
def index():

    query = request.args.get("q", "").strip()

    if query:
        doctors = DoctorService.search(query)
    else:
        doctors = DoctorService.get_all()

    return render_template(
        "doctors/index.html",
        doctors=doctors,
        query=query,
    )


@doctor_bp.route("/new", methods=["GET"])
@login_required
@permission_required("doctor:create")
def new():

    return render_template(
        "doctors/form.html",
        departments=DoctorService.get_departments(),
    )


@doctor_bp.route("/new", methods=["POST"])
@login_required
@permission_required("doctor:create")
def create():

    try:

        DoctorService.create(

            username=request.form["username"],

            email=request.form["email"],

            password=request.form["password"],

            license_number=request.form["license_number"],

            specialization=request.form["specialization"],

            phone=request.form["phone"],

            qualification=request.form["qualification"],

            experience=int(request.form["experience"]),

            department_id=int(request.form["department_id"]),
        )

        flash(
            "Doctor created successfully.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

        return redirect(
            url_for("doctor.new")
        )

    return redirect(
        url_for("doctor.index")
    )


@doctor_bp.route("/<int:doctor_id>")
@login_required
@permission_required("doctor:view")
def show(doctor_id):

    doctor = DoctorService.get_by_id(doctor_id)

    if doctor is None:

        flash("Doctor not found.", "danger")

        return redirect(
            url_for("doctor.index")
        )

    return render_template(
        "doctors/show.html",
        doctor=doctor,
    )


@doctor_bp.route("/<int:doctor_id>/edit", methods=["GET"])
@login_required
@permission_required("doctor:update")
def edit(doctor_id):

    doctor = DoctorService.get_by_id(doctor_id)

    if doctor is None:

        flash("Doctor not found.", "danger")

        return redirect(url_for("doctor.index"))

    return render_template(
        "doctors/edit.html",
        doctor=doctor,
        departments=DoctorService.get_departments(),
    )


@doctor_bp.route("/<int:doctor_id>/edit", methods=["POST"])
@login_required
@permission_required("doctor:update")
def update(doctor_id):

    doctor = DoctorService.get_by_id(doctor_id)

    if doctor is None:

        flash("Doctor not found.", "danger")

        return redirect(url_for("doctor.index"))

    DoctorService.update(
        doctor=doctor,
        specialization=request.form["specialization"],
        phone=request.form["phone"],
        qualification=request.form["qualification"],
        experience=int(request.form["experience"]),
        department_id=int(request.form["department_id"]),
    )

    flash("Doctor updated successfully.", "success")

    return redirect(
        url_for("doctor.show", doctor_id=doctor.id)
    )



@doctor_bp.route("/<int:doctor_id>/delete", methods=["POST"])
@login_required
@permission_required("doctor:delete")
def delete(doctor_id):

    doctor = DoctorService.get_by_id(doctor_id)

    if doctor is None:

        flash("Doctor not found.", "danger")

        return redirect(
            url_for("doctor.index")
        )

    DoctorService.delete(doctor)

    flash(
        "Doctor deleted successfully.",
        "success",
    )

    return redirect(
        url_for("doctor.index")
    )

