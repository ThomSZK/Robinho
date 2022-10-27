from operator import length_hint
from this import d
import bcrypt
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user, user_accessed
from flask_wtf import FlaskForm
from importlib_metadata import method_cache
from pyparsing import StringEnd
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = 'supersecrete_key123'


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:Thom_SZK_127789*@localhost:5432/robinho' #?options=-c%20search_path=schema_name
db = SQLAlchemy(app)


bcrypt = Bcrypt(app)

login_manager  = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(User_ID):
    return Rob_User.query.get(int(User_ID))


class Rob_User(db.Model, UserMixin):
    __table_args__ = {'schema' : 'rob'}
    __tablename__ = "Rob_User"
    User_ID = db.Column(db.INTEGER, primary_key = True, nullable = False)
    User_Acc = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    User_Password = db.Column(db.VARCHAR(255))

    def get_id(self):
        return self.User_ID


class RegisterForm(FlaskForm):
    User_Acc = StringField(validators=[InputRequired(), Length(min=2, max=255)], render_kw={"placeholder" : "Username"})
    
    User_Password = PasswordField(validators=[InputRequired(), Length(min=4, max=255)], render_kw={"placeholder" : "Password"})
    
    submit = SubmitField("Register")

    def validate_username(self, User_Acc):
        existing_user_username = Rob_User.query.filter_by(User_Acc = User_Acc.data).first()

        if existing_user_username:
            raise ValidationError("Usuario ja existente. Por favor escolha outro.")
            

class LoginForm(FlaskForm):
    User_Acc = StringField(validators=[InputRequired(), Length(min=2, max=255)], render_kw={"placeholder" : "Username"})
    
    User_Password = PasswordField(validators=[InputRequired(), Length(min=4, max=255)], render_kw={"placeholder" : "Password"})
    
    submit = SubmitField("Login")

def set_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    password_hash = pwhash.decode('utf8')
    return password_hash

@app.route('/')
def select():
    solution = Rob_User.query.all()
    print(solution)
    return 'no idea'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Rob_User.query.filter_by(User_Acc = form.User_Acc.data).first()
        if user:
            if bcrypt.check_password_hash(user.User_Password, form.User_Password.data):
                login_user(user, remember=True)
                return redirect(url_for('dashboard'))
    return render_template("login.html", form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.User_Password.data).decode('utf8')
        new_user = Rob_User(User_Acc = form.User_Acc.data, User_Password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    
    # else:
        #do not add user to database

    return render_template("register.html", form=form) 


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('indexRob.html', user=current_user)


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



