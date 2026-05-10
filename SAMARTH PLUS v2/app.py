from flask import Flask, render_template, request, redirect, session, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
from config import Config

# Import modules
from models import db, User, History
from ml_model import predict_marks
from smart_timetable import generate_smart_timetable
from utils.graph_generator import generate_graph
from utils.pdf_generator import generate_pdf
from chatbot import ai_chat_response, generate_practice_questions

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Create directories
os.makedirs('instance', exist_ok=True)
os.makedirs('static/images/graphs', exist_ok=True)
os.makedirs('static/pdfs', exist_ok=True)

# Initialize DB
with app.app_context():
    db.create_all()

PROJECT = "SAMARTH"
FULL_FORM = "Supportive AI Mentor for Academic Results & Talent Hunting"

@app.route('/')
def home():
    return render_template('index.html', project=PROJECT, fullform=FULL_FORM)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user'] = user.username
            flash("Welcome back, Future Topper! 🎉", "success")
            return redirect('/dashboard')
        flash("Invalid username or password", "error")
    return render_template('login.html', project=PROJECT)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first():
            flash("Username already taken", "error")
        else:
            hashed_pw = generate_password_hash(request.form['password'])
            new_user = User(username=request.form['username'], password=hashed_pw)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully! Please login.", "success")
            return redirect('/login')
    return render_template('register.html', project=PROJECT)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    
    if request.method == 'POST':
        try:
            marks = [int(request.form.get(f'sub{i}', 0)) for i in range(6)]
            predicted = predict_marks(marks)
            subjects = ["English", "Mathematics", "Chemistry", "Physics", "Arts", "AI/ML"]
            weak_subject = subjects[marks.index(min(marks))]

            graph_path = generate_graph(marks, predicted, session['user'])
            pdf_path = generate_pdf(session['user'], marks, predicted)

            record = History(
                username=session['user'],
                marks=str(marks),
                prediction=predicted
            )
            db.session.add(record)
            db.session.commit()

            return render_template('dashboard.html',
                                   prediction=predicted,
                                   percent=int(predicted),
                                   marks=marks,
                                   weak_subject=weak_subject,
                                   graph=graph_path,
                                   pdf=pdf_path,
                                   project=PROJECT,
                                   fullform=FULL_FORM)
        except Exception as e:
            flash(f"Error processing marks: {str(e)}", "error")

    return render_template('dashboard.html', project=PROJECT, fullform=FULL_FORM)

@app.route('/practice', methods=['GET', 'POST'])
def practice():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        result = generate_practice_questions(
            request.form.get('class_level'),
            request.form.get('chapter'),
            request.form.get('topic')
        )
        return jsonify(result)
    return render_template('practice.html', project=PROJECT, fullform=FULL_FORM)

@app.route('/chatbot')
def chatbot():
    if 'user' not in session:
        return redirect('/login')
    return render_template('chatbot.html', project=PROJECT, fullform=FULL_FORM)

@app.route('/api/chat', methods=['POST'])
def api_chat():
    if 'user' not in session:
        return jsonify({"reply": "Please login first"}), 401
    message = request.json.get('message', '')
    reply = ai_chat_response(message)
    return jsonify({"reply": reply})

@app.route('/logout')
def logout():
    session.clear()
    flash("See you soon! Keep learning! 👋", "info")
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)