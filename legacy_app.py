from functools import wraps
import os

from flask import Flask, render_template, request, redirect, session, url_for, flash
from database import get_db

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")



def get_patient_id_for_current_user():
    """
    Return a patient_id corresponding to the currently logged-in user.
    Strategy:
      1) If a patients.patient_id == session['user_id'] exists -> use it.
      2) Else try to find a patient record by email matching users.username.
      3) If none found -> return None
    """
    if "user_id" not in session:
        return None

    user_id = session["user_id"]
    db = get_db()
    cur = db.cursor()

    # 1) direct match patient_id == user_id
    cur.execute("SELECT patient_id FROM patients WHERE patient_id=%s", (user_id,))
    row = cur.fetchone()
    if row:
        return row[0]

    # 2) find username/email from users table and match patients.email
    cur.execute("SELECT username FROM users WHERE user_id=%s", (user_id,))
    u = cur.fetchone()
    if u:
        username = u[0]
        cur.execute("SELECT patient_id FROM patients WHERE email=%s", (username,))
        pr = cur.fetchone()
        if pr:
            return pr[0]

    return None


# -------------------- HOME --------------------
@app.route("/", methods=["GET"])
def home():
    """Show login hero BEFORE login, services AFTER login."""
    if "user_id" not in session:
        return render_template("index.html", show_login=True)
    return render_template("index.html")



# -------------------- DASHBOARD --------------------
@app.route("/dashboard")
@login_required
def dashboard():
    # use patient mapping helper to avoid FK issues
    patient_id = get_patient_id_for_current_user()
    if not patient_id:
        flash("No linked patient profile found. Please complete your profile first.")
        return redirect(url_for("patient_profile"))

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM appointments WHERE patient_id=%s", (patient_id,))
    appointments = cur.fetchall()

    cur.execute("SELECT * FROM billing WHERE patient_id=%s", (patient_id,))
    bills = cur.fetchall()

    cur.execute(
        "SELECT prescription_id, prescription_date, notes FROM prescriptions WHERE patient_id=%s",
        (patient_id,)
    )
    prescriptions = cur.fetchall()

    return render_template(
        "dashboard.html",
        appointments=appointments,
        bills=bills,
        prescriptions=prescriptions
    )


# -------------------- FIXED /index ROUTE --------------------
@app.route("/index")
def index():
    return redirect(url_for("home"))


# -------------------- BOOK APPOINTMENT --------------------
@app.route("/book", methods=["GET", "POST"])
@login_required
def book():
    db = get_db()
    cur = db.cursor()

    if request.method == "POST":
        # find patient_id safely
        patient_id = get_patient_id_for_current_user()
        if not patient_id:
            flash("No patient profile found for this account. Update profile first.")
            return redirect(url_for("patient_profile"))

        doctor_id = request.form.get("doctor_id")
        date = request.form.get("date")
        time = request.form.get("time")

        if not doctor_id or not date:
            flash("Select a doctor and date.")
            return redirect(url_for("book"))

        try:
            cur.execute(
                """INSERT INTO appointments
                   (patient_id, doctor_id, appointment_date, appointment_time, status)
                   VALUES (%s, %s, %s, %s, 'Booked')""",
                (patient_id, doctor_id, date, time)
            )
            db.commit()
        except Exception as e:
            db.rollback()
            flash("Failed to book appointment. Please try again.")
            return redirect(url_for("book"))

        flash("Appointment booked successfully.")
        return redirect(url_for("track"))

    cur.execute("SELECT doctor_id, name, specialization FROM doctors")
    doctors = cur.fetchall()
    return render_template("book.html", doctors=doctors)


## -------------------- RESCHEDULE APPOINTMENT --------------------
@app.route("/reschedule", methods=["GET", "POST"])
@login_required
def reschedule():
    db = get_db()
    cur = db.cursor()

    # session user_id == patient_id
    patient_id = session["user_id"]

    if request.method == "POST":
        appointment_id = request.form.get("appointment_id")
        new_date = request.form.get("date")
        new_time = request.form.get("time")

        if not appointment_id or not new_date:
            flash("Missing data.")
            return redirect(url_for("reschedule"))

        # Verify appointment belongs to the logged-in patient
        cur.execute(
            "SELECT appointment_id FROM appointments WHERE appointment_id=%s AND patient_id=%s",
            (appointment_id, patient_id)
        )
        if not cur.fetchone():
            flash("Invalid appointment.")
            return redirect(url_for("reschedule"))

        cur.execute(
            "UPDATE appointments SET appointment_date=%s, appointment_time=%s WHERE appointment_id=%s",
            (new_date, new_time, appointment_id)
        )
        db.commit()

        flash("Appointment rescheduled successfully.")
        return redirect(url_for("track"))

    # Load appointments for this patient
    cur.execute(
        """SELECT a.appointment_id, d.name, a.appointment_date,
                  a.appointment_time, a.status
           FROM appointments a
           JOIN doctors d ON a.doctor_id=d.doctor_id
           WHERE a.patient_id=%s""",
        (patient_id,)
    )
    appointments = cur.fetchall()

    return render_template("reschedule.html", appointments=appointments)



# -------------------- TRACK APPOINTMENTS --------------------
@app.route("/track")
@login_required
def track():
    patient_id = get_patient_id_for_current_user()
    if not patient_id:
        flash("No patient profile found for this account. Update profile first.")
        return redirect(url_for("patient_profile"))

    db = get_db()
    cur = db.cursor()

    cur.execute(
        """SELECT a.appointment_id, d.name, a.appointment_date, a.appointment_time, a.status
           FROM appointments a
           JOIN doctors d ON a.doctor_id=d.doctor_id
           WHERE a.patient_id=%s""",
        (patient_id,)
    )
    appointments = cur.fetchall()

    return render_template("track.html", appointments=appointments)


# -------------------- DOCTOR PROFILES --------------------
@app.route("/doctors")
def doctors():
    db = get_db()
    cur = db.cursor()
    q = request.args.get("q")

    if q:
        cur.execute("SELECT * FROM doctors WHERE name LIKE %s OR specialization LIKE %s",
                    (f"%{q}%", f"%{q}%"))
    else:
        cur.execute("SELECT * FROM doctors")

    doctors = cur.fetchall()
    return render_template("profiles.html", doctors=doctors)


# -------------------- MEDICAL RECORDS --------------------
@app.route("/records")
@login_required
def records():
    patient_id = get_patient_id_for_current_user()
    if not patient_id:
        flash("No patient profile found for this account. Update profile first.")
        return redirect(url_for("patient_profile"))

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM medical_records WHERE patient_id=%s", (patient_id,))
    records = cur.fetchall()

    return render_template("records.html", records=records)


# -------------------- MEDICINES --------------------
@app.route("/medicines")
def medicines():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM medicines")
    meds = cur.fetchall()
    return render_template("medicine.html", medicines=meds)


# -------------------- PRESCRIPTIONS --------------------
@app.route("/prescriptions")
@login_required
def prescriptions():
    patient_id = get_patient_id_for_current_user()
    if not patient_id:
        flash("No patient profile found for this account. Update profile first.")
        return redirect(url_for("patient_profile"))

    db = get_db()
    cur = db.cursor()

    cur.execute(
        """SELECT p.prescription_id, p.prescription_date, d.name, p.notes
           FROM prescriptions p
           JOIN doctors d ON p.doctor_id=d.doctor_id
           WHERE p.patient_id=%s""",
        (patient_id,)
    )
    data = cur.fetchall()

    return render_template("prescription.html", prescriptions=data)


# -------------------- BILLING --------------------
@app.route("/billing")
@login_required
def billing():
    patient_id = get_patient_id_for_current_user()
    if not patient_id:
        flash("No patient profile found for this account. Update profile first.")
        return redirect(url_for("patient_profile"))

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM billing WHERE patient_id=%s", (patient_id,))
    bills = cur.fetchall()

    return render_template("billing.html", bills=bills)


# -------------------- ADMISSIONS --------------------
@app.route("/admissions")
@login_required
def admissions():
    patient_id = get_patient_id_for_current_user()
    if not patient_id:
        flash("No patient profile found for this account. Update profile first.")
        return redirect(url_for("patient_profile"))

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM admissions WHERE patient_id=%s", (patient_id,))
    admissions = cur.fetchall()

    return render_template("admissions.html", admissions=admissions)


# -------------------- ROOMS --------------------
@app.route("/rooms")
def rooms():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM rooms")
    rooms = cur.fetchall()
    return render_template("rooms.html", rooms=rooms)


# -------------------- INSURANCE --------------------
@app.route("/insurance")
@login_required
def insurance():
    patient_id = get_patient_id_for_current_user()
    if not patient_id:
        flash("No patient profile found for this account. Update profile first.")
        return redirect(url_for("patient_profile"))

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM insurance WHERE patient_id=%s", (patient_id,))
    ins = cur.fetchall()

    return render_template("insurance.html", insurance=ins)


# -------------------- STAFF --------------------
@app.route("/staff")
def staff():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM staff")
    staff = cur.fetchall()
    return render_template("staff.html", staff=staff)


# -------------------- PATIENT PROFILE --------------------
@app.route("/patient", methods=["GET", "POST"])
@login_required
def patient_profile():
    user_id = session["user_id"]
    db = get_db()
    cur = db.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")

        cur.execute("""
            UPDATE patients
            SET name=%s, phone=%s, email=%s, address=%s
            WHERE patient_id=%s
        """, (name, phone, email, address, user_id))

        db.commit()
        flash("Profile updated successfully.")
        return redirect(url_for("patient_profile"))

    cur.execute("SELECT * FROM patients WHERE patient_id=%s", (user_id,))
    patient = cur.fetchone()

    return render_template("patient.html", patient=patient)


# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app.run(
        host=os.environ.get("FLASK_RUN_HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG", "0") == "1",
    )
