from flask import session

from database import get_db


def get_patient_id_for_current_user():
    """
    Return a patient_id corresponding to the currently logged-in user.

    Strategy:
      1) If patients.patient_id == session['user_id'] exists -> use it.
      2) Else try to find a patient record by email matching users.username.
      3) If none found -> return None.
    """

    if "user_id" not in session:
        return None

    user_id = session["user_id"]

    db = get_db()
    cur = db.cursor()

    # Strategy 1
    cur.execute(
        "SELECT patient_id FROM patients WHERE patient_id=%s",
        (user_id,),
    )

    row = cur.fetchone()

    if row:
        return row[0]

    # Strategy 2
    cur.execute(
        "SELECT username FROM users WHERE user_id=%s",
        (user_id,),
    )

    user = cur.fetchone()

    if user:
        username = user[0]

        cur.execute(
            "SELECT patient_id FROM patients WHERE email=%s",
            (username,),
        )

        patient = cur.fetchone()

        if patient:
            return patient[0]

    return None
