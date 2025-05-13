# HSK Vocabulary List Generator

This project contains two things:
1. A ready-made frequency list of Mandarin vocab based on HSK 2.0 levels. If you're looking for a pre-made list, you can just download HSK.json, import it into Migaku, and be done with it. See [How to use HSK.json](#how-to-use-hskjson) for instructions and details.
2. The Python script that generates the list. If you want, you can use it to create a modified HSK list. See [How to generate your own HSK frequency list](#how-to-generate-your-own-hsk-frequency-list) for instructions and details.

## How to use HSK.json

### Instructions

1. Download [HSK.json](https://github.com/JustinMi/migaku-mandarin-hsk-frequency-list/blob/main/HSK.json).
2. Install it in Migaku's settings page.

### Details

Migaku's frequency list format is described [here](https://legacy.migaku.io/tools-guides/migaku-dictionary/manual/#frequency-list-format).

The list is divided into ranges:
- 1st - 1500th element: 5 stars
- 1501st - 5000th: 4 stars
- 5001st - 15000th: 3 stars
- 15001st - 30000th: 2 stars
- 30001st - 60000th: 1 star
- 60001st and above: 0 stars

HSK.json uses HSK 2.0 vocabulary and levels. It's set up such that:
- HSK level 1 is given 5 stars
- HSK level 2 is given 4 stars
- HSK level 3 is given 3 stars
- HSK level 4 is given 2 stars
- HSK level 5 is given 1 star
- HSK level 6 is given 0 stars

If it looks backwards, it's because Migaku's "Recommended Sentences" feature searches words from 5 stars first.
So this way the most basic words in HSK 1 and 2 are prioritized for recommendation.
Migaku's frequency badge colors are also intuitively green for 5 stars, blue for 4 stars, etc. all the way down to red and grey for 1 and 0 stars. So this format is consistent with Migaku's design.
If you'd like to change this, see [Modify which HSK level is assigned to which category](#modify-which-hsk-level-is-assigned-to-which-category).

We add `""` as padding to fill the gap between the end of one vocabulary list and the start of the next range.
For example, if the vocab list for an HSK level fills elements 1-300 and the next range starts at 1501, then we fill the gap between 301 and 1500 with `""`.

We add section headers like "HSK 3" and "HSK 4" for quality of life and searchability reasons but they shouldn't affect anything.

## How to generate your own HSK frequency list

You may want to change the decision to combine HSK 1 and 2 into the 5 stars category.
Or you may want to generate an HSK 3.0 list. Here is how:

### Prerequisites

1. Ensure you have Python 3.7 or higher installed.
2. Clone a dump of all HSK 2.0 and 3.0 vocabulary from https://github.com/drkameleon/complete-hsk-vocabulary/tree/main.

### How to Use

1. Ensure prerequisites are done
2. Clone this repository
3. Run the script to generate the vocab list: 
```bash
python3 migaku-freq-list-generator.py
```
4. Output: The output file, HSK.json, will be created in the project directory. It contains characters grouped by HSK levels, with padding to ensure consistent ranges.

### How to modify

#### Change Section Headers
To change the section headers (e.g., "HSK3", "HSK4"), update the SECTION_HEADERS variable:

```python
SECTION_HEADERS = ["HSK1 and HSK2", "HSK3", "HSK4", "HSK5", "HSK6"]
```

You can also remove section headers; they're included for quality of life reasons but they shouldn't affect things either way.

#### Modify Input Files
The script reads JSON files from the JSON_FILE_PATHS list.
To add or remove input files, update this list:

```python
JSON_FILE_PATHS = [
    'complete-hsk-vocabulary/wordlists/exclusive/old/1.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/2.json',
    ...
]
```

#### Change Output File Name
To change the name of the output file, update the OUTPUT_FILE_PATH variable:

```python
OUTPUT_FILE_PATH = "HSK.json"
```

#### Modify which HSK level is assigned to which category
By default, HSK level 1 is given 5 stars, HSK level 2 is given 4 stars, etc. (see [Details](#details)).
If you want to modify this, then change the order of `JSON_FILE_PATHS`.

```python
# Marks HSK 6 words as 5 stars, HSK 5 words as 4 stars, and so on.
JSON_FILE_PATHS = [
    'complete-hsk-vocabulary/wordlists/exclusive/old/6.json',
    'complete-hsk-vocabulary/wordlists/exclusive/old/5.json',
    ...
]
```

For consistency, you should also change the order of the `SECTION_HEADERS` to match.
