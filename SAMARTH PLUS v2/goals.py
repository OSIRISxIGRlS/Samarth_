# ==============================
# 🎯 SAMARTH GOALS & MOTIVATION SYSTEM
# Supportive AI Mentor for Academic Results & Talent Hunting
# ==============================

from datetime import datetime, timedelta

def get_motivation(username):
    """
    Returns personalized motivational message based on user activity
    """
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is the sum of small efforts repeated day in and day out.",
        "Your future is created by what you do today, not tomorrow.",
        "Every champion was once a beginner who refused to give up.",
        "Talent wins games, but teamwork and intelligence win championships.",
        "The harder you work for something, the greater you'll feel when you achieve it.",
        "Dreams don't work unless you do."
    ]
    
    return {
        "message": "You're doing great! Keep pushing forward.",
        "quote": quotes[hash(username) % len(quotes)],
        "tip": "Set small achievable goals daily. Consistency is the key to mastery."
    }


def create_goal(username, title, target_score, deadline_days=30):
    """
    Helper function to create a new academic goal
    """
    deadline = datetime.now().date() + timedelta(days=deadline_days)
    
    return {
        "username": username,
        "title": title,
        "target_score": target_score,
        "deadline": deadline,
        "status": "In Progress",
        "created_at": datetime.now()
    }


def get_goal_suggestions():
    """
    Smart goal suggestions based on common student needs
    """
    return [
        {
            "title": "Score 90+ in Mathematics",
            "target": 90,
            "category": "Academics"
        },
        {
            "title": "Complete Physics Chapter 5 & 6",
            "target": 85,
            "category": "Syllabus Completion"
        },
        {
            "title": "Improve English Essay Writing",
            "target": 88,
            "category": "Skill Development"
        },
        {
            "title": "Maintain 7-Day Study Streak",
            "target": 100,
            "category": "Consistency"
        }
    ]