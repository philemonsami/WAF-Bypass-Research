import os
import sqlite3
import urllib.request
from flask import Flask, request, render_template_string, jsonify, render_template

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    cursor.execute('''INSERT INTO users (username, password) VALUES ('admin', 'supersecret')''')
    cursor.execute('''INSERT INTO users (username, password) VALUES ('testuser', 'testpass')''')
    conn.commit()
    return conn

db_conn = init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sqli', methods=['GET', 'POST'])
def sqli():
    username = request.args.get('username') or request.form.get('username')
    if not username:
        return "Missing username", 400
    query = f"SELECT * FROM users WHERE username = '{username}'"
    try:
        cursor = db_conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify({"query": query, "result": result})
    except Exception as e:
        return str(e), 500

@app.route('/xss', methods=['GET', 'POST'])
def xss():
    name = request.args.get('name') or request.form.get('name', 'Guest')
    template = f"<h2>Hello, {name}!</h2>"
    return render_template_string(template)

@app.route('/cmd', methods=['GET', 'POST'])
def cmd():
    ip = request.args.get('ip') or request.form.get('ip')
    if not ip:
        return "Missing ip", 400
    cmd_str = f"ping -c 1 {ip}" if os.name != 'nt' else f"ping -n 1 {ip}"
    try:
        output = os.popen(cmd_str).read()
        return f"<pre>{output}</pre>"
    except Exception as e:
        return str(e), 500

@app.route('/lfi', methods=['GET'])
def lfi():
    filename = request.args.get('file')
    if not filename:
        return "Missing file", 400
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except Exception as e:
        return str(e), 500

@app.route('/ssrf', methods=['GET'])
def ssrf():
    url = request.args.get('url')
    if not url:
        return "Missing url", 400
    try:
        with urllib.request.urlopen(url) as response:
            return response.read()
    except Exception as e:
        return str(e), 500

@app.route('/eval', methods=['GET', 'POST'])
def eval_inject():
    calc = request.args.get('calc') or request.form.get('calc')
    if not calc:
        return "Missing calc", 400
    try:
        result = eval(calc)
        return f"Result: {result}"
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)