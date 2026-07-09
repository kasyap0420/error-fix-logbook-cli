# Error Fix Logbook CLI - Project Explanation

## What Problem This Project Solves

Students often face the same programming errors multiple times while learning coding, tools, Git, Python, Java, databases, and frontend setup.

Usually, the student searches online, fixes the issue, and later forgets:

- What the error was
- Why it happened
- What command fixed it
- Which technology caused it
- What should be remembered next time

This project solves that simple problem by storing programming errors and fixes in a local JSON file.

The user can add error notes, search them, filter them by technology, delete old notes, and export all notes to a Markdown file.

This is a beginner-level Python CLI project.

---

## Why This Project Was Built

This project was built for Kasyap Yanamandra, a final-year B.Tech CSE student preparing for internships and campus placements.

The project is meant to prove practical beginner Python skills such as:

- CLI menu design
- User input handling
- File handling
- JSON storage
- Search logic
- Filter logic
- Delete logic
- Markdown export
- Git and GitHub workflow
- Clean documentation

This project does not use a database, web framework, AI API, or external packages.

---

## Technologies Used

## Python 3

Python is used to build the command-line program.

## JSON

JSON is used to store saved error notes locally.

The storage file is:

```text
data/error_notes.json
```

## Markdown

Markdown is used for exporting saved notes.

Exported files are created inside:

```text
exports/
```

## Python Standard Library Modules

The project uses only built-in Python modules:

```text
json
datetime
pathlib
```

No third-party packages are required.

---

## Folder Explanation

```text
error-fix-logbook-cli/
```

Main project folder.

```text
main.py
```

Contains the full Python CLI program.

```text
data/error_notes.json
```

Stores all saved error notes as a JSON array.

Initial content:

```json
[]
```

```text
exports/.gitkeep
```

Keeps the empty `exports` folder tracked in Git.

```text
README.md
```

Explains the project purpose, setup steps, run command, features, and usage.

```text
EXPLANATION.md
```

Explains how the project works internally.

```text
MANUAL_TESTING.md
```

Contains manual test cases.

```text
requirements.txt
```

Shows that no third-party packages are needed.

```text
.gitignore
```

Ignores Python cache files, virtual environment folders, editor folders, logs, and generated export files.

---

## Data Flow Explanation

The project follows this flow:

```text
User selects menu option
        ↓
Program calls related function
        ↓
Program loads notes from JSON file
        ↓
Program performs add/view/search/filter/delete/export operation
        ↓
Program saves updated data when needed
        ↓
Program shows output in terminal
```

Each error note is stored as a dictionary inside a JSON array.

Example note:

```json
{
    "id": 1,
    "title": "ModuleNotFoundError in Python",
    "technology": "Python",
    "error_message": "ModuleNotFoundError: No module named 'requests'",
    "root_cause": "The package was not installed in the active virtual environment.",
    "fix": "Install the package inside the active environment.",
    "command_used": "pip install requests",
    "tags": ["python", "pip", "module"],
    "created_at": "2026-07-09 15:30:10"
}
```

---

## Function-by-Function Explanation

## `setup_project_files()`

Creates required folders and files if they are missing.

It creates:

- `data/`
- `exports/`
- `data/error_notes.json`
- `exports/.gitkeep`

This prevents the program from crashing if required files or folders are missing.

---

## `load_notes()`

Reads notes from:

```text
data/error_notes.json
```

If the file is missing, empty, or invalid, the program safely returns an empty list.

This helps the program continue instead of crashing.

---

## `save_notes(notes)`

Writes the current notes list into the JSON file.

It uses:

```python
json.dump(notes, file, indent=4)
```

The `indent=4` keeps the JSON file readable.

---

## `get_required_input(label)`

Takes input from the user.

If the user enters an empty value, the program asks again.

This is used for important fields like:

- Title
- Technology
- Error message
- Root cause
- Fix

---

## `get_optional_input(label)`

Takes optional input from the user.

This is used for:

- Command used
- Tags

These fields can be empty.

---

## `parse_tags(tags_text)`

Converts comma-separated tags into a Python list.

Example input:

```text
python, pip, error
```

Converted output:

```python
["python", "pip", "error"]
```

---

## `get_next_id(notes)`

Finds the next note ID.

If there are no notes, the first ID is:

```text
1
```

If the highest saved ID is `4`, the next ID becomes:

```text
5
```

---

## `add_note()`

Adds a new error note.

It asks the user for:

- Title
- Technology
- Error message
- Root cause
- Fix
- Command used
- Tags

Then it creates a note dictionary and saves it to the JSON file.

---

## `format_tags(tags)`

Converts the tags list into readable text.

If tags exist:

```text
python, pip, error
```

If no tags exist:

```text
No tags
```

---

## `print_note_summary(note)`

Prints a short version of one note.

It shows:

- ID
- Title
- Technology
- Tags
- Created date

This is used in:

- View all notes
- Search results
- Technology filter results

---

## `view_all_notes()`

Displays all saved notes.

If no notes exist, it shows:

```text
No error notes found.
```

---

## `find_note_by_id(notes, note_id)`

Finds one note using its ID.

If the note exists, it returns the note.

If not found, it returns:

```text
None
```

---

## `print_note_detail(note)`

Prints the full details of one note.

It displays:

- ID
- Title
- Technology
- Error message
- Root cause
- Fix
- Command used
- Tags
- Created date

---

## `view_note_detail()`

Asks the user to enter a note ID.

If the ID exists, the full note is displayed.

If the ID does not exist, the program shows:

```text
No note found with that ID.
```

---

## `note_matches_keyword(note, keyword)`

Checks whether the search keyword exists in any important field.

Search checks:

- Title
- Technology
- Error message
- Root cause
- Fix
- Command used
- Tags

The search is case-insensitive.

That means `python`, `Python`, and `PYTHON` are treated as matching text.

---

## `search_notes()`

Asks the user for a keyword.

Then it searches all saved notes.

If matching notes exist, it displays them.

If no matching notes exist, it shows:

```text
No matching notes found.
```

---

## `filter_notes_by_technology()`

Asks the user for a technology name.

Then it displays notes where the technology field matches the entered value.

Example:

```text
Python
```

can match:

```text
Python
Python 3
Core Python
```

---

## `delete_note()`

Deletes one note by ID.

The program first shows the full note details.

Then it asks the user to type:

```text
YES
```

Only then the note is deleted.

If the user types anything else, deletion is cancelled.

This avoids accidental deletion.

---

## `safe_markdown_value(value)`

Prepares values before exporting to Markdown.

If a field is empty, it writes:

```text
Not recorded
```

If the value is a list, it converts the list into comma-separated text.

---

## `export_notes_to_markdown()`

Exports all saved notes to a Markdown file inside the `exports/` folder.

The export filename includes date and time.

Example:

```text
error_notes_export_20260709_153010.md
```

If there are no notes, export is not created.

---

## `show_menu()`

Displays the CLI menu.

The menu contains options from `1` to `8`.

---

## `main()`

Runs the main program loop.

It keeps showing the menu until the user selects option `8`.

---

## What Happens When a User Adds a Note

1. User selects option `1`.
2. Program asks for note details.
3. Program validates required fields.
4. Program creates a dictionary for the new note.
5. Program assigns the next ID.
6. Program adds current date and time.
7. Program loads existing notes from JSON.
8. Program appends the new note.
9. Program saves the updated list to JSON.
10. Program shows the saved note ID.

---

## What Happens When a User Searches Notes

1. User selects option `3`.
2. Program asks for a keyword.
3. Program loads all notes from JSON.
4. Program checks the keyword against multiple fields.
5. Matching notes are collected.
6. Program displays matching notes.
7. If no match exists, a clear message is shown.

---

## What Happens When a User Deletes a Note

1. User selects option `6`.
2. Program asks for the note ID.
3. Program searches for that note.
4. If found, full note details are displayed.
5. Program asks for confirmation.
6. User must type `YES`.
7. Program removes the note.
8. Program saves the updated list to JSON.
9. Program displays success message.

---

## What Happens When a User Exports Notes

1. User selects option `7`.
2. Program loads all notes from JSON.
3. If there are no notes, export is skipped.
4. Program creates a Markdown file name using date and time.
5. Program formats each note into Markdown.
6. Program saves the file inside `exports/`.
7. Program prints the export file path.

---

## What Kasyap Should Understand Before Interview

Kasyap should be able to explain:

1. Why this project was built
2. How the CLI menu works
3. How Python functions are used
4. How user input is collected
5. Why JSON was used instead of a database
6. How notes are stored as a list of dictionaries
7. How file handling works
8. How `pathlib` handles file paths
9. How search works across multiple fields
10. How technology filter works
11. Why delete confirmation is used
12. How Markdown export works
13. What happens if the JSON file is missing
14. Why only the standard library was used
15. What the limitations are

---

## Limitations

This is a beginner-level CLI project.

Current limitations:

- No database
- No login system
- No edit note feature
- No tag filter
- No sorting option
- No unit tests
- No GUI
- No web app
- No cloud storage
- No multi-user support

These limitations are acceptable for the current project scope.

---

## Future Improvements

Possible future improvements:

- Add edit note option
- Add filter by tag
- Add sorting by date
- Add CSV export
- Add unit tests
- Add backup before delete
- Add sample notes for demo
- Add better corrupted JSON recovery