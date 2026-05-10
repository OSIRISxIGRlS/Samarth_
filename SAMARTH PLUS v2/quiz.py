# ==============================
# 📝 SAMARTH INTERACTIVE QUIZ SYSTEM
# Supportive AI Mentor for Academic Results & Talent Hunting
# ==============================

def generate_quiz(subject, num_questions=5):
    """
    Generate interactive quiz questions based on subject
    """
    quizzes = {
        "Mathematics": [
            {"q": "What is the value of π (pi) approximately?", "a": "3.14", "options": ["2.71", "3.14", "3.41", "2.14"]},
            {"q": "Solve: 2x + 5 = 15", "a": "5", "options": ["5", "10", "7", "15"]},
            {"q": "What is the square root of 144?", "a": "12", "options": ["10", "12", "14", "16"]},
            {"q": "What is 15% of 200?", "a": "30", "options": ["20", "25", "30", "35"]},
            {"q": "What is the formula for area of circle?", "a": "πr²", "options": ["2πr", "πr²", "πd", "4πr"]}
        ],
        "Physics": [
            {"q": "What is the unit of Force?", "a": "Newton", "options": ["Joule", "Newton", "Watt", "Pascal"]},
            {"q": "What is the speed of light?", "a": "3 × 10^8 m/s", "options": ["3 × 10^6", "3 × 10^8", "3 × 10^10", "299 km/s"]},
            {"q": "Newton's First Law is also known as?", "a": "Law of Inertia", "options": ["Law of Inertia", "Law of Gravity", "Law of Action", "Law of Momentum"]},
        ],
        "Chemistry": [
            {"q": "What is the atomic number of Carbon?", "a": "6", "options": ["6", "8", "12", "14"]},
            {"q": "What is the chemical formula of Water?", "a": "H2O", "options": ["H2O", "CO2", "NaCl", "O2"]},
            {"q": "pH value of pure water is?", "a": "7", "options": ["0", "7", "14", "1"]},
        ],
        "English": [
            {"q": "What is the antonym of 'Happy'?", "a": "Sad", "options": ["Joyful", "Sad", "Excited", "Angry"]},
            {"q": "Choose the correct spelling:", "a": "Accommodation", "options": ["Accomodation", "Accommodation", "Acommodation", "Accomadation"]},
        ],
        "AI/ML": [
            {"q": "What does AI stand for?", "a": "Artificial Intelligence", "options": ["Automated Input", "Artificial Intelligence", "Advanced Internet", "Automated Interaction"]},
            {"q": "Which is a type of Machine Learning?", "a": "Supervised Learning", "options": ["Supervised Learning", "Unsupervised Cooking", "Random Learning", "Manual Learning"]},
        ]
    }

    # Default questions if subject not found
    default_questions = [
        {"q": "What is your current class?", "a": "10th/11th/12th", "options": ["9th", "10th", "11th", "12th"]},
        {"q": "How many hours do you study daily?", "a": "4-6 hours", "options": ["1-2", "2-4", "4-6", "6+"]},
    ]

    subject = subject.strip().title() if subject else "General"

    if subject in quizzes:
        questions = quizzes[subject][:num_questions]
    else:
        questions = default_questions

    return {
        "subject": subject,
        "total_questions": len(questions),
        "questions": questions,
        "message": f"🎯 {subject} Quiz Ready! Answer all questions carefully."
    }


def evaluate_quiz(answers, correct_answers):
    """
    Evaluate quiz and return score with feedback
    """
    score = 0
    total = len(correct_answers)
    feedback = []

    for i, ans in enumerate(answers):
        if str(ans).strip().lower() == str(correct_answers[i]).strip().lower():
            score += 1
            feedback.append("✅ Correct")
        else:
            feedback.append("❌ Incorrect")

    percentage = round((score / total) * 100, 2)

    if percentage >= 80:
        remark = "Excellent! Outstanding Performance 🔥"
    elif percentage >= 60:
        remark = "Good Job! Keep Improving 💪"
    else:
        remark = "Needs more practice. Don't give up! 📚"

    return {
        "score": score,
        "total": total,
        "percentage": percentage,
        "remark": remark,
        "feedback": feedback
    }