from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report, insight, file_path="data_report.pdf"):
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Data Quality Report", styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"Quality Score: {report.get('data_quality_score')}%", styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Missing Values:", styles["Heading2"]))
    content.append(Paragraph(str(report.get("missing_values")), styles["Normal"]))

    content.append(Spacer(1, 10))

    content.append(Paragraph("Duplicates:", styles["Heading2"]))
    content.append(Paragraph(str(report.get("duplicates")), styles["Normal"]))

    content.append(Spacer(1, 10))

    content.append(Paragraph("Outliers:", styles["Heading2"]))
    content.append(Paragraph(str(report.get("outliers")), styles["Normal"]))

    content.append(Spacer(1, 20))

    content.append(Paragraph("AI Insight:", styles["Heading2"]))
    content.append(Paragraph(insight, styles["Normal"]))

    doc.build(content)

    return file_path