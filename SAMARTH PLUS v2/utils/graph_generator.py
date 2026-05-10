import matplotlib
matplotlib.use('Agg')  # Important for Flask
import matplotlib.pyplot as plt
import os

def generate_graph(marks, predicted, username):
    subjects = ["Eng", "Math", "Chem", "Phy", "Arts", "AI"]
    
    plt.figure(figsize=(10, 6))
    plt.bar(subjects, marks, color='#6366f1', alpha=0.8, label='Current Marks')
    plt.axhline(y=predicted, color='red', linestyle='--', label=f'Predicted: {predicted}%')
    plt.title(f"{username}'s Performance Analysis")
    plt.ylabel('Marks (%)')
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    os.makedirs('static/images/graphs', exist_ok=True)
    filepath = f'static/images/graphs/{username}_performance.png'
    plt.savefig(filepath, dpi=200, bbox_inches='tight')
    plt.close()
    
    return filepath