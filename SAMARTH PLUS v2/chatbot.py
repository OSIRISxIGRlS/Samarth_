# ==============================
# 🤖 SAMARTH AI CHATBOT
# Supportive AI Mentor for Academic Results & Talent Hunting
# ==============================

def ai_chat_response(message):
    """
    Intelligent response system for SAMARTH AI Tutor
    """
    message = message.lower().strip()
    
    # Greeting responses
    if any(greet in message for greet in ['hi', 'hello', 'hey', 'namaste']):
        return "Hello! I'm SAMARTH, your AI Study Mentor. How can I help you today? 😊"
    
    # Study related
    if 'study' in message or 'how to study' in message:
        return "Great question! Focus on understanding concepts rather than rote learning. Would you like a personalized study strategy?"
    
    if 'motivation' in message or 'motivate' in message:
        return "You are capable of amazing things! Every topper was once a beginner. Keep going, success is closer than you think! 💪"
    
    if 'weak' in message or 'improve' in message:
        return "Don't worry! Identify your weak subjects and practice consistently. Would you like me to generate practice questions for a specific topic?"
    
    if 'time' in message or 'timetable' in message:
        return "I can help you create a smart timetable. Go to the Timetable section or tell me your weak subjects!"
    
    if 'future' in message or 'career' in message:
        return "You're not just studying for exams — you're building your future! SAMARTH helps you discover your talents."
    
    if 'thank' in message:
        return "You're most welcome! I'm always here to support your academic journey. Keep shining! ✨"
    
    # Default smart responses
    responses = [
        "That's an interesting point! Can you tell me more about what you're struggling with?",
        "I'm here to help you excel. What subject or topic would you like to work on?",
        "Excellent question! Would you like me to generate practice questions on this topic?",
        "Remember: Consistency beats intensity. Small daily improvements lead to big results.",
        "You're doing great by seeking help. That's what successful students do!"
    ]
    
    import random
    return random.choice(responses)


def generate_practice_questions(class_level, chapter, topic):
    """
    Generate practice questions based on input
    """
    if not class_level or not chapter or not topic:
        return {
            "message": "Please provide Class, Chapter and Topic",
            "questions": []
        }
    
    questions = [
        f"Q1: Explain the fundamental concepts of **{topic}** from Chapter {chapter} with real-life examples.",
        f"Q2: Solve a typical numerical/problem-based question on **{topic}** (Class {class_level}).",
        f"Q3: What are the most important formulas/definitions in **{topic}**?",
        f"Q4: Give 3 important MCQs with answers on **{topic}**.",
        f"Q5: How is **{topic}** connected to other chapters in your syllabus?"
    ]
    
    return {
        "message": f"Here are 5 practice questions for **Class {class_level} - {chapter} ({topic})**",
        "questions": questions,
        "tip": "Try solving these without looking at notes first!"
    }