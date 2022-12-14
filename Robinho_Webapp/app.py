#!/usr/bin/env python3
from crypt import methods
from email.policy import default
from operator import length_hint
from this import d
import bcrypt
import flask
from flask import Flask, render_template, request, flash, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user, user_accessed
from flask_wtf import FlaskForm
from importlib_metadata import method_cache
from pyparsing import StringEnd
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import urllib
# from werkzeug import secure_filename
#from RobinhoImageProcessing import main as img
#from RobinhoImageProcessing.utils import detector, superimpose as si
import cv2
import numpy as np
import serial
import time
# from __future__ import print_function
import sys
import os
import time
import struct
import json
import socket
import random
import threading


USER_QUEUE = []

app = Flask(__name__)
app.secret_key = 'supersecrete_key123'

# password = "Thom_SZK_127789*"
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
        frame = cv2.imread('/home/arena/Documents/GitHub/Robinho/Robinho_Webapp/images/feed.png')
        time.sleep(0.5)
        if frame is not None:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

def readImagemFrom(url):
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    return cv2.imdecode(arr, -1) # 'Load it as it is'

def genPov():  
    #camera = cv2.VideoCapture(-1)
    frames=0
    while True:
        #success, frame = camera.read()  # read the camera frame
        #if not success:
            #break
        #else:
        frames+=1
        frame = cv2.imread('/home/arena/Documents/GitHub/Robinho/Robinho_Webapp/images/pov_feed.png')
        time.sleep(0.3)
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
    user_type = db.Column(db.INTEGER)
    user_current_task = db.Column(db.INTEGER)

    def get_id(self):
        return self.user_id


class Rob_Tasks(db.Model, UserMixin):
    __table_args__ = {'schema' : 'public'}
    __tablename__ = "rob_tasks"
    task_id = db.Column(db.INTEGER, primary_key = True, nullable = False)
    task_name = db.Column(db.VARCHAR(255), nullable = False)
    task_level = db.Column(db.INTEGER, nullable = False)
    task_order = db.Column(db.INTEGER, nullable = False)
    task_description = db.Column(db.VARCHAR(1000))


class Rob_Review_Tasks(db.Model, UserMixin):
    __table_args__ = {'schema' : 'public'}
    __tablename__ = "rob_review_tasks"
    task_id = db.Column(db.INTEGER, primary_key = True, nullable = False)
    user_id = db.Column(db.INTEGER, primary_key = True, nullable = False)
    task_grade = db.Column(db.INTEGER)
    task_reviewed = db.Column(db.BOOLEAN, nullable = False, default = False)
    task_reviewer = db.Column(db.INTEGER)
    task_time = db.Column(db.INTEGER)

class Rob_Queue(db.Model, UserMixin):
    __table_args__ = {'schema' : 'public'}
    __tablename__ = "rob_queue"
    queue_id = db.Column(db.INTEGER, primary_key = True, nullable = False)
    user_id = db.Column(db.INTEGER, nullable = False)
    user_name = db.Column(db.VARCHAR(255), nullable = False)
    task_id = db.Column(db.INTEGER, nullable = False)



# VITUAL QUEUE OR A DB QUEUE WILL BE NEEDED 

class RegisterForm(FlaskForm):
    User_Acc = StringField(validators=[InputRequired(), Length(min=2, max=255)], render_kw={"placeholder" : "Usuario", "class": "form-control form-control-user"})
    
    User_Password = PasswordField(validators=[InputRequired(), Length(min=4, max=255)], render_kw={"placeholder" : "Senha", "class": "form-control form-control-user"})

    User_Type = RadioField(choices=[('1','Professor'),('2','Aluno')], default='2', render_kw={"class": "radio-list"});
    
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
                if user.user_type == 2:
                    return render_template('tarefas-usuario.html', user = Rob_User.query.filter_by(user_id = current_user.get_id()).first(), tasks = Rob_Tasks.query.order_by(Rob_Tasks.task_level, Rob_Tasks.task_order).all())
                elif user.user_type == 1:
                    return redirect(url_for('dashboard'))
    return render_template("login.html", form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required 
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/tarefa_aluno', methods=['GET', 'POST'])
@login_required 
def tarefa_aluno():
    return render_template('tarefas-usuario.html', user = Rob_User.query.filter_by(user_id = current_user.get_id()).first(), tasks = Rob_Tasks.query.order_by(Rob_Tasks.task_level, Rob_Tasks.task_order).all())

@app.route('/tarefa_aluno_bloco', methods=['GET', 'POST'])
@login_required
def tarefa_aluno_bloco():
    task_id = request.args.get('id')
    task = Rob_Tasks.query.get(int(task_id))
    user_task = Rob_User.query.filter_by(user_id = current_user.get_id()).first()
    user_task.user_current_task = task_id
    db.session.commit()

    # user_task = Rob_Review_Tasks.query.filter_by(task_id = task_id, user_id = current_user.get_id()).first()
    # if not user_task:
    #     user_task = Rob_Review_Tasks(task_id = task_id, user_id = current_user.get_id())
    #     db.session.add(user_task)
    #     db.session.commit()

    mypath = "/home/arena/Documents/GitHub/Robinho/Tasks/" + str(user_task.user_current_task) + "/" + str(current_user.user_id) + '.json'
    try:
        with open(mypath, mode="r") as f2:
            jsonc = f2.read()
        blockly = json.loads(jsonc)
    except Exception as e:
        print(e)
        blockly = None

    return render_template('tarefas-usuario-blocos.html', 
      task = task, 
      user = Rob_User.query.filter_by(user_id = current_user.get_id()).first(), 
      blocklyload = blockly
    )


@app.route('/tarefa_professor', methods=['GET', 'POST'])
@login_required
def tarefa_professor():
    # if(current_user.user_id == 6):
    #     return render_template('tarefas-professor.html')
    # else:
    #     return render_template('indexRob.html')
    user_tasks = db.session.query(Rob_Review_Tasks, Rob_Tasks, Rob_User).join(Rob_Tasks, Rob_Tasks.task_id == Rob_Review_Tasks.task_id).join(Rob_User, Rob_User.user_id == Rob_Review_Tasks.user_id).order_by(Rob_Review_Tasks.task_id.desc(), Rob_User.user_acc).all()
    print(user_tasks)
    return render_template('tarefas-professor.html', user_tasks=user_tasks, user = Rob_User.query.filter_by(user_id = current_user.get_id()).first())

@app.route('/tarefa_professor_bloco', methods=['GET', 'POST'])
@login_required
def tarefa_professor_bloco():
    myid = request.args.get('id')
    task_id, user_id = myid.split('-')

    task = db.session.query(Rob_Review_Tasks, Rob_Tasks, Rob_User).join(Rob_Tasks, Rob_Tasks.task_id == Rob_Review_Tasks.task_id).join(Rob_User, Rob_User.user_id == Rob_Review_Tasks.user_id).filter(Rob_Review_Tasks.task_id == int(task_id)).filter(Rob_Review_Tasks.user_id == int(user_id)).first()

    mypath = "/home/arena/Documents/GitHub/Robinho/Tasks/" + str(task.Rob_Tasks.task_id) + "/" + str(task.Rob_Review_Tasks.user_id) + '.json'
    try:
        with open(mypath, mode="r") as f2:
            jsonc = f2.read()
        blockly = json.loads(jsonc)
    except Exception as e:
        print(e)
        blockly = None

    print("tarefa_professor_bloco", blockly)
    
    return render_template('tarefas-professor-blocos.html', 
    task = task, 
    user = Rob_User.query.filter_by(user_id = current_user.get_id()).first(),
    blocklyload = blockly
    )

@app.route('/video_feed')
def video_feed():
    return Response(genFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/pov_feed')
def pov_feed():
    return Response(genPov(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/lista_espera', methods=['GET', 'POST'])
@login_required
def lista_espera():
    queue = db.session.query(Rob_Queue, Rob_Tasks).join(Rob_Tasks, Rob_Tasks.task_id == Rob_Queue.task_id).order_by(Rob_Queue.queue_id).all()
    return render_template('lista-de-espera.html', queue=queue, user = Rob_User.query.filter_by(user_id = current_user.get_id()).first())
 

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.User_Password.data).decode('utf8')
        new_user = Rob_User(user_acc = form.User_Acc.data, user_password = hashed_password, user_type = form.User_Type.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    
    # else:
        #do not add user to database

    return render_template("register.html", form=form) 


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    # if current_user.user_type == 2:
    #     return render_template('tarefas-usuario.html', user = Rob_User.query.filter_by(user_id = current_user.get_id()).first(), tasks = Rob_Tasks.query.order_by(Rob_Tasks.task_level, Rob_Tasks.task_order).all())
    # else: 
    return render_template('indexRob.html', user=current_user)


@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet(): 
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")


prepend = b"""
print("start prepend main")

import machine
import socket
import time
import camera
import robinho_func
from machine import Pin
from machine import UART

time.sleep(1)

flash = Pin(4, Pin.OUT)
robinho_func.blink(1.0, flash)
uart = machine.UART(1, 9600, rx=12, tx=13)
uart.init(9600, bits=8, parity=None, stop=1)
uart.read()

robinho_func.blink(0.1, flash)
robinho_func.arduino_cmd(0b00011011, uart)
robinho_func.arduino_cmd(0x18, uart)
robinho_func.arduino_cmd(0x16, uart)
robinho_func.blink(0.1, flash)

print("end prepend main")

"""

postpend = b"""
print("start postpend main")

robinho_func.blink(1.0, flash)
time.sleep(2)
robinho_func.arduino_cmd(0b00011011, uart)
robinho_func.arduino_cmd(0x18, uart)
robinho_func.arduino_cmd(0x16, uart)
robinho_func.blink(1.0, flash)
print("end postpend main")

"""

GENIUSHOSTPORTS = [("192.168.101.3", 5071)]

def genius_send(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for hostport in GENIUSHOSTPORTS:
        sock.sendto(data, hostport)
    sock.close()

@app.route("/genius", methods = ['POST'])
def genius():
    print('Genius run')
    with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
        command, color = random.choice([(b'r', b"#ff0000")])
        print(command, color)
        ser.write(command)
        for _ in range(100):
            print("sending genius")
            genius_send(color)
            time.sleep(5)

        """
        ser.write(b'g')
        ser.write(b'b')
        ser.write(b'y')
        time.sleep(2)  
        """              
    return "Genius ok"


@app.route("/sendmain", methods = ['POST', 'GET'])
def sendmain():
    # print("Request send blockly:" + repr(request.get_data()))
    print('Iniciando envio de codigo: ')
    user = Rob_Queue.query.first()
    # with open("/tmp/esp_code_tmp.py", mode="wb") as f:
    #     f.write(prepend + request.get_data() + postpend)
    path = "/home/arena/Documents/GitHub/Robinho/Tasks/" + str(user.task_id) + "/" + str(user.user_id) + '.py'
    with open(path, mode="r") as f:
        data = f.read()
        print(data)
    robinho_send(_op, _host, _port, _passwd, path, _dst_file)

    return "Executando"

@app.route("/savemain", methods = ['POST', 'GET'])
def savemain():
    print("Request save py:" + repr(request.get_data("blockly")))
    user_task = Rob_User.query.filter_by(user_id = current_user.get_id()).first()
    mypath = "/home/arena/Documents/GitHub/Robinho/Tasks/" + str(user_task.user_current_task) + "/" + str(current_user.user_id) + '.py'
    os.makedirs(os.path.dirname(mypath), exist_ok=True)
    with open("/home/arena/Documents/GitHub/Robinho/MicroPython/sample.py", mode="wb") as f, open(mypath, mode="w+") as f2:
        print(2)
        f.write(prepend + request.get_data() + postpend)
        print(3)
        f2.write(prepend.decode("utf-8") + request.get_data().decode("utf-8") + postpend.decode("utf-8"))
        print(4)
    # robinho_send(_op, _host, _port, _passwd, "/tmp/esp_code_tmp.py", _dst_file)
    return "Blockly Salvo"    

@app.route("/savemain_blockly", methods = ['POST'])
def savemain_blockly():
    print("Request save blockly:", request.json)
    user_task = Rob_User.query.filter_by(user_id = current_user.get_id()).first()
    mypath = "/home/arena/Documents/GitHub/Robinho/Tasks/" + str(user_task.user_current_task) + "/" + str(current_user.user_id) + '.json'
    os.makedirs(os.path.dirname(mypath), exist_ok=True)
    with open(mypath, mode="w+") as f2:
        f2.write(json.dumps(request.json))
    # robinho_send(_op, _host, _port, _passwd, "/tmp/esp_code_tmp.py", _dst_file)
    return "Blockly json Salvo"   

# TO BE DONE maybe?
# @app.route("/stop", methods = ['POST'])
# def stopping():
#     print(request.get_data())

#     with open("/tmp/esp_code_tmp.py", mode="wb") as f:
#         f.write(prepend + request.get_data() + postpend)

#     robinho_stop(_op, _host, _port, _passwd, "/tmp/esp_code_tmp.py", _dst_file)

#     return "Executando"


@app.route("/savecode", methods=['POST'])
def savecode():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return 'Code saved succesfully'



@app.route("/queue", methods=['POST'])
def queue():
    user = Rob_User.query.filter_by(user_id = current_user.get_id()).first()
    task_id = user.user_current_task
    user_task = Rob_Review_Tasks.query.filter_by(task_id = task_id, user_id = current_user.get_id()).first()
    if not user_task:
        user_task = Rob_Review_Tasks(task_id = task_id, user_id = current_user.get_id())
        db.session.add(user_task)
        db.session.commit()
    user_queue = Rob_Queue.query.filter_by(task_id = task_id, user_id = current_user.get_id()).first()
    if not user_queue:
        user_task = Rob_Queue(task_id = task_id, user_id = current_user.get_id(), user_name = user.user_acc)
        db.session.add(user_task)
        db.session.commit()
    return 'Queued!'


# this function will be handled by the teacher
@app.route("/dequeue", methods=['POST'])
def dequeue():
    user = Rob_Queue.query.first()
    db.session.delete(user)
    db.session.commit()
    return 'Dequeued!'


@app.route("/review", methods=['GET'])
def review():
    task_id = request.args.get('task_id')
    user_id = request.args.get('user_id')
    task_grade = request.args.get('task_grade')

    print('TASK: ' + request.args.get('task_id'))
    print('USER: ' + user_id)
    
    user_task = Rob_Review_Tasks.query.filter_by(task_id = task_id, user_id = user_id).first()
    user_task.task_grade = task_grade
    db.session.commit()
    return 'Reviewed!'


# --------------------------------------------------------------

# Define to 1 to use builtin "uwebsocket" module of MicroPython
USE_BUILTIN_UWEBSOCKET = 0
# Treat this remote directory as a root for file transfers
SANDBOX = ""
#SANDBOX = "/tmp/webrepl/"
DEBUG = 0

WEBREPL_REQ_S = "<2sBBQLH64s"
WEBREPL_PUT_FILE = 1
WEBREPL_GET_FILE = 2
WEBREPL_GET_VER  = 3


def debugmsg(msg):
    if DEBUG:
        print(msg)


if USE_BUILTIN_UWEBSOCKET:
    from uwebsocket import websocket
else:
    class websocket:

        def __init__(self, s):
            self.s = s
            self.buf = b""

        def write(self, data):
            l = len(data)
            if l < 126:
                # TODO: hardcoded "binary" type
                hdr = struct.pack(">BB", 0x82, l)
            else:
                hdr = struct.pack(">BBH", 0x82, 126, l)
            self.s.send(hdr)
            self.s.send(data)

        def recvexactly(self, sz):
            res = b""
            while sz:
                data = self.s.recv(sz)
                if not data:
                    break
                res += data
                sz -= len(data)
            return res

        def read(self, size, text_ok=False):
            if not self.buf:
                while True:
                    hdr = self.recvexactly(2)
                    assert len(hdr) == 2
                    fl, sz = struct.unpack(">BB", hdr)
                    if sz == 126:
                        hdr = self.recvexactly(2)
                        assert len(hdr) == 2
                        (sz,) = struct.unpack(">H", hdr)
                    if fl == 0x82:
                        break
                    if text_ok and fl == 0x81:
                        break
                    debugmsg("Got unexpected websocket record of type %x, skipping it" % fl)
                    while sz:
                        skip = self.s.recv(sz)
                        debugmsg("Skip data: %s" % skip)
                        sz -= len(skip)
                data = self.recvexactly(sz)
                assert len(data) == sz
                self.buf = data

            d = self.buf[:size]
            self.buf = self.buf[size:]
            assert len(d) == size, len(d)
            return d

        def ioctl(self, req, val):
            assert req == 9 and val == 2


def login(ws, passwd):
    while True:
        c = ws.read(1, text_ok=True)
        if c == b":":
            assert ws.read(1, text_ok=True) == b" "
            break
    ws.write(passwd.encode("utf-8") + b"\r")

def read_resp(ws):
    data = ws.read(4)
    sig, code = struct.unpack("<2sH", data)
    assert sig == b"WB"
    return code


def send_req(ws, op, sz=0, fname=b""):
    rec = struct.pack(WEBREPL_REQ_S, b"WA", op, 0, 0, sz, len(fname), fname)
    debugmsg("%r %d" % (rec, len(rec)))
    ws.write(rec)


def get_ver(ws):
    send_req(ws, WEBREPL_GET_VER)
    d = ws.read(3)
    d = struct.unpack("<BBB", d)
    return d


def put_file(ws, local_file, remote_file):
    sz = os.stat(local_file)[6]
    dest_fname = (SANDBOX + remote_file).encode("utf-8")
    rec = struct.pack(WEBREPL_REQ_S, b"WA", WEBREPL_PUT_FILE, 0, 0, sz, len(dest_fname), dest_fname)
    debugmsg("%r %d" % (rec, len(rec)))
    ws.write(rec[:10])
    ws.write(rec[10:])
    assert read_resp(ws) == 0
    cnt = 0
    with open(local_file, "rb") as f:
        while True:
            sys.stdout.write("Sent %d of %d bytes\r" % (cnt, sz))
            sys.stdout.flush()
            buf = f.read(1024)
            if not buf:
                break
            ws.write(buf)
            cnt += len(buf)
    print()
    assert read_resp(ws) == 0

def get_file(ws, local_file, remote_file):
    src_fname = (SANDBOX + remote_file).encode("utf-8")
    rec = struct.pack(WEBREPL_REQ_S, b"WA", WEBREPL_GET_FILE, 0, 0, 0, len(src_fname), src_fname)
    debugmsg("%r %d" % (rec, len(rec)))
    ws.write(rec)
    assert read_resp(ws) == 0
    with open(local_file, "wb") as f:
        cnt = 0
        while True:
            ws.write(b"\0")
            (sz,) = struct.unpack("<H", ws.read(2))
            if sz == 0:
                break
            while sz:
                buf = ws.read(sz)
                if not buf:
                    raise OSError()
                cnt += len(buf)
                f.write(buf)
                sz -= len(buf)
                sys.stdout.write("Received %d bytes\r" % cnt)
                sys.stdout.flush()
    print()
    assert read_resp(ws) == 0


def help(rc=0):
    exename = sys.argv[0].rsplit("/", 1)[-1]
    print("%s - Perform remote file operations using MicroPython WebREPL protocol" % exename)
    print("Arguments:")
    print("  [-p password] <host>:<remote_file> <local_file> - Copy remote file to local file")
    print("  [-p password] <local_file> <host>:<remote_file> - Copy local file to remote file")
    print("Examples:")
    print("  %s script.py 192.168.4.1:/another_name.py" % exename)
    print("  %s script.py 192.168.4.1:/app/" % exename)
    print("  %s -p password 192.168.4.1:/app/script.py ." % exename)
    sys.exit(rc)

def error(msg):
    print(msg)
    sys.exit(1)

def parse_remote(remote):
    host, fname = remote.rsplit(":", 1)
    if fname == "":
        fname = "/"
    port = 8266
    if ":" in host:
        host, port = host.split(":")
        port = int(port)
    return (host, port, fname)


# Very simplified client handshake, works for MicroPython's
# websocket server implementation, but probably not for other
# servers.
def client_handshake(sock):
    cl = sock.makefile("rwb", 0)
    cl.write(b"""\
GET / HTTP/1.1\r
Host: echo.websocket.org\r
Connection: Upgrade\r
Upgrade: websocket\r
Sec-WebSocket-Key: foo\r
\r
""")
    l = cl.readline()
#    print(l)
    while 1:
        l = cl.readline()
        if l == b"\r\n":
            break
#        sys.stdout.write(l)


def robinho_send(op, host, port, passwd, src_file, dst_file):
 
    print("op:%s, host:%s, port:%d, passwd:%s." % (op, host, port, passwd))
    print(src_file, "->", dst_file)

    s = socket.socket()

    print((host, port))
    s.connect((host, port))

    #s = s.makefile("rwb")
    client_handshake(s)

    ws = websocket(s)

    login(ws, passwd)
    print("Remote WebREPL version:", get_ver(ws))

    # Set websocket to send data marked as "binary"
    ws.ioctl(9, 2)

    if op == "get":
        get_file(ws, dst_file, src_file)
    elif op == "put":
        put_file(ws, src_file, dst_file)

    print('Resetting...')
    # ws.write only sends binary data, so we need to instead send the
    # appropriate header for "text" data to send control characters
    text_hdr = struct.pack(">BB", 0x81, 1)
    print("texthdr", text_hdr)
    s.sendall(text_hdr)
    print("sent1")
    s.sendall(b'\x03')  #ctrl-c to interrupt whatever might be happening
    #print("recv", s.recv(1000))
    s.sendall(text_hdr)
    print("sent2")
    s.sendall(b'\x04')  #ctrl-d
    print("sent3")

    s.close()


# TO BE DONE 
def robinho_stop(op, host, port, passwd, src_file, dst_file):
    
    print("op:%s, host:%s, port:%d, passwd:%s." % (op, host, port, passwd))
    print(src_file, "->", dst_file)

    s = socket.socket()

    ai = socket.getaddrinfo(host, port)
    addr = ai[0][4]

    s.connect(addr)

    #s = s.makefile("rwb")
    client_handshake(s)

    ws = websocket(s)

    login(ws, passwd)
    print("Remote WebREPL version:", get_ver(ws))

    # Set websocket to send data marked as "binary"
    ws.ioctl(9, 2)

    if op == "get":
        get_file(ws, dst_file, src_file)
    elif op == "put":
        put_file(ws, src_file, dst_file)

    print('Stopping...')
    # ws.write only sends binary data, so we need to instead send the
    # appropriate header for "text" data to send control characters
    text_hdr = struct.pack(">BB", 0x81, 1)
    print("texthdr", text_hdr)
    s.sendall(text_hdr)
    print("sent1")
    s.sendall(b'\x03')  #ctrl-c to interrupt whatever might be happening
    #print("recv", s.recv(1000))
    s.sendall(text_hdr)
    print("sent2")
    s.close()


_op = "put"
_host = "192.168.101.3"
_port = 8266
_passwd = "robinho"
_src_file = "temp.py"
_dst_file = "main.py"
# robinho_send(_op, _host, _port, _passwd, _src_file, _dst_file)

@app.route("/favicon.ico") # 2 add get for favicon
def fav():
    print(os.path.join(app.root_path, 'static'))
    return flask.send_from_directory(app.static_folder, 'favicon.ico') # for sure return the file

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, ssl_context='adhoc')
