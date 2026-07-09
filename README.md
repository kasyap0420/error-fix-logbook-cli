# Error Fix Logbook CLI

## Project Purpose

Error Fix Logbook CLI is a beginner-level Python command-line project.

It helps a student save programming errors and their fixes in one place. Instead of searching the same error again and again, the user can store the error message, root cause, fix, command used, technology name, and tags.

This project is built for learning practical Python basics, not for production use.

## Features

The CLI menu allows the user to:

1. Add a new error note
2. View all saved error notes
3. Search error notes by keyword
4. Filter notes by technology
5. View one note in detail
6. Delete an error note
7. Export all notes to a Markdown file
8. Exit the program

Each error note stores:

- ID
- Title
- Technology
- Error message
- Root cause
- Fix
- Command used
- Tags
- Created date and time

## Tech Stack

- Python 3
- JSON file storage
- Python standard library only

Python modules used:

- `json`
- `datetime`
- `pathlib`

No external packages are used.

## Folder Structure

```text
error-fix-logbook-cli/
│
├── main.py
├── data/
│   └── error_notes.json
├── exports/
│   └── .gitkeep
├── README.md
├── EXPLANATION.md
├── MANUAL_TESTING.md
├── requirements.txt
└── .gitignore