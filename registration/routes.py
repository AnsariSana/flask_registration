from registration import app
from flask import render_template, request, flash
from registration.forms import RegisterForm
import sqlite3
import os


@app.route('/', methods=['POST','GET'])
@app.route('/register', methods=['POST','GET'])
def register():
    form = RegisterForm()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database.db")

    if request.method == "POST":
        try:
            print(request.form['username'])
            username = request.form['username']
            password = request.form['password']
            again_password = request.form['again_password']

            if not username or not password or not again_password:
                flash("Please fill all the fields","error")
                return render_template("registration.html", name="Register", form=form)
            with sqlite3.connect(db_path) as con:  
                    cur = con.cursor()  
                    current_user = cur.execute("SELECT username FROM User WHERE username = (?)",(username,))

                    user_exist = cur.fetchall()

                    if user_exist:
                        flash("User already exist","error")

                    elif password != again_password:
                        
                        flash("Please enter same password","error")

                    else:

                        cur.execute("INSERT into User(username, password) values (?,?)",(username,password,))  
                        con.commit()  
                        flash("Employee successfully Added")
                    
        except Exception as e:
            print(e)
            flash("Something went wrong please try later","error")
        con.close()  
    return render_template("registration.html", name="Register", form=form)