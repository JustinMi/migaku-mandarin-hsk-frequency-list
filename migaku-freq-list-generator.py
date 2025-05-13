import json
import os

# Path to the JSON files from https://github.com/drkameleon/complete-hsk-vocabulary/tree/main
JSON_FILE_PATHS = [
    'complete-hsk-vocabulary/wordlists/exclusive/old/1.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/2.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/3.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/4.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/5.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/6.json',
]
OUTPUT_FILE_PATH = "HSK.json"

# Define the ranges for each JSON file. Migaku's frequency list format is divided into ranges:
# 1st - 1500th element: 5 stars
# 1501st - 5000th: 4 stars
# 5001st - 15000th: 3 stars
# 15001st - 30000th: 2 stars
# 30001st - 60000th: 1 star
# 60001st and above: 0 stars
RANGES = [
    (1, 1500),       # 1.json
    (1501, 5000),    # 2.json
    (5001, 15000),   # 3.json
    (15001, 30000),  # 4.json
    (30001, 60000),   # 5.json
    (60001, None)   # 6.json (no upper limit)
]

# Section headers for each range
SECTION_HEADERS = ["HSK1", "HSK2", "HSK3", "HSK4", "HSK5", "HSK6"]

def extract_simplified_words(file_path: str) -> list:
    """
    Extracts simplified words from a JSON file.

    Args:
        file_path (str): The path to the JSON file.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract all "simplified" entries
    simplified_words = [
        entry.get("simplified", "").lower()
        for entry in data if "simplified" in entry
    ]
    return simplified_words

if __name__ == "__main__":
    giant_list = []

    for i, (start, end) in enumerate(RANGES):
        # Add the section header
        section_header = SECTION_HEADERS[i]
        giant_list.append(section_header)

        # Extract words from the JSON file
        extracted_words = extract_simplified_words(JSON_FILE_PATHS[i])

        # Calculate padding needed. We add `""` as padding to fill the gap between the end of one vocabulary list and the start of the next range.
        # For example, if the vocab list fills elements 1-300 and the next range starts at 1501, then we need to fill the gap between 301 and 1500.
        if end is not None:
            padding_needed = end - start - len(extracted_words)
        else:
            padding_needed = 0  # No padding for the last file

        # Add extracted words to the giant list
        giant_list.extend(extracted_words)

        # Add padding if needed
        if padding_needed > 0:
            giant_list.extend([""] * padding_needed)

    # Write the giant list to the output file
    with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as output_file:
        output_file.write("[")
        for idx, word in enumerate(giant_list):
            output_file.write(f"\"{word}\"")
            
            # Add a comma unless it's the last element
            if idx < len(giant_list) - 1:
                output_file.write(", \n")
        output_file.write("]")

    print(f"Giant list of characters has been written to {OUTPUT_FILE_PATH}")
