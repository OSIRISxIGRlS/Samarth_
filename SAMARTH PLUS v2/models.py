# ==============================
# 🗄️ SAMARTH DATABASE MODELS
# Supportive AI Mentor for Academic Results & Talent Hunting
# ==============================

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# ====================== USER MODEL ======================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Hashed password
    
    def __repr__(self):
        return f"<User {self.username}>"

# ====================== PREDICTION HISTORY ======================
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    marks = db.Column(db.String(200), nullable=False)      # Stored as string list
    prediction = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<History {self.username} - {self.prediction}%>"

# ====================== GOALS MODEL ======================
class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    target_score = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), default="In Progress")  # In Progress, Completed, Failed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Goal {self.title} - {self.status}>"

# ====================== OPTIONAL: QUIZ SCORES ======================
class QuizScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)