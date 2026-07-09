import json
import shutil
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
EXPORTS_DIR = BASE_DIR / "exports"
BACKUPS_DIR = BASE_DIR / "backups"

DATA_FILE = DATA_DIR / "error_notes.json"


def ensure_project_files():
    DATA_DIR.mkdir(exist_ok=True)
    EXPORTS_DIR.mkdir(exist_ok=True)
    BACKUPS_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")

    export_gitkeep = EXPORTS_DIR / ".gitkeep"
    if not export_gitkeep.exists():
        export_gitkeep.write_text("", encoding="utf-8")

    backup_gitkeep = BACKUPS_DIR / ".gitkeep"
    if not backup_gitkeep.exists():
        backup_gitkeep.write_text("", encoding="utf-8")


def load_notes():
    ensure_project_files()

    try:
        content = DATA_FILE.read_text(encoding="utf-8").strip()

        if content == "":
            save_notes([])
            return []

        notes = json.loads(content)

        if isinstance(notes, list):
            return notes

        save_notes([])
        return []

    except json.JSONDecodeError:
        save_notes([])
        return []


def save_notes(notes):
    ensure_project_files()

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)


def create_backup():
    ensure_project_files()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = BACKUPS_DIR / f"error_notes_backup_{timestamp}.json"

    if DATA_FILE.exists():
        shutil.copy2(DATA_FILE, backup_file)
    else:
        backup_file.write_text("[]", encoding="utf-8")

    return backup_file