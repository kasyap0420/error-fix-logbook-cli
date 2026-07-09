# Manual Testing

This file contains manual test cases for Error Fix Logbook CLI.

---

## Test Case 1

| Field | Details |
|---|---|
| Test Case Number | TC-01 |
| Feature Tested | Program startup |
| Steps | 1. Open terminal in the project folder.<br>2. Run `python main.py`. |
| Expected Result | Program starts and displays menu options 1 to 8. |
| Actual Result | To be filled after testing. |

---

## Test Case 2

| Field | Details |
|---|---|
| Test Case Number | TC-02 |
| Feature Tested | View all notes when no notes exist |
| Steps | 1. Run `python main.py`.<br>2. Select option `2`. |
| Expected Result | Program shows `No error notes found.` |
| Actual Result | To be filled after testing. |

---

## Test Case 3

| Field | Details |
|---|---|
| Test Case Number | TC-03 |
| Feature Tested | Add a new error note |
| Steps | 1. Run `python main.py`.<br>2. Select option `1`.<br>3. Enter title, technology, error message, root cause, fix, command, and tags. |
| Expected Result | Program saves the note and shows the saved note ID. |
| Actual Result | To be filled after testing. |

---

## Test Case 4

| Field | Details |
|---|---|
| Test Case Number | TC-04 |
| Feature Tested | Required input validation |
| Steps | 1. Run `python main.py`.<br>2. Select option `1`.<br>3. Press Enter without typing a title. |
| Expected Result | Program shows `This field cannot be empty.` and asks again. |
| Actual Result | To be filled after testing. |

---

## Test Case 5

| Field | Details |
|---|---|
| Test Case Number | TC-05 |
| Feature Tested | View all saved notes |
| Steps | 1. Add at least one note.<br>2. Select option `2`. |
| Expected Result | Program displays saved notes in summary format with ID, title, technology, tags, and created date. |
| Actual Result | To be filled after testing. |

---

## Test Case 6

| Field | Details |
|---|---|
| Test Case Number | TC-06 |
| Feature Tested | Search notes by title keyword |
| Steps | 1. Add a note with title `Python import error`.<br>2. Select option `3`.<br>3. Search for `import`. |
| Expected Result | Program displays the matching note. |
| Actual Result | To be filled after testing. |

---

## Test Case 7

| Field | Details |
|---|---|
| Test Case Number | TC-07 |
| Feature Tested | Search notes by error message |
| Steps | 1. Add a note with error message `ModuleNotFoundError`.<br>2. Select option `3`.<br>3. Search for `ModuleNotFoundError`. |
| Expected Result | Program displays the matching note. |
| Actual Result | To be filled after testing. |

---

## Test Case 8

| Field | Details |
|---|---|
| Test Case Number | TC-08 |
| Feature Tested | Search notes by root cause |
| Steps | 1. Add a note where root cause contains `package was not installed`.<br>2. Select option `3`.<br>3. Search for `package`. |
| Expected Result | Program displays the matching note. |
| Actual Result | To be filled after testing. |

---

## Test Case 9

| Field | Details |
|---|---|
| Test Case Number | TC-09 |
| Feature Tested | Search notes by fix |
| Steps | 1. Add a note where fix contains `install dependency`.<br>2. Select option `3`.<br>3. Search for `dependency`. |
| Expected Result | Program displays the matching note. |
| Actual Result | To be filled after testing. |

---

## Test Case 10

| Field | Details |
|---|---|
| Test Case Number | TC-10 |
| Feature Tested | Search notes by command used |
| Steps | 1. Add a note with command `pip install requests`.<br>2. Select option `3`.<br>3. Search for `pip`. |
| Expected Result | Program displays the matching note. |
| Actual Result | To be filled after testing. |

---

## Test Case 11

| Field | Details |
|---|---|
| Test Case Number | TC-11 |
| Feature Tested | Search notes by tag |
| Steps | 1. Add a note with tag `venv`.<br>2. Select option `3`.<br>3. Search for `venv`. |
| Expected Result | Program displays the matching note. |
| Actual Result | To be filled after testing. |

---

## Test Case 12

| Field | Details |
|---|---|
| Test Case Number | TC-12 |
| Feature Tested | Search with no matching result |
| Steps | 1. Select option `3`.<br>2. Search for a keyword that does not exist. |
| Expected Result | Program shows `No matching notes found.` |
| Actual Result | To be filled after testing. |

---

## Test Case 13

| Field | Details |
|---|---|
| Test Case Number | TC-13 |
| Feature Tested | Filter notes by technology |
| Steps | 1. Add a note with technology `Python`.<br>2. Select option `4`.<br>3. Enter `Python`. |
| Expected Result | Program displays notes where technology contains `Python`. |
| Actual Result | To be filled after testing. |

---

## Test Case 14

| Field | Details |
|---|---|
| Test Case Number | TC-14 |
| Feature Tested | Filter notes by missing technology |
| Steps | 1. Select option `4`.<br>2. Enter a technology that does not exist in saved notes. |
| Expected Result | Program shows `No notes found for that technology.` |
| Actual Result | To be filled after testing. |

---

## Test Case 15

| Field | Details |
|---|---|
| Test Case Number | TC-15 |
| Feature Tested | View one note in detail |
| Steps | 1. Add a note.<br>2. Select option `5`.<br>3. Enter the note ID. |
| Expected Result | Program displays full details of that note. |
| Actual Result | To be filled after testing. |

---

## Test Case 16

| Field | Details |
|---|---|
| Test Case Number | TC-16 |
| Feature Tested | View note with invalid ID |
| Steps | 1. Select option `5`.<br>2. Enter an ID that does not exist. |
| Expected Result | Program shows `No note found with that ID.` |
| Actual Result | To be filled after testing. |

---

## Test Case 17

| Field | Details |
|---|---|
| Test Case Number | TC-17 |
| Feature Tested | Cancel delete |
| Steps | 1. Add a note.<br>2. Select option `6`.<br>3. Enter the note ID.<br>4. Type anything except `YES`. |
| Expected Result | Program shows `Delete cancelled.` and the note remains saved. |
| Actual Result | To be filled after testing. |

---

## Test Case 18

| Field | Details |
|---|---|
| Test Case Number | TC-18 |
| Feature Tested | Delete note with confirmation |
| Steps | 1. Add a note.<br>2. Select option `6`.<br>3. Enter the note ID.<br>4. Type `YES`. |
| Expected Result | Program deletes the note and shows `Error note deleted successfully.` |
| Actual Result | To be filled after testing. |

---

## Test Case 19

| Field | Details |
|---|---|
| Test Case Number | TC-19 |
| Feature Tested | Export notes to Markdown |
| Steps | 1. Add at least one note.<br>2. Select option `7`. |
| Expected Result | Program creates a Markdown file inside the `exports/` folder. |
| Actual Result | To be filled after testing. |

---

## Test Case 20

| Field | Details |
|---|---|
| Test Case Number | TC-20 |
| Feature Tested | Export when no notes exist |
| Steps | 1. Make sure `data/error_notes.json` contains `[]`.<br>2. Run `python main.py`.<br>3. Select option `7`. |
| Expected Result | Program shows `No error notes found. Export was not created.` |
| Actual Result | To be filled after testing. |

---

## Test Case 21

| Field | Details |
|---|---|
| Test Case Number | TC-21 |
| Feature Tested | Invalid menu option |
| Steps | 1. Run `python main.py`.<br>2. Enter `99`. |
| Expected Result | Program shows `Invalid choice. Enter a number from 1 to 8.` |
| Actual Result | To be filled after testing. |

---

## Test Case 22

| Field | Details |
|---|---|
| Test Case Number | TC-22 |
| Feature Tested | Exit program |
| Steps | 1. Run `python main.py`.<br>2. Select option `8`. |
| Expected Result | Program shows exit message and stops. |
| Actual Result | To be filled after testing. |

---

## Test Case 23

| Field | Details |
|---|---|
| Test Case Number | TC-23 |
| Feature Tested | Missing JSON file handling |
| Steps | 1. Delete `data/error_notes.json`.<br>2. Run `python main.py`. |
| Expected Result | Program recreates `data/error_notes.json` and does not crash. |
| Actual Result | To be filled after testing. |

---

## Test Case 24

| Field | Details |
|---|---|
| Test Case Number | TC-24 |
| Feature Tested | Missing exports folder handling |
| Steps | 1. Delete the `exports` folder.<br>2. Run `python main.py`. |
| Expected Result | Program recreates the `exports` folder and does not crash. |
| Actual Result | To be filled after testing. |

---

## Test Case 25

| Field | Details |
|---|---|
| Test Case Number | TC-25 |
| Feature Tested | JSON file update after adding note |
| Steps | 1. Add a note from the CLI.<br>2. Open `data/error_notes.json`. |
| Expected Result | The new note is saved inside the JSON array with all required fields. |
| Actual Result | To be filled after testing. |

---

## Test Case 26

| Field | Details |
|---|---|
| Test Case Number | TC-26 |
| Feature Tested | Generated export file name |
| Steps | 1. Add at least one note.<br>2. Select option `7`.<br>3. Open the `exports` folder. |
| Expected Result | Export file name contains date and time, for example `error_notes_export_20260709_153010.md`. |
| Actual Result | To be filled after testing. |

---

## Test Case 27

| Field | Details |
|---|---|
| Test Case Number | TC-27 |
| Feature Tested | Program stop using keyboard |
| Steps | 1. Run `python main.py`.<br>2. Press `Ctrl + C`. |
| Expected Result | Program stops and shows `Program stopped by user.` |
| Actual Result | To be filled after testing. |