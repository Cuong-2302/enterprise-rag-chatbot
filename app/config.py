from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

VECTOR_DB_DIR = BASE_DIR / "vector_db"

PDF_FILE = DATA_DIR / "resume.pdf"

print(PDF_FILE)
print(PDF_FILE.exists())