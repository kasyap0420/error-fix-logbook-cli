# Error Fix Logbook CLI

## Project Purpose

Error Fix Logbook CLI is a Python command-line project that helps a student save programming errors and fixes for later reference.

Instead of solving the same issue repeatedly, the user can record:

* Error title
* Technology
* Error message
* Root cause
* Fix
* Command used
* Tags
* Status
* Difficulty
* Source
* Created date
* Updated date

This project is built for learning practical Python, file handling, JSON storage, modular code structure, basic testing, and GitHub workflow.

It is a learning project. It is not a web app, desktop GUI, or production tool.

---

## Features

The upgraded CLI supports:

1. Add new error note
2. View notes
3. Search notes
4. Filter notes
5. View one note in detail
6. Edit note
7. Delete note
8. Dashboard
9. Export notes
10. Backup data
11. Exit

---

## Main Features Explained

### Add Error Note

The user can save an error with details like technology, error message, root cause, fix, command, tags, status, difficulty, and source.

### View Notes

The user can view saved notes and sort them by:

* Newest
* Oldest
* Title
* Technology

### Search Notes

Search checks these fields:

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

### Filter Notes

The user can filter notes by:

* Technology
* Tag
* Status
* Difficulty

### Edit Note

The user can update an existing note without deleting and recreating it.

### Delete Note

Before deleting a note, the app creates a JSON backup inside the `backups/` folder.

### Dashboard

The dashboard shows:

* Total notes
* Open notes
* Fixed notes
* Needs review notes
* Easy notes
* Medium notes
* Hard notes
* Technologies used

### Export Notes

The app can export notes to:

* Markdown
* CSV

It can also export one selected note to Markdown.

### Backup Data

The user can manually create a backup of the JSON data file.

---

## Tech Stack

* Python 3
* JSON file storage
* CSV export
* Markdown export
* Python standard library
* `unittest` for basic tests

No external packages are required.

---

## Python Modules Used

The project uses only Python standard library modules:

* `json`
* `csv`
* `datetime`
* `pathlib`
* `shutil`
* `os`
* `unittest`

---

## Folder Structure

```text
error-fix-logbook-cli/
│
├── main.py
├── app/
│   ├── __init__.py
│   ├── menu.py
│   ├── storage.py
│   ├── note_service.py
│   ├── export_service.py
│   └── validators.py
│
├── data/
│   └── error_notes.json
│
├── exports/
│   └── .gitkeep
│
├── backups/
│   └── .gitkeep
│
├── tests/
│   └── test_note_service.py
│
├── README.md
├── EXPLANATION.md
├── MANUAL_TESTING.md
├── requirements.txt
└── .gitignore
```

---

## Setup Steps

### 1. Open Project Folder

```powershell
cd "C:\Users\kasya\OneDrive\Documents\error-fix-logbook-cli"
```

### 2. Create Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 4. Check Python Version

```powershell
python --version
```

### 5. Install Requirements

```powershell
pip install -r requirements.txt
```

No external packages are required. This command is only used to confirm the setup.

---

## Run Command

```powershell
python main.py
```

---

## Run Tests

```powershell
python -m unittest discover -s tests
```

Expected result:

```text
Ran 8 tests

OK
```

---

## CLI Menu

When the project runs, this menu appears:

```text
==================================================
ERROR FIX LOGBOOK CLI
==================================================
Saved Notes  : 0
Open         : 0
Fixed        : 0
Needs Review : 0
Technologies : None
==================================================

Main Menu
--------------------------------------------------
1. Add new error note
2. View notes
3. Search notes
4. Filter notes
5. View one note in detail
6. Edit note
7. Delete note
8. Dashboard
9. Export notes
10. Backup data
11. Exit
```

---

## Sample Note Data

A saved note looks like this in JSON:

```json
{
    "id": 1,
    "title": "Python ModuleNotFoundError",
    "technology": "Python",
    "error_message": "ModuleNotFoundError: No module named 'requests'",
    "root_cause": "requests package was not installed in the active virtual environment",
    "fix": "Activate the virtual environment and install requests",
    "command_used": "pip install requests",
    "tags": [
        "python",
        "pip",
        "venv"
    ],
    "status": "FIXED",
    "difficulty": "EASY",
    "source": "SELF",
    "created_at": "2026-07-09 16:40:35",
    "updated_at": "2026-07-09 16:40:35"
}
```

---

## Status Options

The app supports these status values:

```text
OPEN
FIXED
NEEDS_REVIEW
```

---

## Difficulty Options

The app supports these difficulty values:

```text
EASY
MEDIUM
HARD
```

---

## Source Options

The app supports these source values:

```text
SELF
DOCUMENTATION
COLLEGE
YOUTUBE
STACK_OVERFLOW
CHATGPT
OTHER
```

---

## What This Project Demonstrates

This project demonstrates:

* Python CLI development
* Modular Python project structure
* File handling
* JSON read/write
* CSV export
* Markdown export
* Search logic
* Filter logic
* Sorting logic
* Edit feature
* Delete confirmation
* Backup before delete
* Basic dashboard calculation
* Input validation
* Unit testing with `unittest`
* Git and GitHub workflow
* Beginner-to-intermediate project documentation

---

## Project Status

Current status:

```text
Intermediate Python CLI version completed.
```

Completed work:

* Basic CLI completed
* Modular app folder added
* JSON storage added
* Edit note added
* Dashboard added
* Filters added
* Sorting added
* Backup added
* Markdown export added
* CSV export added
* Unit tests added
* GitHub push completed

---

## Limitations

Current limitations:

* No database
* No login system
* No GUI window
* No web interface
* No cloud sync
* No multi-user support
* No automatic error detection
* No AI-based fix suggestion
* No advanced test coverage
* No packaging as installable CLI command

---

## Future Scope

This project can be improved in the future with:

* Tkinter-based GUI version
* Duplicate note detection
* CSV import support
* Tag-based statistics
* More unit test coverage
* Edit history for notes
* Archive option for old notes
* Installable CLI command support
* Sample demo data
* Terminal screenshots in README
