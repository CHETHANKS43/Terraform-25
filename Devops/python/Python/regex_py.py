import re

def find_all_emails(text):
    """Find all email addresses in the given text."""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    print("Found Emails:", emails)

def extract_phone_numbers(text):
    """Extract phone numbers from text (supports different formats)."""
    pattern = r"\+?\d{1,3}?[ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}"
    phones = re.findall(pattern, text)
    print("Found Phone Numbers:", phones)

def validate_date_format(date_string):
    """Check if a date follows the format YYYY-MM-DD."""
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    match = re.match(pattern, date_string)
    print(f"Date '{date_string}' is valid:" if match else f"Date '{date_string}' is invalid")

def replace_urls(text):
    """Replace all URLs in text with [LINK]."""
    pattern = r"\d{4}-\d{2}-\d{2}"
    updated_text = re.sub(pattern, "[LINK]", text)
    print("Updated Text:", updated_text)

def regex_examples():
    print("--- Regex Module Examples ---")
    sample_text = """
        Contact us at support@example.com or admin@test.com.
        Visit https://example.com for more info.
        Call us at +1 (555) 123-4567 or 555-987-6543.
        Today's date is 2025-03-23.
    """


    find_all_emails(sample_text)
    extract_phone_numbers(sample_text)
    validate_date_format("2025-03-23")
    validate_date_format("23-03-2025")
    replace_urls(sample_text)

if __name__ == "__main__":
    regex_examples()








