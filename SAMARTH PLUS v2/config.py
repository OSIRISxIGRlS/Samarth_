import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Secret key for session management and security
    SECRET_KEY = os.getenv('SECRET_KEY', 'samarth-supportive-ai-mentor-2026-ultra-secure-key')
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///instance/samarth.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Other configurations (you can add more later)
    DEBUG = False