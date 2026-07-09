STATUSES = ["OPEN", "FIXED", "NEEDS_REVIEW"]
DIFFICULTIES = ["EASY", "MEDIUM", "HARD"]
SOURCES = [
    "SELF",
    "DOCUMENTATION",
    "COLLEGE",
    "YOUTUBE",
    "STACK_OVERFLOW",
    "CHATGPT",
    "OTHER"
]


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


def choose_from_options(title, options, allow_empty=False):
    print(f"\n{title}")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        choice = input("Enter choice number: ").strip()

        if allow_empty and choice == "":
            return None

        if choice.isdigit():
            choice_number = int(choice)

            if 1 <= choice_number <= len(options):
                return options[choice_number - 1]

        print("Invalid choice. Select a valid option number.")


def ask_yes_no(label):
    while True:
        value = input(label).strip().lower()

        if value in ["y", "yes"]:
            return True

        if value in ["n", "no"]:
            return False

        print("Enter yes or no.")


def get_note_id():
    while True:
        value = input("Enter note ID: ").strip()

        if value.isdigit():
            return int(value)

        print("Invalid ID. Enter a number.")