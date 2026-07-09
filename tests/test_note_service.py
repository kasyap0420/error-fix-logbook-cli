import unittest

from app.note_service import (
    create_note,
    delete_note,
    filter_by_tag,
    filter_by_technology,
    find_note_by_id,
    get_dashboard,
    search_notes,
    update_note
)


class TestNoteService(unittest.TestCase):

    def sample_note_data(self):
        return {
            "title": "Python ModuleNotFoundError",
            "technology": "Python",
            "error_message": "ModuleNotFoundError: No module named 'requests'",
            "root_cause": "requests package was not installed",
            "fix": "Install requests using pip",
            "command_used": "pip install requests",
            "tags": ["python", "pip", "venv"],
            "status": "FIXED",
            "difficulty": "EASY",
            "source": "SELF"
        }

    def test_create_note_adds_note_with_id(self):
        notes = []

        updated_notes, created_note = create_note(notes, self.sample_note_data())

        self.assertEqual(len(updated_notes), 1)
        self.assertEqual(created_note["id"], 1)
        self.assertEqual(created_note["title"], "Python ModuleNotFoundError")

    def test_search_notes_finds_by_keyword(self):
        notes, created_note = create_note([], self.sample_note_data())

        results = search_notes(notes, "requests")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], created_note["id"])

    def test_filter_by_technology(self):
        notes, created_note = create_note([], self.sample_note_data())

        results = filter_by_technology(notes, "Python")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["technology"], "Python")

    def test_filter_by_tag(self):
        notes, created_note = create_note([], self.sample_note_data())

        results = filter_by_tag(notes, "venv")

        self.assertEqual(len(results), 1)
        self.assertIn("venv", results[0]["tags"])

    def test_find_note_by_id(self):
        notes, created_note = create_note([], self.sample_note_data())

        found_note = find_note_by_id(notes, created_note["id"])

        self.assertIsNotNone(found_note)
        self.assertEqual(found_note["id"], created_note["id"])

    def test_update_note(self):
        notes, created_note = create_note([], self.sample_note_data())

        updated_notes, updated_note = update_note(
            notes,
            created_note["id"],
            {"status": "OPEN", "difficulty": "MEDIUM"}
        )

        self.assertIsNotNone(updated_note)
        self.assertEqual(updated_note["status"], "OPEN")
        self.assertEqual(updated_note["difficulty"], "MEDIUM")

    def test_delete_note(self):
        notes, created_note = create_note([], self.sample_note_data())

        updated_notes, deleted_note = delete_note(notes, created_note["id"])

        self.assertIsNotNone(deleted_note)
        self.assertEqual(len(updated_notes), 0)

    def test_dashboard_counts_notes(self):
        notes, created_note = create_note([], self.sample_note_data())

        dashboard = get_dashboard(notes)

        self.assertEqual(dashboard["total_notes"], 1)
        self.assertEqual(dashboard["fixed_notes"], 1)
        self.assertEqual(dashboard["easy_notes"], 1)


if __name__ == "__main__":
    unittest.main()