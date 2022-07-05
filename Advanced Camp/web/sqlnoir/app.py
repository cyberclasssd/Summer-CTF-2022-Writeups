#CyberClass CTF, SQL Injection Challenge
#Modified version of https://gist.github.com/hackeris/fa2bfd20e6bec08c8d5240efe87d4687

import os
import sqlite3

from flask import Flask
from flask import redirect
from flask import request
from flask import session
from jinja2 import Template

app = Flask(__name__)

app.secret_key = 'doneky! bonk snoc donk UNUSABLE PITA??'

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database.db')


def connect_db():
    return sqlite3.connect(DATABASE_PATH)


def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(32),
            password VARCHAR(32)
            )''')
    conn.commit()
    conn.close()


def init_data():
    users = [
        ('admin', '21937812739812738921128731237123892137982173892179'),
    ]
    conn = connect_db()
    cur = conn.cursor()
    cur.executemany('INSERT INTO `user` VALUES(NULL,?,?)', users)
    conn.commit()
    conn.close()


def init():
    create_tables()
    init_data()


def get_user_from_username_and_password(username, password):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT id, username FROM `user` WHERE username=\'%s\' AND password=\'%s\'' % (username, password))
    row = cur.fetchone()
    conn.commit()
    conn.close()

    return {'id': row[0], 'username': row[1]} if row is not None else None


def get_user_from_id(uid):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT id, username FROM `user` WHERE id=%d' % uid)
    row = cur.fetchone()
    conn.commit()
    conn.close()

    return {'id': row[0], 'username': row[1]}



def render_login_page():
    return '''
<h1> Nothing to see here ;) </h1>
<form method="POST" style="margin: 60px auto; width: 140px;">
    <p><input name="username" type="text"/></p>
    <p><input name="password" type="password"/></p>
    <p><input value="Login" type="submit"/></p>
</form>
    '''


def render_home_page(uid):
    user = get_user_from_id(uid)
    template = Template('''
<div style="width: 400px; margin: 80px auto; ">
    <h4>I am: {{ user['username'] }}</h4>
    <h1 style="color: #FF0000;">flag{h0w_r_u_so_c00l}</h1>
</div>
    ''')
    return template.render(user=user)


@app.route('/')
def index():
    if 'uid' in session:
        return render_home_page(session['uid'])
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_login_page()
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if '\'' in password:
            return redirect('/error')
        user = get_user_from_username_and_password(username, password)
        if user is not None:
            session['uid'] = user['id']
            return redirect('/')
        else:
            return redirect('/login')


@app.route('/logout')
def logout():
    if 'uid' in session:
        session.pop('uid')
    return redirect('/login')

@app.route('/error')
def error():
    return "<h1> ERROR! Login included <code style=\"Color: red\">'</code> in password. </h1>\n</h2> GO AWAYYYYYYYYYYYYYYYYYY</h2>"

init()

if __name__ == "__main__":
    app.run()
