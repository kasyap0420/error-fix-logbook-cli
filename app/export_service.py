import csv
from datetime import datetime

from app.note_service import normalize_note, normalize_notes
from app.storage import EXPORTS_DIR, ensure_project_files


def safe_text(value):
    if value is None:
        return "Not recorded"

    if isinstance(value, list):
        if not value:
            return "Not recorded"

        return ", ".join(value)

    cleaned_value = str(value).strip()

    if cleaned_value == "":
        return "Not recorded"

    return cleaned_value


def build_note_markdown(note):
    note = normalize_note(note)

    lines = []
    lines.append(f"## {note.get('id')}. {safe_text(note.get('title'))}")
    lines.append("")
    lines.append(f"**Technology:** {safe_text(note.get('technology'))}")
    lines.append("")
    lines.append(f"**Status:** {safe_text(note.get('status'))}")
    lines.append("")
    lines.append(f"**Difficulty:** {safe_text(note.get('difficulty'))}")
    lines.append("")
    lines.append(f"**Source:** {safe_text(note.get('source'))}")
    lines.append("")
    lines.append("**Error Message:**")
    lines.append("")
    lines.append(safe_text(note.get("error_message")))
    lines.append("")
    lines.append("**Root Cause:**")
    lines.append("")
    lines.append(safe_text(note.get("root_cause")))
    lines.append("")
    lines.append("**Fix:**")
    lines.append("")
    lines.append(safe_text(note.get("fix")))
    lines.append("")
    lines.append("**Command Used:**")
    lines.append("")
    lines.append("```")
    lines.append(safe_text(note.get("command_used")))
    lines.append("```")
    lines.append("")
    lines.append(f"**Tags:** {safe_text(note.get('tags'))}")
    lines.append("")
    lines.append(f"**Created At:** {safe_text(note.get('created_at'))}")
    lines.append("")
    lines.append(f"**Updated At:** {safe_text(note.get('updated_at'))}")
    lines.append("")

    return "\n".join(lines)


def export_all_to_markdown(notes):
    ensure_project_files()

    normalized_notes = normalize_notes(notes)

    if not normalized_notes:
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_file = EXPORTS_DIR / f"error_notes_export_{timestamp}.md"

    lines = []
    lines.append("# Error Fix Logbook Export")
    lines.append("")
    lines.append(f"Exported At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Total Notes: {len(normalized_notes)}")
    lines.append("")

    for note in normalized_notes:
        lines.append("---")
        lines.append("")
        lines.append(build_note_markdown(note))

    export_file.write_text("\n".join(lines), encoding="utf-8")

    return export_file


def export_one_to_markdown(note):
    ensure_project_files()

    if note is None:
        return None

    note = normalize_note(note)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_file = EXPORTS_DIR / f"error_note_{note.get('id')}_{timestamp}.md"

    lines = []
    lines.append("# Error Fix Logbook Single Note Export")
    lines.append("")
    lines.append(f"Exported At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append(build_note_markdown(note))

    export_file.write_text("\n".join(lines), encoding="utf-8")

    return export_file


def export_all_to_csv(notes):
    ensure_project_files()

    normalized_notes = normalize_notes(notes)

    if not normalized_notes:
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_file = EXPORTS_DIR / f"error_notes_export_{timestamp}.csv"

    fieldnames = [
        "id",
        "title",
        "technology",
        "error_message",
        "root_cause",
        "fix",
        "command_used",
        "tags",
        "status",
        "difficulty",
        "source",
        "created_at",
        "updated_at"
    ]

    with export_file.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for note in normalized_notes:
            row = note.copy()
            row["tags"] = ", ".join(row.get("tags", []))
            writer.writerow(row)

    return export_file