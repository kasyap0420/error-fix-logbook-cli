import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
EXPORTS_DIR = BASE_DIR / "exports"
DATA_FILE = DATA_DIR / "error_notes.json"


def setup_project_files():
    DATA_DIR.mkdir(exist_ok=True)
    EXPORTS_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")

    gitkeep_file = EXPORTS_DIR / ".gitkeep"
    if not gitkeep_file.exists():
        gitkeep_file.write_text("", encoding="utf-8")


def load_notes():
    setup_project_files()

    try:
        file_content = DATA_FILE.read_text(encoding="utf-8").strip()

        if file_content == "":
            save_notes([])
            return []

        notes = json.loads(file_content)

        if isinstance(notes, list):
            return notes

        save_notes([])
        return []

    except json.JSONDecodeError:
        save_notes([])
        return []


def save_notes(notes):
    DATA_DIR.mkdir(exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)


def get_required_input(label):
    while True:
        value = input(label).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_optional_input(label):
    return input(label).strip()


def parse_tags(tags_text):
    if not tags_text:
        return []

    tags = []

    for tag in tags_text.split(","):
        cleaned_tag = tag.strip()

        if cleaned_tag:
            tags.append(cleaned_tag)

    return tags


def get_next_id(notes):
    if not notes:
        return 1

    max_id = 0

    for note in notes:
        try:
            note_id = int(note.get("id", 0))
            if note_id > max_id:
                max_id = note_id
        except ValueError:
            continue

    return max_id + 1


def add_note():
    notes = load_notes()

    print("\nAdd New Error Note")
    print("-" * 40)

    title = get_required_input("Title: ")
    technology = get_required_input("Technology: ")
    error_message = get_required_input("Error message: ")
    root_cause = get_required_input("Root cause: ")
    fix = get_required_input("Fix: ")
    command_used = get_optional_input("Command used (optional): ")
    tags_text = get_optional_input("Tags separated by comma (optional): ")

    note = {
        "id": get_next_id(notes),
        "title": title,
        "technology": technology,
        "error_message": error_message,
        "root_cause": root_cause,
        "fix": fix,
        "command_used": command_used,
        "tags": parse_tags(tags_text),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    notes.append(note)
    save_notes(notes)

    print("\nError note saved successfully.")
    print(f"Saved note ID: {note['id']}")


def format_tags(tags):
    if not tags:
        return "No tags"

    return ", ".join(tags)


def print_note_summary(note):
    print(
        f"{note.get('id')}. "
        f"{note.get('title', 'No title')} "
        f"[{note.get('technology', 'No technology')}] "
        f"- Tags: {format_tags(note.get('tags', []))} "
        f"- Created: {note.get('created_at', 'No date')}"
    )


def view_all_notes():
    notes = load_notes()

    print("\nAll Saved Error Notes")
    print("-" * 40)

    if not notes:
        print("No error notes found.")
        return

    for note in notes:
        print_note_summary(note)


def find_note_by_id(notes, note_id):
    for note in notes:
        if str(note.get("id")) == str(note_id):
            return note

    return None


def print_note_detail(note):
    print("\nError Note Detail")
    print("-" * 40)
    print(f"ID: {note.get('id')}")
    print(f"Title: {note.get('title')}")
    print(f"Technology: {note.get('technology')}")
    print(f"Error Message:\n{note.get('error_message')}")
    print(f"Root Cause:\n{note.get('root_cause')}")
    print(f"Fix:\n{note.get('fix')}")
    print(f"Command Used: {note.get('command_used') or 'Not recorded'}")
    print(f"Tags: {format_tags(note.get('tags', []))}")
    print(f"Created At: {note.get('created_at')}")


def view_note_detail():
    notes = load_notes()

    if not notes:
        print("\nNo error notes found.")
        return

    print("\nView One Error Note")
    print("-" * 40)

    note_id = get_required_input("Enter note ID: ")
    note = find_note_by_id(notes, note_id)

    if note is None:
        print("No note found with that ID.")
        return

    print_note_detail(note)


def note_matches_keyword(note, keyword):
    searchable_fields = [
        "title",
        "technology",
        "error_message",
        "root_cause",
        "fix",
        "command_used"
    ]

    combined_text = ""

    for field in searchable_fields:
        combined_text += " " + str(note.get(field, ""))

    combined_text += " " + " ".join(note.get("tags", []))

    return keyword.lower() in combined_text.lower()


def search_notes():
    notes = load_notes()

    print("\nSearch Error Notes")
    print("-" * 40)

    if not notes:
        print("No error notes found.")
        return

    keyword = get_required_input("Enter search keyword: ")

    matched_notes = []

    for note in notes:
        if note_matches_keyword(note, keyword):
            matched_notes.append(note)

    if not matched_notes:
        print("No matching notes found.")
        return

    print(f"\nSearch results for: {keyword}")
    print("-" * 40)

    for note in matched_notes:
        print_note_summary(note)


def filter_notes_by_technology():
    notes = load_notes()

    print("\nFilter Notes by Technology")
    print("-" * 40)

    if not notes:
        print("No error notes found.")
        return

    technology = get_required_input("Enter technology name: ")

    matched_notes = []

    for note in notes:
        note_technology = str(note.get("technology", ""))

        if technology.lower() in note_technology.lower():
            matched_notes.append(note)

    if not matched_notes:
        print("No notes found for that technology.")
        return

    print(f"\nNotes for technology: {technology}")
    print("-" * 40)

    for note in matched_notes:
        print_note_summary(note)


def delete_note():
    notes = load_notes()

    print("\nDelete Error Note")
    print("-" * 40)

    if not notes:
        print("No error notes found.")
        return

    note_id = get_required_input("Enter note ID to delete: ")
    note = find_note_by_id(notes, note_id)

    if note is None:
        print("No note found with that ID.")
        return

    print_note_detail(note)

    confirmation = input("\nType YES to delete this note: ").strip()

    if confirmation != "YES":
        print("Delete cancelled.")
        return

    updated_notes = []

    for saved_note in notes:
        if str(saved_note.get("id")) != str(note_id):
            updated_notes.append(saved_note)

    save_notes(updated_notes)

    print("Error note deleted successfully.")


def safe_markdown_value(value):
    if isinstance(value, list):
        if not value:
            return "Not recorded"

        return ", ".join(value)

    if value is None:
        return "Not recorded"

    value = str(value).strip()

    if value == "":
        return "Not recorded"

    return value


def export_notes_to_markdown():
    notes = load_notes()

    print("\nExport Notes to Markdown")
    print("-" * 40)

    if not notes:
        print("No error notes found. Export was not created.")
        return

    EXPORTS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_file = EXPORTS_DIR / f"error_notes_export_{timestamp}.md"

    lines = []
    lines.append("# Error Fix Logbook Export")
    lines.append("")
    lines.append(f"Exported At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Total Notes: {len(notes)}")
    lines.append("")

    for note in notes:
        lines.append("---")
        lines.append("")
        lines.append(f"## {safe_markdown_value(note.get('id'))}. {safe_markdown_value(note.get('title'))}")
        lines.append("")
        lines.append(f"**Technology:** {safe_markdown_value(note.get('technology'))}")
        lines.append("")
        lines.append("**Error Message:**")
        lines.append("")
        lines.append(safe_markdown_value(note.get("error_message")))
        lines.append("")
        lines.append("**Root Cause:**")
        lines.append("")
        lines.append(safe_markdown_value(note.get("root_cause")))
        lines.append("")
        lines.append("**Fix:**")
        lines.append("")
        lines.append(safe_markdown_value(note.get("fix")))
        lines.append("")
        lines.append("**Command Used:**")
        lines.append("")
        lines.append("```")
        lines.append(safe_markdown_value(note.get("command_used")))
        lines.append("```")
        lines.append("")
        lines.append(f"**Tags:** {safe_markdown_value(note.get('tags'))}")
        lines.append("")
        lines.append(f"**Created At:** {safe_markdown_value(note.get('created_at'))}")
        lines.append("")

    export_file.write_text("\n".join(lines), encoding="utf-8")

    print("Markdown export created successfully.")
    print(f"Export file: {export_file}")


def show_menu():
    print("\nError Fix Logbook CLI")
    print("=" * 40)
    print("1. Add a new error note")
    print("2. View all saved error notes")
    print("3. Search error notes by keyword")
    print("4. Filter notes by technology")
    print("5. View one note in detail")
    print("6. Delete an error note")
    print("7. Export all notes to a Markdown file")
    print("8. Exit")


def main():
    setup_project_files()

    while True:
        show_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_all_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            filter_notes_by_technology()
        elif choice == "5":
            view_note_detail()
        elif choice == "6":
            delete_note()
        elif choice == "7":
            export_notes_to_markdown()
        elif choice == "8":
            print("Exiting Error Fix Logbook CLI.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 8.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")