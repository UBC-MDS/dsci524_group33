"""
Configuration file as input into date-based functions.

Ian Gault: This dictionary was created using ChatGPT5 based on the dates and names entered into it as a form of 'toy data'. This allowed for focus to be on the functions and future testing of the milestone assignments, instead of data entry.
"""

from datetime import date

PROGRAM_CONFIG_2025_2026 = {
    "program_start": date(2025, 8, 29),
    "program_end": date(2026, 6, 30),
    "blocks": [
        {"block": 1, "start": date(2025, 8, 29), "end": date(2025, 10, 3)},
        {"block": 2, "start": date(2025, 10, 6), "end": date(2025, 11, 7)},
        {"block": 3, "start": date(2025, 11, 17), "end": date(2025, 12, 19)},
        {"block": 4, "start": date(2026, 1, 5), "end": date(2026, 2, 6)},
        {"block": 5, "start": date(2026, 2, 9), "end": date(2026, 3, 20)},
        {"block": 6, "start": date(2026, 3, 23), "end": date(2026, 4, 24)},
    ],
    "capstone": {"start": date(2026, 4, 27), "end": date(2026, 6, 30)},
    "breaks": [
        {"name": "Fall break", "start": date(2025, 11, 8), "end": date(2025, 11, 16)},
        {"name": "Holiday break", "start": date(2025, 12, 20), "end": date(2026, 1, 4)},
        {"name": "Winter break", "start": date(2026, 2, 15), "end": date(2026, 2, 22)},
    ],
}
