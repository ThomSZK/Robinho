from crypt import methods
from operator import length_hint
from this import d
import bcrypt
from django.shortcuts import render
from flask import Flask, render_template, request, flash, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user, user_accessed
from flask_wtf import FlaskForm
from importlib_metadata import method_cache
from pyparsing import StringEnd
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
#from RobinhoImageProcessing import main as img
#from RobinhoImageProcessing.utils import detector, superimpose as si
import cv2
import numpy as np
import time

app = Flask(__name__)
app.secret_key = 'supersecrete_key123'

password = "Thom_SZK_127789*"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:robinho@localhost:5432/robinho' #?options=-c%20search_path=schema_name
db = SQLAlchemy(app)


bcrypt = Bcrypt(app)

login_manager  = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


def genFrames():  
    #camera = cv2.VideoCapture(-1)
    frames=0
    while True:
        #success, frame = camera.read()  # read the camera frame
        #if not success:
            #break
        #else:
        frames+=1
        frame = cv2.imread('./images/feed.png')
        time.sleep(0.5)
        if frame is not None:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@login_manager.user_loader
def load_user(user_id):
    return Rob_User.query.get(int(user_id))


class Rob_User(db.Model, UserMixin):
    __table_args__ = {'schema' : 'public'}
    __tablename__ = "rob_user"
    user_id = db.Column(db.INTEGER, primary_key = True, nullable = False)
    user_acc = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    user_password = db.Column(db.VARCHAR(255))

    def get_id(self):
        return self.user_id


class RegisterForm(FlaskForm):
    User_Acc = StringField(validators=[InputRequired(), Length(min=2, max=255)], render_kw={"placeholder" : "Usuario", "class": "form-control form-control-user"})
    
    User_Password = PasswordField(validators=[InputRequired(), Length(min=4, max=255)], render_kw={"placeholder" : "Senha", "class": "form-control form-control-user"})
    
    submit = SubmitField("Criar conta", render_kw={"class": "btn btn-primary btn-user btn-block"})

    def validate_username(self, User_Acc):
        existing_user_username = Rob_User.query.filter_by(User_Acc = User_Acc.data).first()

        if existing_user_username:
            raise ValidationError("Usuario ja existente. Por favor escolha outro.")
            

class LoginForm(FlaskForm):
    User_Acc = StringField(validators=[InputRequired(), Length(min=2, max=255)], render_kw={"placeholder" : "Usuario", "class": "form-control form-control-user"})
    
    User_Password = PasswordField(validators=[InputRequired(), Length(min=4, max=255)], render_kw={"placeholder" : "Senha", "class": "form-control form-control-user"})
    
    submit = SubmitField("Entrar", render_kw={"class": "btn btn-primary btn-user btn-block"})

def set_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    password_hash = pwhash.decode('utf8')
    return password_hash


@app.route('/')
def select():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Rob_User.query.filter_by(user_acc = form.User_Acc.data).first()
        if user:
            if bcrypt.check_password_hash(user.user_password, form.User_Password.data):
                login_user(user, remember=True)
                return redirect(url_for('dashboard'))
    return render_template("login.html", form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#ARRUMAR LINK -- tarefa usuario --> tarefa usuario blocos 
@app.route('/tarefa_aluno', methods=['GET', 'POST'])
@login_required
def tarefa_aluno():
    return render_template('tarefas-usuario.html')

@app.route('/tarefa_aluno_bloco', methods=['GET', 'POST'])
@login_required
def tarefa_aluno_bloco():
    return render_template('tarefas-usuario-blocos.html')

#Arrumar link -- tarefa professor --> tarefa professor blocos
@app.route('/tarefa_professor', methods=['GET', 'POST'])
@login_required
def tarefa_professor():
    return render_template('tarefas-professor.html')

@app.route('/tarefa_professor_bloco', methods=['GET', 'POST'])
@login_required
def tarefa_professor_bloco():
    return render_template('tarefas-professor-blocos.html')

@app.route('/video_feed')
def video_feed():
    return Response(genFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/lista_espera', methods=['GET', 'POST'])
@login_required
def lista_espera():
    return render_template('lista-de-espera.html')
 

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.User_Password.data).decode('utf8')
        new_user = Rob_User(user_acc = form.User_Acc.data, user_password = hashed_password)
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
    app.run(debug=True, host='192.168.100.253')



