from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

def generate_pdf(username, marks, predicted):
    os.makedirs('static/pdfs', exist_ok=True)
    filepath = f'static/pdfs/{username}_report_{datetime.now().strftime("%Y%m%d")}.pdf'
    
    doc = SimpleDocTemplate(filepath, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph(f"SAMARTH PLUS Report - {username}", styles['Title']))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(f"Predicted Performance: <b>{predicted}%</b>", styles['Heading2']))
    
    doc.build(elements)
    return filepath