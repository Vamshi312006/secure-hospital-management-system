from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.routes.auth import login_required
from app.services.patient_service import PatientService

patient_bp = Blueprint(
    "patient",
    __name__,
    url_prefix="/patients",
)


@patient_bp.route("/")
@login_required
def index():

    query = request.args.get("q", "").strip()

    if query:
        patients = PatientService.search(query)
    else:
        patients = PatientService.get_all()

    return render_template(
        "patients/index.html",
        patients=patients,
        query=query,
    )


@patient_bp.route("/new", methods=["GET"])
@login_required
def new():

    return render_template(
        "patients/form.html",
    )


@patient_bp.route("/new", methods=["POST"])
@login_required
def create():

    try:

        PatientService.create(
            username=request.form["username"],
            email=request.form["email"],
            password=request.form["password"],
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            dob=request.form["dob"] or None,
            gender=request.form["gender"],
            blood_group=request.form["blood_group"],
            phone=request.form["phone"],
            address=request.form["address"],
            emergency_contact=request.form["emergency_contact"],
        )

        flash(
            "Patient created successfully.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

        return redirect(
            url_for("patient.new")
        )

    return redirect(
        url_for("patient.index")
    )
