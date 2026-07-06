
# -------------------- Helpers --------------------
def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first.")
            return redirect(url_for("home") + "#login")
        return f(*args, **kwargs)
    return wrapped


# -------------------- LOGIN --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Missing username or password.")
            return redirect(url_for("home") + "#login")

        db = get_db()
        cur = db.cursor()

        cur.execute(
            "SELECT user_id, role FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cur.fetchone()

        if user:
            session["user_id"] = user[0]
            session["role"] = user[1]
            flash("Logged in successfully.")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials.")
            return redirect(url_for("home") + "#login")

    return redirect(url_for("home") + "#login")


# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("You have logged out.")
    return redirect(url_for("home"))
