# Manual Testing

This file contains manual test cases for the intermediate version of Error Fix Logbook CLI.

Before testing, open the project folder:

```powershell
cd "C:\Users\kasya\OneDrive\Documents\error-fix-logbook-cli"
```

Activate virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the project:

```powershell
python main.py
```

To reset data before testing:

```powershell
Set-Content -Path ".\data\error_notes.json" -Value "[]"
```

---

## Test Case 1

| Field            | Details                                                |
| ---------------- | ------------------------------------------------------ |
| Test Case Number | TC-01                                                  |
| Feature Tested   | Program startup                                        |
| Steps            | 1. Run `python main.py`.                               |
| Expected Result  | Program starts and displays menu options from 1 to 11. |
| Actual Result    | To be filled after testing.                            |

---

## Test Case 2

| Field            | Details                                                                                            |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-02                                                                                              |
| Feature Tested   | Header dashboard with empty data                                                                   |
| Steps            | 1. Reset `data/error_notes.json` to `[]`.<br>2. Run `python main.py`.                              |
| Expected Result  | Header shows `Saved Notes: 0`, `Open: 0`, `Fixed: 0`, `Needs Review: 0`, and `Technologies: None`. |
| Actual Result    | To be filled after testing.                                                                        |

---

## Test Case 3

| Field            | Details                               |
| ---------------- | ------------------------------------- |
| Test Case Number | TC-03                                 |
| Feature Tested   | View notes when empty                 |
| Steps            | 1. Select option `2`.                 |
| Expected Result  | Program shows `No error notes found.` |
| Actual Result    | To be filled after testing.           |

---

## Test Case 4

| Field            | Details                                                                                             |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-04                                                                                               |
| Feature Tested   | Add new note                                                                                        |
| Steps            | 1. Select option `1`.<br>2. Enter all required fields.<br>3. Select status, difficulty, and source. |
| Expected Result  | Program saves note and shows saved note ID.                                                         |
| Actual Result    | To be filled after testing.                                                                         |

Sample data:

```text
Title: Python ModuleNotFoundError
Technology: Python
Error message: ModuleNotFoundError: No module named 'requests'
Root cause: requests package was not installed in the active virtual environment
Fix: Activate the virtual environment and install requests
Command used: pip install requests
Tags: python, pip, venv
Status: FIXED
Difficulty: EASY
Source: SELF
```

---

## Test Case 5

| Field            | Details                                                         |
| ---------------- | --------------------------------------------------------------- |
| Test Case Number | TC-05                                                           |
| Feature Tested   | Required field validation                                       |
| Steps            | 1. Select option `1`.<br>2. Press Enter without entering title. |
| Expected Result  | Program shows `This field cannot be empty.`                     |
| Actual Result    | To be filled after testing.                                     |

---

## Test Case 6

| Field            | Details                                                                            |
| ---------------- | ---------------------------------------------------------------------------------- |
| Test Case Number | TC-06                                                                              |
| Feature Tested   | Status selection validation                                                        |
| Steps            | 1. Add a note.<br>2. When status options appear, enter invalid option such as `9`. |
| Expected Result  | Program shows invalid choice message and asks again.                               |
| Actual Result    | To be filled after testing.                                                        |

---

## Test Case 7

| Field            | Details                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------- |
| Test Case Number | TC-07                                                                                    |
| Feature Tested   | Difficulty selection validation                                                          |
| Steps            | 1. Add a note.<br>2. When difficulty options appear, enter invalid option such as `abc`. |
| Expected Result  | Program shows invalid choice message and asks again.                                     |
| Actual Result    | To be filled after testing.                                                              |

---

## Test Case 8

| Field            | Details                                                                |
| ---------------- | ---------------------------------------------------------------------- |
| Test Case Number | TC-08                                                                  |
| Feature Tested   | Source selection validation                                            |
| Steps            | 1. Add a note.<br>2. When source options appear, enter invalid option. |
| Expected Result  | Program shows invalid choice message and asks again.                   |
| Actual Result    | To be filled after testing.                                            |

---

## Test Case 9

| Field            | Details                                                                   |
| ---------------- | ------------------------------------------------------------------------- |
| Test Case Number | TC-09                                                                     |
| Feature Tested   | View notes sorted by newest                                               |
| Steps            | 1. Add at least one note.<br>2. Select option `2`.<br>3. Select `newest`. |
| Expected Result  | Notes are displayed with newest first.                                    |
| Actual Result    | To be filled after testing.                                               |

---

## Test Case 10

| Field            | Details                                                                    |
| ---------------- | -------------------------------------------------------------------------- |
| Test Case Number | TC-10                                                                      |
| Feature Tested   | View notes sorted by oldest                                                |
| Steps            | 1. Add at least two notes.<br>2. Select option `2`.<br>3. Select `oldest`. |
| Expected Result  | Notes are displayed with oldest first.                                     |
| Actual Result    | To be filled after testing.                                                |

---

## Test Case 11

| Field            | Details                                                                            |
| ---------------- | ---------------------------------------------------------------------------------- |
| Test Case Number | TC-11                                                                              |
| Feature Tested   | View notes sorted by title                                                         |
| Steps            | 1. Add notes with different titles.<br>2. Select option `2`.<br>3. Select `title`. |
| Expected Result  | Notes are displayed alphabetically by title.                                       |
| Actual Result    | To be filled after testing.                                                        |

---

## Test Case 12

| Field            | Details                                                                                       |
| ---------------- | --------------------------------------------------------------------------------------------- |
| Test Case Number | TC-12                                                                                         |
| Feature Tested   | View notes sorted by technology                                                               |
| Steps            | 1. Add notes with different technologies.<br>2. Select option `2`.<br>3. Select `technology`. |
| Expected Result  | Notes are displayed alphabetically by technology.                                             |
| Actual Result    | To be filled after testing.                                                                   |

---

## Test Case 13

| Field            | Details                                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-13                                                                                                             |
| Feature Tested   | Search by title                                                                                                   |
| Steps            | 1. Add note with title `Python ModuleNotFoundError`.<br>2. Select option `3`.<br>3. Search `ModuleNotFoundError`. |
| Expected Result  | Matching note is displayed.                                                                                       |
| Actual Result    | To be filled after testing.                                                                                       |

---

## Test Case 14

| Field            | Details                                                                               |
| ---------------- | ------------------------------------------------------------------------------------- |
| Test Case Number | TC-14                                                                                 |
| Feature Tested   | Search by technology                                                                  |
| Steps            | 1. Add note with technology `Python`.<br>2. Select option `3`.<br>3. Search `Python`. |
| Expected Result  | Matching note is displayed.                                                           |
| Actual Result    | To be filled after testing.                                                           |

---

## Test Case 15

| Field            | Details                                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-15                                                                                                                         |
| Feature Tested   | Search by error message                                                                                                       |
| Steps            | 1. Add note with error message containing `ModuleNotFoundError`.<br>2. Select option `3`.<br>3. Search `ModuleNotFoundError`. |
| Expected Result  | Matching note is displayed.                                                                                                   |
| Actual Result    | To be filled after testing.                                                                                                   |

---

## Test Case 16

| Field            | Details                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-16                                                                                                         |
| Feature Tested   | Search by root cause                                                                                          |
| Steps            | 1. Add note where root cause contains `virtual environment`.<br>2. Select option `3`.<br>3. Search `virtual`. |
| Expected Result  | Matching note is displayed.                                                                                   |
| Actual Result    | To be filled after testing.                                                                                   |

---

## Test Case 17

| Field            | Details                                                                                             |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-17                                                                                               |
| Feature Tested   | Search by fix                                                                                       |
| Steps            | 1. Add note where fix contains `install requests`.<br>2. Select option `3`.<br>3. Search `install`. |
| Expected Result  | Matching note is displayed.                                                                         |
| Actual Result    | To be filled after testing.                                                                         |

---

## Test Case 18

| Field            | Details                                                                                       |
| ---------------- | --------------------------------------------------------------------------------------------- |
| Test Case Number | TC-18                                                                                         |
| Feature Tested   | Search by command                                                                             |
| Steps            | 1. Add note with command `pip install requests`.<br>2. Select option `3`.<br>3. Search `pip`. |
| Expected Result  | Matching note is displayed.                                                                   |
| Actual Result    | To be filled after testing.                                                                   |

---

## Test Case 19

| Field            | Details                                                                    |
| ---------------- | -------------------------------------------------------------------------- |
| Test Case Number | TC-19                                                                      |
| Feature Tested   | Search by tag                                                              |
| Steps            | 1. Add note with tag `venv`.<br>2. Select option `3`.<br>3. Search `venv`. |
| Expected Result  | Matching note is displayed.                                                |
| Actual Result    | To be filled after testing.                                                |

---

## Test Case 20

| Field            | Details                                                                   |
| ---------------- | ------------------------------------------------------------------------- |
| Test Case Number | TC-20                                                                     |
| Feature Tested   | Search with no result                                                     |
| Steps            | 1. Select option `3`.<br>2. Search `docker` when no note contains docker. |
| Expected Result  | Program shows `No matching notes found.`                                  |
| Actual Result    | To be filled after testing.                                               |

---

## Test Case 21

| Field            | Details                                                                |
| ---------------- | ---------------------------------------------------------------------- |
| Test Case Number | TC-21                                                                  |
| Feature Tested   | Filter by technology                                                   |
| Steps            | 1. Select option `4`.<br>2. Select `Technology`.<br>3. Enter `Python`. |
| Expected Result  | Notes with Python technology are displayed.                            |
| Actual Result    | To be filled after testing.                                            |

---

## Test Case 22

| Field            | Details                                                       |
| ---------------- | ------------------------------------------------------------- |
| Test Case Number | TC-22                                                         |
| Feature Tested   | Filter by tag                                                 |
| Steps            | 1. Select option `4`.<br>2. Select `Tag`.<br>3. Enter `venv`. |
| Expected Result  | Notes containing tag `venv` are displayed.                    |
| Actual Result    | To be filled after testing.                                   |

---

## Test Case 23

| Field            | Details                                                            |
| ---------------- | ------------------------------------------------------------------ |
| Test Case Number | TC-23                                                              |
| Feature Tested   | Filter by status                                                   |
| Steps            | 1. Select option `4`.<br>2. Select `Status`.<br>3. Select `FIXED`. |
| Expected Result  | Notes with status `FIXED` are displayed.                           |
| Actual Result    | To be filled after testing.                                        |

---

## Test Case 24

| Field            | Details                                                               |
| ---------------- | --------------------------------------------------------------------- |
| Test Case Number | TC-24                                                                 |
| Feature Tested   | Filter by difficulty                                                  |
| Steps            | 1. Select option `4`.<br>2. Select `Difficulty`.<br>3. Select `EASY`. |
| Expected Result  | Notes with difficulty `EASY` are displayed.                           |
| Actual Result    | To be filled after testing.                                           |

---

## Test Case 25

| Field            | Details                                                                       |
| ---------------- | ----------------------------------------------------------------------------- |
| Test Case Number | TC-25                                                                         |
| Feature Tested   | Filter with no result                                                         |
| Steps            | 1. Select option `4`.<br>2. Select a filter value that has no matching notes. |
| Expected Result  | Program shows `No notes found for selected filter.`                           |
| Actual Result    | To be filled after testing.                                                   |

---

## Test Case 26

| Field            | Details                                             |
| ---------------- | --------------------------------------------------- |
| Test Case Number | TC-26                                               |
| Feature Tested   | View one note in detail                             |
| Steps            | 1. Select option `5`.<br>2. Enter existing note ID. |
| Expected Result  | Full note details are displayed.                    |
| Actual Result    | To be filled after testing.                         |

---

## Test Case 27

| Field            | Details                                     |
| ---------------- | ------------------------------------------- |
| Test Case Number | TC-27                                       |
| Feature Tested   | View note with invalid ID                   |
| Steps            | 1. Select option `5`.<br>2. Enter ID `999`. |
| Expected Result  | Program shows `No note found with that ID.` |
| Actual Result    | To be filled after testing.                 |

---

## Test Case 28

| Field            | Details                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| Test Case Number | TC-28                                                                                                              |
| Feature Tested   | Edit note title                                                                                                    |
| Steps            | 1. Select option `6`.<br>2. Enter existing note ID.<br>3. Enter new title.<br>4. Press Enter for unchanged fields. |
| Expected Result  | Note title is updated and `updated_at` changes.                                                                    |
| Actual Result    | To be filled after testing.                                                                                        |

---

## Test Case 29

| Field            | Details                                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-29                                                                                                       |
| Feature Tested   | Edit note status                                                                                            |
| Steps            | 1. Select option `6`.<br>2. Enter existing note ID.<br>3. Choose to change status.<br>4. Select new status. |
| Expected Result  | Note status is updated.                                                                                     |
| Actual Result    | To be filled after testing.                                                                                 |

---

## Test Case 30

| Field            | Details                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-30                                                                                                               |
| Feature Tested   | Edit note difficulty                                                                                                |
| Steps            | 1. Select option `6`.<br>2. Enter existing note ID.<br>3. Choose to change difficulty.<br>4. Select new difficulty. |
| Expected Result  | Note difficulty is updated.                                                                                         |
| Actual Result    | To be filled after testing.                                                                                         |

---

## Test Case 31

| Field            | Details                                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-31                                                                                                       |
| Feature Tested   | Edit note source                                                                                            |
| Steps            | 1. Select option `6`.<br>2. Enter existing note ID.<br>3. Choose to change source.<br>4. Select new source. |
| Expected Result  | Note source is updated.                                                                                     |
| Actual Result    | To be filled after testing.                                                                                 |

---

## Test Case 32

| Field            | Details                                                                                |
| ---------------- | -------------------------------------------------------------------------------------- |
| Test Case Number | TC-32                                                                                  |
| Feature Tested   | Clear tags during edit                                                                 |
| Steps            | 1. Select option `6`.<br>2. Enter existing note ID.<br>3. In tags field, type `CLEAR`. |
| Expected Result  | Tags are removed from the note.                                                        |
| Actual Result    | To be filled after testing.                                                            |

---

## Test Case 33

| Field            | Details                                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Test Case Number | TC-33                                                                                                                                             |
| Feature Tested   | Edit note with no changes                                                                                                                         |
| Steps            | 1. Select option `6`.<br>2. Enter existing note ID.<br>3. Press Enter for all fields.<br>4. Choose no for status, difficulty, and source changes. |
| Expected Result  | Program shows `No changes entered.`                                                                                                               |
| Actual Result    | To be filled after testing.                                                                                                                       |

---

## Test Case 34

| Field            | Details                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Test Case Number | TC-34                                                                                      |
| Feature Tested   | Delete note cancellation                                                                   |
| Steps            | 1. Select option `7`.<br>2. Enter existing note ID.<br>3. When asked to delete, type `no`. |
| Expected Result  | Program shows `Delete cancelled.` and note remains saved.                                  |
| Actual Result    | To be filled after testing.                                                                |

---

## Test Case 35

| Field            | Details                                                                              |
| ---------------- | ------------------------------------------------------------------------------------ |
| Test Case Number | TC-35                                                                                |
| Feature Tested   | Delete note with backup                                                              |
| Steps            | 1. Select option `7`.<br>2. Enter existing note ID.<br>3. Confirm delete with `yes`. |
| Expected Result  | Note is deleted and backup file is created inside `backups/`.                        |
| Actual Result    | To be filled after testing.                                                          |

---

## Test Case 36

| Field            | Details                                     |
| ---------------- | ------------------------------------------- |
| Test Case Number | TC-36                                       |
| Feature Tested   | Delete invalid note ID                      |
| Steps            | 1. Select option `7`.<br>2. Enter ID `999`. |
| Expected Result  | Program shows `No note found with that ID.` |
| Actual Result    | To be filled after testing.                 |

---

## Test Case 37

| Field            | Details                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------- |
| Test Case Number | TC-37                                                                                    |
| Feature Tested   | Dashboard                                                                                |
| Steps            | 1. Add at least one note.<br>2. Select option `8`.                                       |
| Expected Result  | Dashboard displays total notes, status counts, difficulty counts, and technologies used. |
| Actual Result    | To be filled after testing.                                                              |

---

## Test Case 38

| Field            | Details                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| Test Case Number | TC-38                                                                                           |
| Feature Tested   | Export all notes to Markdown                                                                    |
| Steps            | 1. Add at least one note.<br>2. Select option `9`.<br>3. Select `Export all notes to Markdown`. |
| Expected Result  | Markdown file is created inside `exports/`.                                                     |
| Actual Result    | To be filled after testing.                                                                     |

---

## Test Case 39

| Field            | Details                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| Test Case Number | TC-39                                                                                           |
| Feature Tested   | Export one note to Markdown                                                                     |
| Steps            | 1. Select option `9`.<br>2. Select `Export one note to Markdown`.<br>3. Enter existing note ID. |
| Expected Result  | Single note Markdown file is created inside `exports/`.                                         |
| Actual Result    | To be filled after testing.                                                                     |

---

## Test Case 40

| Field            | Details                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Test Case Number | TC-40                                                                                      |
| Feature Tested   | Export all notes to CSV                                                                    |
| Steps            | 1. Add at least one note.<br>2. Select option `9`.<br>3. Select `Export all notes to CSV`. |
| Expected Result  | CSV file is created inside `exports/`.                                                     |
| Actual Result    | To be filled after testing.                                                                |

---

## Test Case 41

| Field            | Details                                                                           |
| ---------------- | --------------------------------------------------------------------------------- |
| Test Case Number | TC-41                                                                             |
| Feature Tested   | Export when no notes exist                                                        |
| Steps            | 1. Reset `data/error_notes.json` to `[]`.<br>2. Run app.<br>3. Select option `9`. |
| Expected Result  | Program shows `No error notes found. Export was not created.`                     |
| Actual Result    | To be filled after testing.                                                       |

---

## Test Case 42

| Field            | Details                                        |
| ---------------- | ---------------------------------------------- |
| Test Case Number | TC-42                                          |
| Feature Tested   | Manual backup                                  |
| Steps            | 1. Select option `10`.                         |
| Expected Result  | Backup JSON file is created inside `backups/`. |
| Actual Result    | To be filled after testing.                    |

---

## Test Case 43

| Field            | Details                                                      |
| ---------------- | ------------------------------------------------------------ |
| Test Case Number | TC-43                                                        |
| Feature Tested   | Invalid menu option                                          |
| Steps            | 1. Enter `99` in main menu.                                  |
| Expected Result  | Program shows `Invalid choice. Enter a number from 1 to 11.` |
| Actual Result    | To be filled after testing.                                  |

---

## Test Case 44

| Field            | Details                                                      |
| ---------------- | ------------------------------------------------------------ |
| Test Case Number | TC-44                                                        |
| Feature Tested   | Exit cancellation                                            |
| Steps            | 1. Select option `11`.<br>2. When asked to exit, enter `no`. |
| Expected Result  | Program returns to main menu.                                |
| Actual Result    | To be filled after testing.                                  |

---

## Test Case 45

| Field            | Details                                                       |
| ---------------- | ------------------------------------------------------------- |
| Test Case Number | TC-45                                                         |
| Feature Tested   | Exit confirmation                                             |
| Steps            | 1. Select option `11`.<br>2. When asked to exit, enter `yes`. |
| Expected Result  | Program shows `Exiting Error Fix Logbook CLI.` and stops.     |
| Actual Result    | To be filled after testing.                                   |

---

## Test Case 46

| Field            | Details                                          |
| ---------------- | ------------------------------------------------ |
| Test Case Number | TC-46                                            |
| Feature Tested   | Keyboard interrupt                               |
| Steps            | 1. Run `python main.py`.<br>2. Press `Ctrl + C`. |
| Expected Result  | Program shows `Program stopped by user.`         |
| Actual Result    | To be filled after testing.                      |

---

## Test Case 47

| Field            | Details                                                     |
| ---------------- | ----------------------------------------------------------- |
| Test Case Number | TC-47                                                       |
| Feature Tested   | JSON file update                                            |
| Steps            | 1. Add a note.<br>2. Open `data/error_notes.json`.          |
| Expected Result  | JSON file contains the saved note with all required fields. |
| Actual Result    | To be filled after testing.                                 |

---

## Test Case 48

| Field            | Details                                                        |
| ---------------- | -------------------------------------------------------------- |
| Test Case Number | TC-48                                                          |
| Feature Tested   | Missing JSON file handling                                     |
| Steps            | 1. Delete `data/error_notes.json`.<br>2. Run `python main.py`. |
| Expected Result  | Program recreates `data/error_notes.json` and does not crash.  |
| Actual Result    | To be filled after testing.                                    |

---

## Test Case 49

| Field            | Details                                                  |
| ---------------- | -------------------------------------------------------- |
| Test Case Number | TC-49                                                    |
| Feature Tested   | Missing exports folder handling                          |
| Steps            | 1. Delete `exports/` folder.<br>2. Run `python main.py`. |
| Expected Result  | Program recreates `exports/` folder and `.gitkeep` file. |
| Actual Result    | To be filled after testing.                              |

---

## Test Case 50

| Field            | Details                                                  |
| ---------------- | -------------------------------------------------------- |
| Test Case Number | TC-50                                                    |
| Feature Tested   | Missing backups folder handling                          |
| Steps            | 1. Delete `backups/` folder.<br>2. Run `python main.py`. |
| Expected Result  | Program recreates `backups/` folder and `.gitkeep` file. |
| Actual Result    | To be filled after testing.                              |

---

## Unit Test Command

Run:

```powershell
python -m unittest discover -s tests
```

Expected result:

```text
Ran 8 tests

OK
```
