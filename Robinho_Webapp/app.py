from this import d
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# from flask_wtf import wtforms
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError


app = Flask(__name__)
app.secret_key = 'supersecrete_key123'


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:Thom_SZK_127789*@localhost:5432/robinho?options=-c%20search_path=schema_name'
db = SQLAlchemy(app)


class Rob_User(db.Model):
    __table_args__ = {'schema' : 'rob'}
    __tablename__ = "Rob_User"
    User_ID = db.Column(db.INTEGER, primary_key = True)
    User_Acc = db.Column(db.VARCHAR(255), unique = True)
    User_Password = db.Column(db.VARCHAR(255))


@app.route('/')
def select():
    solution = Rob_User.query.all()
    print(solution)
    return 'Nao sei'


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html") 


@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet(): 
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)



