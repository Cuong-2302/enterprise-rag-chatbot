def detect_section(text):

    text = text.upper()

    if "EDUCATION" in text:
        return "education"

    if "WORK EXPERIENCE" in text:
        return "experience"

    if "PERSONAL PROJECTS" in text:
        return "project"

    if "TECHNICAL SKILLS" in text:
        return "skill"

    return "other"