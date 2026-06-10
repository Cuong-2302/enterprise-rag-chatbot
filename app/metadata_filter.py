def detect_section(text):

    text = text.lower()

    if "personal projects" in text:
        return "projects"

    if "work experience" in text:
        return "experience"

    if "technical skills" in text:
        return "skills"

    if "education" in text:
        return "education"

    return "other"