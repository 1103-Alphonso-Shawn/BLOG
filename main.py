from flask import Flask, render_template, request, session, redirect, url_for
from database import init_db, get_user, create_user,create_post,get_posts,delete_post

app = Flask(__name__)
app.secret_key = "your_secret_key"


# ---------------- INIT DATABASE ----------------
init_db()


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("home.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user(username, password)

        if user:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Wrong username or password")

    return render_template("login.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            create_user(username, password)
            session["user"] = username
            return redirect(url_for("dashboard"))
        except:
            return render_template("register.html", error="Username already exists")

    return render_template("register.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    posts = get_posts()
    user = session["user"]

    return render_template("dashboard.html", posts=posts, user=user)



# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/create", methods=["POST"])
def create():
    # 1. check login
    if "user" not in session:
        return redirect(url_for("login"))

    # 2. get form data
    title = request.form["title"]
    content = request.form["content"]

    # 3. get logged-in user
    author = session["user"]

    # 4. save to database
    create_post(title, content, author)

    # 5. go back to dashboard
    return redirect(url_for("dashboard"))

@app.route("/delete", methods=["POST"])
def delete_p():

    if "user" not in session:
        return redirect(url_for("login"))

    title = request.form["title"]
    author = session["user"]
    

    delete_post(title,author)

    return redirect(url_for("dashboard"))
# ---------------- VIEW POSTS ----------------

    


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True,port=5001)