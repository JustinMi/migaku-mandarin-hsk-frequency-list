import json
import os

# Path to the JSON files
JSON_FILE_PATHS = [
    'complete-hsk-vocabulary/wordlists/exclusive/old/1.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/2.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/3.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/4.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/5.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/6.json',
]
OUTPUT_FILE_PATH = "HSK.json"

# Define the ranges for each JSON file
RANGES = [
    (1, 1500),       # 1.json + 2.json
    (1501, 5000),    # 3.json
    (5001, 15000),   # 4.json
    (15001, 30000),  # 5.json
    (30001, None),   # 6.json (no upper limit)
]

# Section headers for each range
SECTION_HEADERS = ["N5", "N4", "N3", "N2", "N1"]

def extract_simplified_words(file_path: str) -> list:
    """
    Extracts simplified words and their numeric transcriptions from a JSON file.

    Args:
        file_path (str): The path to the JSON file.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract all "simplified" entries with their "numeric" transcription
    simplified_words_with_pinyin = [
        [
            entry.get("simplified", "").lower(),
            entry["forms"][0]["transcriptions"].get("pinyin", "").lower()
        ]
        for entry in data if "simplified" in entry and "forms" in entry
    ]
    return simplified_words_with_pinyin

if __name__ == "__main__":
    giant_list = []

    for i, (start, end) in enumerate(RANGES):
        # Add the section header
        section_header = [SECTION_HEADERS[i], SECTION_HEADERS[i]]
        giant_list.append(section_header)

        if i == 0:
            # Combine 1.json and 2.json for the first range
            extracted_words = extract_simplified_words(JSON_FILE_PATHS[0]) + extract_simplified_words(JSON_FILE_PATHS[1])
        else:
            # Use the corresponding JSON file for other ranges
            extracted_words = extract_simplified_words(JSON_FILE_PATHS[i + 1])

        # Calculate padding needed
        if end is not None:
            padding_needed = end - start + 1 - len(extracted_words)
        else:
            padding_needed = 0  # No padding for the last file

        # Add extracted words to the giant list
        giant_list.extend(extracted_words)

        # Add padding if needed
        if padding_needed > 0:
            giant_list.extend([["", ""]] * padding_needed)

    # Write the giant list to the output file
    with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as output_file:
        output_file.write("[")
        for word in giant_list:
            output_file.write(f"[\"{word[0]}\", \"{word[1]}\"],\n")
        output_file.write("]\n")

    print(f"Giant list has been written to {OUTPUT_FILE_PATH}")
