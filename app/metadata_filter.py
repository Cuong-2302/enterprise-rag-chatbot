# app/metadata_filter.py

def detect_section(text):

    text = text.lower()

    if "personal projects" in text:
        return "project"

    if "technical skills" in text:
        return "skills"

    if "education" in text:
        return "education"

    return "general"