# ==============================
# ⏰ SAMARTH SMART TIMETABLE GENERATOR
# Supportive AI Mentor for Academic Results & Talent Hunting
# ==============================

def generate_smart_timetable(marks, wake_time="6:00 AM", school_time="8:00 AM", 
                           home_time="3:30 PM", sleep_time="10:30 PM"):
    """
    Generate personalized smart timetable based on marks
    """
    subjects = [
        "English", 
        "Mathematics", 
        "Chemistry", 
        "Physics", 
        "Arts", 
        "AI/ML"
    ]

    # Classify subjects
    weak = []
    medium = []
    strong = []

    for i in range(len(marks)):
        if marks[i] <= 45:
            weak.append(subjects[i])
        elif marks[i] <= 75:
            medium.append(subjects[i])
        else:
            strong.append(subjects[i])

    timetable = []

    timetable.append(f"🌅 Wake Up: {wake_time}")
    timetable.append("🧘 Morning Exercise / Meditation - 20 mins")

    # Morning Study Slot
    if weak:
        timetable.append(f"📚 Morning Study (Focus on Weak Subjects): {', '.join(weak)}")
    else:
        timetable.append("📖 Morning Study: Revision of Strong Subjects")

    timetable.append(f"🏫 School / College Time: {school_time}")

    timetable.append("🏠 Return Home: " + home_time)
    timetable.append("😌 Rest + Snacks - 45 minutes")

    # Evening Slot
    if weak or medium:
        evening_sub = weak + medium
        timetable.append(f"📝 Evening Focused Study: {', '.join(evening_sub[:3])}")
    else:
        timetable.append("📝 Evening Study: Practice Previous Year Questions")

    timetable.append("🍽️ Dinner + Family Time")

    # Night Slot
    if strong:
        timetable.append(f"🌙 Night Revision: {', '.join(strong)}")
    else:
        timetable.append("🌙 Night Revision: Light Study + Formulae Revision")

    timetable.append(f"😴 Sleep Time: {sleep_time}")

    # AI Suggestions
    timetable.append("─" * 40)
    if len(weak) >= 3:
        timetable.append("⚠️ ALERT: Multiple weak subjects detected. Prioritize basics!")
    elif len(weak) == 0:
        timetable.append("🔥 Excellent! You are performing well in all subjects.")
    
    timetable.append("💡 Pro Tip: Follow this timetable consistently for best results.")

    return timetable