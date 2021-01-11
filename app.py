import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    feedback = list(mongo.db.feedback.find())
    return render_template("home.html", feedback=feedback)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/reviews")
def reviews():
    feedback = list(mongo.db.feedback.find())
    return render_template("reviews.html", feedback=feedback)

@app.route("/contactUs", methods=["GET", "POST"])
def contactUs():
    return render_template("contactUs.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        username = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=username))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    feedback = list(mongo.db.feedback.find())
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username, feedback=feedback)

    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/reviewAdd", methods=["GET", "POST"])
def reviewAdd():
    if request.method == "POST":
        interested = True if request.form.get("interested") else False
        pledged = True if request.form.get("pledged") else False
        comment = {
            "name": request.form.get("name"),
            "surname": request.form.get("surname"),
            "email": request.form.get("email"),
            "interested": interested,
            "pledged": pledged,
            "amount": request.form.get("amount"),
            "review": request.form.get("review"),
            "created_by": session["user"]
        }
        mongo.db.feedback.insert_one(comment)
        flash("Review Successfully Added")
    return render_template("reviewAdd.html")

@app.route("/reviewEdit/<feed_id>", methods=["GET", "POST"])
def reviewEdit(feed_id):
    if request.method == "POST":
        interested = True if request.form.get("interested") else False
        pledged = True if request.form.get("pledged") else False
        submit = {
            "name": request.form.get("name"),
            "surname": request.form.get("surname"),
            "email": request.form.get("email"),
            "interested": interested,
            "pledged": pledged,
            "amount": request.form.get("amount"),
            "review": request.form.get("review"),
            "created_by": session["user"]
        }
        mongo.db.feedback.update({"_id": ObjectId(feed_id)}, submit)
        flash("Review Successfully Updated")
    feed = mongo.db.feedback.find_one({"_id": ObjectId(feed_id)})
    return render_template("reviewEdit.html", feed=feed)

@app.route("/reviewDeleted/<feed_id>")
def reviewDeleted(feed_id):
    mongo.db.feedback.remove({"_id": ObjectId(feed_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)