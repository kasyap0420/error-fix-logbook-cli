from datetime import datetime

from app.validators import STATUSES, DIFFICULTIES, SOURCES


def now_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def normalize_tags(tags):
    if tags is None:
        return []

    if isinstance(tags, list):
        cleaned_tags = []

        for tag in tags:
            cleaned_tag = str(tag).strip()

            if cleaned_tag:
                cleaned_tags.append(cleaned_tag)

        return cleaned_tags

    if isinstance(tags, str):
        cleaned_tags = []

        for tag in tags.split(","):
            cleaned_tag = tag.strip()

            if cleaned_tag:
                cleaned_tags.append(cleaned_tag)

        return cleaned_tags

    return []


def normalize_choice(value, allowed_values, default_value):
    if not value:
        return default_value

    cleaned_value = str(value).strip().upper().replace(" ", "_")

    if cleaned_value in allowed_values:
        return cleaned_value

    return default_value


def normalize_note(note):
    current_time = now_string()

    normalized = {
        "id": note.get("id", 0),
        "title": str(note.get("title", "")).strip(),
        "technology": str(note.get("technology", "")).strip(),
        "error_message": str(note.get("error_message", "")).strip(),
        "root_cause": str(note.get("root_cause", "")).strip(),
        "fix": str(note.get("fix", "")).strip(),
        "command_used": str(note.get("command_used", "")).strip(),
        "tags": normalize_tags(note.get("tags", [])),
        "status": normalize_choice(note.get("status"), STATUSES, "FIXED"),
        "difficulty": normalize_choice(note.get("difficulty"), DIFFICULTIES, "MEDIUM"),
        "source": normalize_choice(note.get("source"), SOURCES, "SELF"),
        "created_at": note.get("created_at") or current_time,
        "updated_at": note.get("updated_at") or note.get("created_at") or current_time
    }

    try:
        normalized["id"] = int(normalized["id"])
    except ValueError:
        normalized["id"] = 0

    return normalized


def normalize_notes(notes):
    normalized_notes = []

    for note in notes:
        if isinstance(note, dict):
            normalized_notes.append(normalize_note(note))

    return normalized_notes


def get_next_id(notes):
    if not notes:
        return 1

    highest_id = 0

    for note in notes:
        try:
            note_id = int(note.get("id", 0))

            if note_id > highest_id:
                highest_id = note_id
        except ValueError:
            continue

    return highest_id + 1


def create_note(notes, note_data):
    normalized_notes = normalize_notes(notes)
    current_time = now_string()

    note = {
        "id": get_next_id(normalized_notes),
        "title": str(note_data.get("title", "")).strip(),
        "technology": str(note_data.get("technology", "")).strip(),
        "error_message": str(note_data.get("error_message", "")).strip(),
        "root_cause": str(note_data.get("root_cause", "")).strip(),
        "fix": str(note_data.get("fix", "")).strip(),
        "command_used": str(note_data.get("command_used", "")).strip(),
        "tags": normalize_tags(note_data.get("tags", [])),
        "status": normalize_choice(note_data.get("status"), STATUSES, "FIXED"),
        "difficulty": normalize_choice(note_data.get("difficulty"), DIFFICULTIES, "MEDIUM"),
        "source": normalize_choice(note_data.get("source"), SOURCES, "SELF"),
        "created_at": current_time,
        "updated_at": current_time
    }

    normalized_notes.append(note)
    return normalized_notes, note


def find_note_by_id(notes, note_id):
    for note in normalize_notes(notes):
        if note.get("id") == int(note_id):
            return note

    return None


def update_note(notes, note_id, updates):
    normalized_notes = normalize_notes(notes)

    for note in normalized_notes:
        if note.get("id") == int(note_id):
            for field, value in updates.items():
                if field == "tags":
                    note[field] = normalize_tags(value)
                elif field == "status":
                    note[field] = normalize_choice(value, STATUSES, note.get("status", "FIXED"))
                elif field == "difficulty":
                    note[field] = normalize_choice(value, DIFFICULTIES, note.get("difficulty", "MEDIUM"))
                elif field == "source":
                    note[field] = normalize_choice(value, SOURCES, note.get("source", "SELF"))
                else:
                    note[field] = str(value).strip()

            note["updated_at"] = now_string()
            return normalized_notes, note

    return normalized_notes, None


def delete_note(notes, note_id):
    normalized_notes = normalize_notes(notes)

    for index, note in enumerate(normalized_notes):
        if note.get("id") == int(note_id):
            deleted_note = normalized_notes.pop(index)
            return normalized_notes, deleted_note

    return normalized_notes, None


def note_matches_keyword(note, keyword):
    keyword = keyword.lower().strip()

    searchable_text = " ".join([
        str(note.get("title", "")),
        str(note.get("technology", "")),
        str(note.get("error_message", "")),
        str(note.get("root_cause", "")),
        str(note.get("fix", "")),
        str(note.get("command_used", "")),
        str(note.get("status", "")),
        str(note.get("difficulty", "")),
        str(note.get("source", "")),
        " ".join(note.get("tags", []))
    ])

    return keyword in searchable_text.lower()


def search_notes(notes, keyword):
    matched_notes = []

    for note in normalize_notes(notes):
        if note_matches_keyword(note, keyword):
            matched_notes.append(note)

    return matched_notes


def filter_by_technology(notes, technology):
    matched_notes = []

    for note in normalize_notes(notes):
        if technology.lower().strip() in note.get("technology", "").lower():
            matched_notes.append(note)

    return matched_notes


def filter_by_tag(notes, tag):
    matched_notes = []
    search_tag = tag.lower().strip()

    for note in normalize_notes(notes):
        note_tags = note.get("tags", [])

        for saved_tag in note_tags:
            if search_tag in saved_tag.lower():
                matched_notes.append(note)
                break

    return matched_notes


def filter_by_status(notes, status):
    selected_status = normalize_choice(status, STATUSES, "")

    return [
        note for note in normalize_notes(notes)
        if note.get("status") == selected_status
    ]


def filter_by_difficulty(notes, difficulty):
    selected_difficulty = normalize_choice(difficulty, DIFFICULTIES, "")

    return [
        note for note in normalize_notes(notes)
        if note.get("difficulty") == selected_difficulty
    ]


def sort_notes(notes, sort_type):
    normalized_notes = normalize_notes(notes)

    if sort_type == "oldest":
        return sorted(normalized_notes, key=lambda note: note.get("created_at", ""))

    if sort_type == "title":
        return sorted(normalized_notes, key=lambda note: note.get("title", "").lower())

    if sort_type == "technology":
        return sorted(normalized_notes, key=lambda note: note.get("technology", "").lower())

    return sorted(normalized_notes, key=lambda note: note.get("created_at", ""), reverse=True)


def get_dashboard(notes):
    normalized_notes = normalize_notes(notes)

    dashboard = {
        "total_notes": len(normalized_notes),
        "open_notes": 0,
        "fixed_notes": 0,
        "needs_review_notes": 0,
        "easy_notes": 0,
        "medium_notes": 0,
        "hard_notes": 0,
        "technologies": []
    }

    technologies = set()

    for note in normalized_notes:
        status = note.get("status")

        if status == "OPEN":
            dashboard["open_notes"] += 1
        elif status == "FIXED":
            dashboard["fixed_notes"] += 1
        elif status == "NEEDS_REVIEW":
            dashboard["needs_review_notes"] += 1

        difficulty = note.get("difficulty")

        if difficulty == "EASY":
            dashboard["easy_notes"] += 1
        elif difficulty == "MEDIUM":
            dashboard["medium_notes"] += 1
        elif difficulty == "HARD":
            dashboard["hard_notes"] += 1

        technology = note.get("technology", "").strip()

        if technology:
            technologies.add(technology)

    dashboard["technologies"] = sorted(technologies)

    return dashboard