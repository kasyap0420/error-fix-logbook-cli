import os

from app.export_service import (
    export_all_to_csv,
    export_all_to_markdown,
    export_one_to_markdown
)
from app.note_service import (
    create_note,
    delete_note,
    filter_by_difficulty,
    filter_by_status,
    filter_by_tag,
    filter_by_technology,
    find_note_by_id,
    get_dashboard,
    normalize_notes,
    search_notes,
    sort_notes,
    update_note
)
from app.storage import create_backup, ensure_project_files, load_notes, save_notes
from app.validators import (
    DIFFICULTIES,
    SOURCES,
    STATUSES,
    ask_yes_no,
    choose_from_options,
    get_note_id,
    get_optional_input,
    get_required_input,
    parse_tags
)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def print_header():
    notes = normalize_notes(load_notes())
    dashboard = get_dashboard(notes)

    print("=" * 50)
    print("ERROR FIX LOGBOOK CLI")
    print("=" * 50)
    print(f"Saved Notes  : {dashboard['total_notes']}")
    print(f"Open         : {dashboard['open_notes']}")
    print(f"Fixed        : {dashboard['fixed_notes']}")
    print(f"Needs Review : {dashboard['needs_review_notes']}")

    if dashboard["technologies"]:
        print(f"Technologies : {', '.join(dashboard['technologies'])}")
    else:
        print("Technologies : None")

    print("=" * 50)


def show_main_menu():
    print("\nMain Menu")
    print("-" * 50)
    print("1. Add new error note")
    print("2. View notes")
    print("3. Search notes")
    print("4. Filter notes")
    print("5. View one note in detail")
    print("6. Edit note")
    print("7. Delete note")
    print("8. Dashboard")
    print("9. Export notes")
    print("10. Backup data")
    print("11. Exit")


def format_tags(tags):
    if not tags:
        return "No tags"

    return ", ".join(tags)


def print_note_summary(note):
    print(
        f"{note.get('id')}. {note.get('title')} "
        f"[{note.get('technology')}] "
        f"| Status: {note.get('status')} "
        f"| Difficulty: {note.get('difficulty')} "
        f"| Tags: {format_tags(note.get('tags', []))} "
        f"| Created: {note.get('created_at')}"
    )


def print_note_detail(note):
    print("\nError Note Detail")
    print("-" * 50)
    print(f"ID: {note.get('id')}")
    print(f"Title: {note.get('title')}")
    print(f"Technology: {note.get('technology')}")
    print(f"Status: {note.get('status')}")
    print(f"Difficulty: {note.get('difficulty')}")
    print(f"Source: {note.get('source')}")
    print(f"Error Message:\n{note.get('error_message')}")
    print(f"Root Cause:\n{note.get('root_cause')}")
    print(f"Fix:\n{note.get('fix')}")
    print(f"Command Used: {note.get('command_used') or 'Not recorded'}")
    print(f"Tags: {format_tags(note.get('tags', []))}")
    print(f"Created At: {note.get('created_at')}")
    print(f"Updated At: {note.get('updated_at')}")


def add_note_menu():
    notes = load_notes()

    print("\nAdd New Error Note")
    print("-" * 50)

    note_data = {
        "title": get_required_input("Title: "),
        "technology": get_required_input("Technology: "),
        "error_message": get_required_input("Error message: "),
        "root_cause": get_required_input("Root cause: "),
        "fix": get_required_input("Fix: "),
        "command_used": get_optional_input("Command used (optional): "),
        "tags": parse_tags(get_optional_input("Tags separated by comma (optional): ")),
        "status": choose_from_options("Select status", STATUSES),
        "difficulty": choose_from_options("Select difficulty", DIFFICULTIES),
        "source": choose_from_options("Select source", SOURCES)
    }

    updated_notes, created_note = create_note(notes, note_data)
    save_notes(updated_notes)

    print("\nError note saved successfully.")
    print(f"Saved note ID: {created_note.get('id')}")


def view_notes_menu():
    notes = normalize_notes(load_notes())

    print("\nView Notes")
    print("-" * 50)

    if not notes:
        print("No error notes found.")
        return

    sort_choice = choose_from_options(
        "Sort notes by",
        ["newest", "oldest", "title", "technology"]
    )

    sorted_notes = sort_notes(notes, sort_choice)

    print(f"\nTotal Notes: {len(sorted_notes)}")
    print("-" * 50)

    for note in sorted_notes:
        print_note_summary(note)


def search_notes_menu():
    notes = load_notes()

    print("\nSearch Notes")
    print("-" * 50)

    if not notes:
        print("No error notes found.")
        return

    keyword = get_required_input("Enter search keyword: ")
    matched_notes = search_notes(notes, keyword)

    if not matched_notes:
        print("No matching notes found.")
        return

    print(f"\nSearch Results: {len(matched_notes)} note(s)")
    print("-" * 50)

    for note in matched_notes:
        print_note_summary(note)


def filter_notes_menu():
    notes = load_notes()

    print("\nFilter Notes")
    print("-" * 50)

    if not notes:
        print("No error notes found.")
        return

    filter_choice = choose_from_options(
        "Filter by",
        ["Technology", "Tag", "Status", "Difficulty"]
    )

    if filter_choice == "Technology":
        technology = get_required_input("Enter technology: ")
        matched_notes = filter_by_technology(notes, technology)
    elif filter_choice == "Tag":
        tag = get_required_input("Enter tag: ")
        matched_notes = filter_by_tag(notes, tag)
    elif filter_choice == "Status":
        status = choose_from_options("Select status", STATUSES)
        matched_notes = filter_by_status(notes, status)
    else:
        difficulty = choose_from_options("Select difficulty", DIFFICULTIES)
        matched_notes = filter_by_difficulty(notes, difficulty)

    if not matched_notes:
        print("No notes found for selected filter.")
        return

    print(f"\nFiltered Results: {len(matched_notes)} note(s)")
    print("-" * 50)

    for note in matched_notes:
        print_note_summary(note)


def view_note_detail_menu():
    notes = load_notes()

    print("\nView One Note")
    print("-" * 50)

    if not notes:
        print("No error notes found.")
        return

    note_id = get_note_id()
    note = find_note_by_id(notes, note_id)

    if note is None:
        print("No note found with that ID.")
        return

    print_note_detail(note)


def edit_note_menu():
    notes = load_notes()

    print("\nEdit Note")
    print("-" * 50)

    if not notes:
        print("No error notes found.")
        return

    note_id = get_note_id()
    note = find_note_by_id(notes, note_id)

    if note is None:
        print("No note found with that ID.")
        return

    print_note_detail(note)

    print("\nPress Enter to keep the current value.")
    print("For tags, type CLEAR to remove all tags.")

    updates = {}

    title = input(f"Title [{note.get('title')}]: ").strip()
    if title:
        updates["title"] = title

    technology = input(f"Technology [{note.get('technology')}]: ").strip()
    if technology:
        updates["technology"] = technology

    error_message = input("Error message [keep current if blank]: ").strip()
    if error_message:
        updates["error_message"] = error_message

    root_cause = input("Root cause [keep current if blank]: ").strip()
    if root_cause:
        updates["root_cause"] = root_cause

    fix = input("Fix [keep current if blank]: ").strip()
    if fix:
        updates["fix"] = fix

    command_used = input(f"Command used [{note.get('command_used') or 'Not recorded'}]: ").strip()
    if command_used:
        updates["command_used"] = command_used

    tags = input(f"Tags [{format_tags(note.get('tags', []))}]: ").strip()
    if tags.upper() == "CLEAR":
        updates["tags"] = []
    elif tags:
        updates["tags"] = parse_tags(tags)

    if ask_yes_no("Change status? yes/no: "):
        updates["status"] = choose_from_options("Select new status", STATUSES)

    if ask_yes_no("Change difficulty? yes/no: "):
        updates["difficulty"] = choose_from_options("Select new difficulty", DIFFICULTIES)

    if ask_yes_no("Change source? yes/no: "):
        updates["source"] = choose_from_options("Select new source", SOURCES)

    if not updates:
        print("No changes entered.")
        return

    updated_notes, updated_note = update_note(notes, note_id, updates)
    save_notes(updated_notes)

    print("\nNote updated successfully.")
    print_note_detail(updated_note)


def delete_note_menu():
    notes = load_notes()

    print("\nDelete Note")
    print("-" * 50)

    if not notes:
        print("No error notes found.")
        return

    note_id = get_note_id()
    note = find_note_by_id(notes, note_id)

    if note is None:
        print("No note found with that ID.")
        return

    print_note_detail(note)

    if not ask_yes_no("\nDelete this note? yes/no: "):
        print("Delete cancelled.")
        return

    backup_file = create_backup()

    updated_notes, deleted_note = delete_note(notes, note_id)
    save_notes(updated_notes)

    print("\nNote deleted successfully.")
    print(f"Backup created before delete: {backup_file}")


def dashboard_menu():
    notes = load_notes()
    dashboard = get_dashboard(notes)

    print("\nDashboard")
    print("-" * 50)
    print(f"Total Notes       : {dashboard['total_notes']}")
    print(f"Open Notes        : {dashboard['open_notes']}")
    print(f"Fixed Notes       : {dashboard['fixed_notes']}")
    print(f"Needs Review      : {dashboard['needs_review_notes']}")
    print(f"Easy Notes        : {dashboard['easy_notes']}")
    print(f"Medium Notes      : {dashboard['medium_notes']}")
    print(f"Hard Notes        : {dashboard['hard_notes']}")

    if dashboard["technologies"]:
        print(f"Technologies Used : {', '.join(dashboard['technologies'])}")
    else:
        print("Technologies Used : None")


def export_notes_menu():
    notes = load_notes()

    print("\nExport Notes")
    print("-" * 50)

    if not notes:
        print("No error notes found. Export was not created.")
        return

    export_choice = choose_from_options(
        "Select export type",
        [
            "Export all notes to Markdown",
            "Export one note to Markdown",
            "Export all notes to CSV"
        ]
    )

    if export_choice == "Export all notes to Markdown":
        export_file = export_all_to_markdown(notes)
    elif export_choice == "Export one note to Markdown":
        note_id = get_note_id()
        note = find_note_by_id(notes, note_id)

        if note is None:
            print("No note found with that ID.")
            return

        export_file = export_one_to_markdown(note)
    else:
        export_file = export_all_to_csv(notes)

    if export_file is None:
        print("Export was not created.")
        return

    print("\nExport created successfully.")
    print(f"Export file: {export_file}")


def backup_data_menu():
    print("\nBackup Data")
    print("-" * 50)

    backup_file = create_backup()

    print("Backup created successfully.")
    print(f"Backup file: {backup_file}")


def run_app():
    ensure_project_files()

    while True:
        clear_screen()
        print_header()
        show_main_menu()

        choice = input("\nEnter your choice: ").strip()

        clear_screen()

        if choice == "1":
            add_note_menu()
        elif choice == "2":
            view_notes_menu()
        elif choice == "3":
            search_notes_menu()
        elif choice == "4":
            filter_notes_menu()
        elif choice == "5":
            view_note_detail_menu()
        elif choice == "6":
            edit_note_menu()
        elif choice == "7":
            delete_note_menu()
        elif choice == "8":
            dashboard_menu()
        elif choice == "9":
            export_notes_menu()
        elif choice == "10":
            backup_data_menu()
        elif choice == "11":
            if ask_yes_no("Exit the program? yes/no: "):
                print("Exiting Error Fix Logbook CLI.")
                break
        else:
            print("Invalid choice. Enter a number from 1 to 11.")

        pause()