# Error Fix Logbook CLI - Explanation

## What Problem This Project Solves

Students often face repeated programming errors while learning coding, tools, Git, Python, Java, databases, frontend setup, and command-line usage.

Many times, the student fixes the issue once but forgets:

* What the error message was
* Why the error happened
* Which command fixed it
* Which technology caused it
* Where the fix came from
* Whether the issue is fully fixed or still needs review

This project solves that problem by giving the user a simple command-line tool to save error notes locally.

The saved notes can be searched, filtered, edited, deleted, backed up, and exported.

---

## Why This Project Was Built

This project was built for Kasyap Yanamandra, a final-year B.Tech CSE student preparing for internships and campus placements.

The project shows practical Python skills without using unnecessary frameworks.

It demonstrates:

* Python functions
* Modular code organization
* CLI menu handling
* Input validation
* JSON file storage
* Search logic
* Filter logic
* Sorting logic
* Edit logic
* Backup handling
* Markdown export
* CSV export
* Unit testing
* GitHub workflow
* Clear documentation

This project should be explained as an intermediate Python CLI learning project.

It should not be described as production-ready, AI-powered, advanced, enterprise-level, or professional-grade.

---

## Technologies Used

## Python 3

Python is used to build the CLI application.

## JSON

JSON is used as local file storage.

Main data file:

```text
data/error_notes.json
```

## Markdown

Markdown is used to export readable notes.

Markdown exports are created inside:

```text
exports/
```

## CSV

CSV export is used to create spreadsheet-friendly output.

CSV exports are created inside:

```text
exports/
```

## unittest

Python `unittest` is used for basic service-level tests.

Test file:

```text
tests/test_note_service.py
```

---

## Python Standard Library Modules Used

The project uses only Python standard library modules:

```text
json
csv
datetime
pathlib
shutil
os
unittest
```

No external packages are required.

---

## Folder Explanation

## `main.py`

Entry point of the application.

It imports and runs:

```python
from app.menu import run_app
```

It also catches `KeyboardInterrupt`, so if the user presses `Ctrl + C`, the program stops safely.

---

## `app/`

Contains the main application code.

This folder makes the project more organized than keeping everything inside one large `main.py` file.

---

## `app/__init__.py`

Marks the `app` folder as a Python package.

---

## `app/menu.py`

Handles the terminal interface.

It contains:

* Main menu
* Header display
* User input flow
* Add note screen
* View notes screen
* Search screen
* Filter screen
* Edit screen
* Delete screen
* Dashboard screen
* Export screen
* Backup screen
* Exit confirmation

This file connects user choices to the service functions.

---

## `app/storage.py`

Handles file and folder operations.

It is responsible for:

* Creating required folders
* Creating `data/error_notes.json` if missing
* Loading notes from JSON
* Saving notes to JSON
* Creating backup files

Important functions:

```python
ensure_project_files()
load_notes()
save_notes(notes)
create_backup()
```

---

## `app/note_service.py`

Contains the main note logic.

It is responsible for:

* Creating notes
* Normalizing old and new note data
* Finding notes by ID
* Updating notes
* Deleting notes
* Searching notes
* Filtering notes
* Sorting notes
* Creating dashboard counts

Important functions:

```python
create_note(notes, note_data)
find_note_by_id(notes, note_id)
update_note(notes, note_id, updates)
delete_note(notes, note_id)
search_notes(notes, keyword)
filter_by_technology(notes, technology)
filter_by_tag(notes, tag)
filter_by_status(notes, status)
filter_by_difficulty(notes, difficulty)
sort_notes(notes, sort_type)
get_dashboard(notes)
```

---

## `app/export_service.py`

Handles export logic.

It can export:

* All notes to Markdown
* One note to Markdown
* All notes to CSV

Important functions:

```python
export_all_to_markdown(notes)
export_one_to_markdown(note)
export_all_to_csv(notes)
```

---

## `app/validators.py`

Contains reusable input and validation helpers.

It stores valid choices for:

* Status
* Difficulty
* Source

Important constants:

```python
STATUSES = ["OPEN", "FIXED", "NEEDS_REVIEW"]
DIFFICULTIES = ["EASY", "MEDIUM", "HARD"]
SOURCES = ["SELF", "DOCUMENTATION", "COLLEGE", "YOUTUBE", "STACK_OVERFLOW", "CHATGPT", "OTHER"]
```

Important functions:

```python
get_required_input(label)
get_optional_input(label)
parse_tags(tags_text)
choose_from_options(title, options, allow_empty=False)
ask_yes_no(label)
get_note_id()
```

---

## `data/error_notes.json`

Stores all saved notes as a JSON array.

Initial content:

```json
[]
```

---

## `exports/`

Stores generated export files.

Generated files are ignored by Git:

```text
exports/*.md
exports/*.csv
```

The folder is tracked using:

```text
exports/.gitkeep
```

---

## `backups/`

Stores backup JSON files.

A backup is created before deleting a note.

Generated backup files are ignored by Git:

```text
backups/*.json
```

The folder is tracked using:

```text
backups/.gitkeep
```

---

## `tests/test_note_service.py`

Contains unit tests for the note service logic.

Tests cover:

* Creating notes
* Searching notes
* Filtering by technology
* Filtering by tag
* Finding note by ID
* Updating note
* Deleting note
* Dashboard count

Run tests with:

```powershell
python -m unittest discover -s tests
```

---

## Data Model

Each note contains these fields:

```text
id
title
technology
error_message
root_cause
fix
command_used
tags
status
difficulty
source
created_at
updated_at
```

Example:

```json
{
    "id": 1,
    "title": "Python ModuleNotFoundError",
    "technology": "Python",
    "error_message": "ModuleNotFoundError: No module named 'requests'",
    "root_cause": "requests package was not installed",
    "fix": "Install requests using pip",
    "command_used": "pip install requests",
    "tags": ["python", "pip", "venv"],
    "status": "FIXED",
    "difficulty": "EASY",
    "source": "SELF",
    "created_at": "2026-07-09 16:40:35",
    "updated_at": "2026-07-09 16:40:35"
}
```

---

## Data Flow Explanation

The application follows this flow:

```text
User selects menu option
        ↓
menu.py receives the input
        ↓
menu.py calls service/storage/export function
        ↓
storage.py loads data from JSON
        ↓
note_service.py processes data
        ↓
storage.py saves updated data when needed
        ↓
menu.py displays result in terminal
```

---

## What Happens When the Program Starts

1. `main.py` calls `run_app()`.
2. `run_app()` calls `ensure_project_files()`.
3. Required folders and files are created if missing.
4. The header and dashboard summary are displayed.
5. The main menu is shown.
6. The program waits for user input.

---

## What Happens When a User Adds a Note

1. User selects option `1`.
2. `add_note_menu()` asks for note details.
3. Required fields are validated.
4. Tags are converted into a list.
5. Status, difficulty, and source are selected from fixed options.
6. `create_note()` creates a new note dictionary.
7. The note gets a new ID.
8. `created_at` and `updated_at` are added.
9. `save_notes()` writes the updated notes list to JSON.
10. The program shows the saved note ID.

---

## What Happens When a User Views Notes

1. User selects option `2`.
2. The program loads notes from JSON.
3. The user selects sorting type.
4. Notes are sorted.
5. Short note summaries are displayed.

Sorting options:

```text
newest
oldest
title
technology
```

---

## What Happens When a User Searches Notes

1. User selects option `3`.
2. Program asks for a keyword.
3. Notes are loaded from JSON.
4. `search_notes()` checks the keyword against multiple fields.
5. Matching notes are displayed.
6. If nothing matches, the program shows a clear message.

Search checks:

* Title
* Technology
* Error message
* Root cause
* Fix
* Command used
* Tags
* Status
* Difficulty
* Source

---

## What Happens When a User Filters Notes

1. User selects option `4`.
2. Program asks what to filter by.
3. User selects one of these options:

```text
Technology
Tag
Status
Difficulty
```

4. Related filter function is called.
5. Matching notes are displayed.
6. If no notes match, the program shows a clear message.

---

## What Happens When a User Views One Note

1. User selects option `5`.
2. Program asks for note ID.
3. `find_note_by_id()` searches the saved notes.
4. If found, full note details are displayed.
5. If not found, the program shows a clear message.

---

## What Happens When a User Edits a Note

1. User selects option `6`.
2. Program asks for note ID.
3. Existing note details are displayed.
4. User can press Enter to keep current values.
5. User can enter new values for selected fields.
6. User can change status, difficulty, and source.
7. `update_note()` updates the note.
8. `updated_at` is changed.
9. Updated data is saved to JSON.
10. Updated note details are displayed.

---

## What Happens When a User Deletes a Note

1. User selects option `7`.
2. Program asks for note ID.
3. Existing note details are displayed.
4. Program asks for confirmation.
5. If user confirms, `create_backup()` creates a backup JSON file.
6. `delete_note()` removes the note.
7. Updated notes are saved to JSON.
8. Program displays backup file path.

This reduces the risk of accidental data loss.

---

## What Happens When a User Opens Dashboard

1. User selects option `8`.
2. Notes are loaded from JSON.
3. `get_dashboard()` counts notes by status and difficulty.
4. Technologies are collected.
5. Summary is displayed.

Dashboard includes:

* Total notes
* Open notes
* Fixed notes
* Needs review notes
* Easy notes
* Medium notes
* Hard notes
* Technologies used

---

## What Happens When a User Exports Notes

1. User selects option `9`.
2. Program asks for export type.
3. User can select:

```text
Export all notes to Markdown
Export one note to Markdown
Export all notes to CSV
```

4. Export file is created inside `exports/`.
5. File path is displayed.

---

## What Happens When a User Creates Backup

1. User selects option `10`.
2. `create_backup()` copies `data/error_notes.json`.
3. Backup is saved inside `backups/`.
4. Backup file path is displayed.

---

## What Kasyap Should Understand Before Interview

Kasyap should be able to explain:

1. Why this project was built
2. Why CLI was used
3. Why JSON was used instead of a database
4. What each folder does
5. Why the project was split into modules
6. How `main.py` starts the app
7. How `menu.py` handles user interaction
8. How `storage.py` handles JSON files
9. How `note_service.py` handles business logic
10. How `export_service.py` handles Markdown and CSV exports
11. How `validators.py` handles reusable input validation
12. How search works
13. How filters work
14. How edit works
15. Why backup before delete is useful
16. How unit tests were added
17. What limitations the project has
18. What can be improved later

---

## Why This Is Intermediate Compared to the First Version

The first version had most logic inside `main.py`.

The upgraded version is better because:

* Code is split into modules
* Logic is easier to test
* Edit feature was added
* Dashboard was added
* Status tracking was added
* Difficulty tracking was added
* Source tracking was added
* Tag filtering was added
* Sorting was added
* Backup before delete was added
* CSV export was added
* Unit tests were added

---

## Limitations

Current limitations:

* No database
* No GUI
* No web interface
* No login system
* No cloud backup
* No automatic error detection
* No AI suggestions
* No duplicate detection
* No installable package command
* Basic unit test coverage only

---

## Future Improvements

Possible improvements:

* Add GUI using Tkinter
* Add duplicate note detection
* Add import from CSV
* Add tag statistics
* Add more tests
* Add edit history
* Add archive feature
* Add packaged CLI command
* Add sample demo data
* Add screenshots to README
