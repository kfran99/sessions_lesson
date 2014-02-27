from flask import Flask, render_template, request, redirect, session, url_for, flash
import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

@app.route("/")
def index():
    if session.get("username"):
        return "User %s is logged in!" %session["username"]
    else:
        return render_template("index.html")

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")

    status = model.authenticate(username, password)
    if status == "SUCCESS":
        flash("User authenticated")
        session['username'] = username
        return redirect(url_for("index"))    
    elif status == "no_user":
        flash("User does not exist")
        return redirect(url_for("index"))
    elif status == "incorrect":
        flash("Username or Password incorrect, there may be a ferret stampede in progress!")
        return redirect(url_for("index"))
    

@app.route("/user/<username>")
def view_user(username):
    model.get_user_by_name("username")
    # show the user profile for that user
    return 'User %s is logged in.' % username

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/clear")
def clear():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
