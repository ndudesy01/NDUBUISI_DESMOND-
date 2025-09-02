from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            dob TEXT,
            phone TEXT,
            password TEXT
        )''')

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        dob = request.form['dob']
        phone = request.form['phone']
        password = request.form['password']

        # Validations
        if not re.match("^[a-zA-Z0-9]+$", username):
            flash("Username must be alphanumeric.")
            return render_template("register.html")

        if not re.match("^\+234\d{10}$", phone):
            flash("Phone number must start with +234 and have 10 digits after.")
            return render_template("register.html")

        if not re.search("[@#$%^&+=]", password) or not re.search("[a-zA-Z0-9]", password):
            flash("Password must be alphanumeric and contain at least one special character.")
            return render_template("register.html")

        with sqlite3.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=? OR email=?", (username, email))
            if cur.fetchone():
                flash("User already exists.")
                return render_template("register.html")
            cur.execute("INSERT INTO users (username, email, dob, phone, password) VALUES (?, ?, ?, ?, ?)",
                        (username, email, dob, phone, password))
            conn.commit()
        return render_template("message.html", message="Registration successful!", link=url_for('login'))

    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_input = request.form['login']
        password = request.form['password']

        with sqlite3.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE (username=? OR email=?) AND password=?", (login_input, login_input, password))
            user = cur.fetchone()
            if user:
                return render_template("message.html", message="Login successful!", success=True)
            else:
                flash("Invalid username/email or password.")
                return render_template("login.html")

    return render_template("login.html")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
