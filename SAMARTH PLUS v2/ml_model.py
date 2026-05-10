# ==============================
# 🤖 SAMARTH ML MODEL
# Supportive AI Mentor for Academic Results & Talent Hunting
# ==============================

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# ==================== TRAINING DATA ====================
# Improved training data for better predictions
X = np.array([
    [45, 50, 55, 48, 60, 52],   # Average student
    [78, 82, 75, 80, 85, 79],   # Good student
    [92, 88, 95, 90, 85, 93],   # Excellent student
    [35, 40, 38, 42, 45, 39],   # Weak student
    [65, 70, 68, 72, 75, 69],   # Above Average
    [85, 90, 88, 87, 92, 89],   # Very Good
    [55, 60, 58, 62, 65, 59],   # Moderate
    [95, 92, 94, 96, 90, 93]    # Topper
])

y = np.array([52, 80, 93, 40, 71, 88, 62, 94])  # Overall predicted performance

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model (Random Forest for better accuracy)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_scaled, y)

# ==================== PREDICTION FUNCTION ====================
def predict_marks(marks):
    """
    Predict overall performance based on 6 subject marks
    marks: list of 6 integers [eng, math, chem, phy, arts, ai]
    """
    try:
        marks_array = np.array([marks])
        marks_scaled = scaler.transform(marks_array)
        
        prediction = model.predict(marks_scaled)[0]
        
        # Clamp between 0 and 100
        prediction = max(0, min(prediction, 100))
        
        return round(prediction, 2)
    
    except Exception as e:
        print("ML Prediction Error:", e)
        return 65.0  # Default fallback


# Optional: Get subject-wise insights
def get_subject_insights(marks):
    subjects = ["English", "Mathematics", "Chemistry", "Physics", "Arts", "AI/ML"]
    insights = []
    
    for i, score in enumerate(marks):
        if score >= 85:
            level = "Excellent"
        elif score >= 70:
            level = "Good"
        elif score >= 50:
            level = "Average"
        else:
            level = "Needs Improvement"
        
        insights.append({
            "subject": subjects[i],
            "score": score,
            "level": level
        })
    
    return insights