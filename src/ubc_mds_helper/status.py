"""
A date and calendar-based Python module that describes position in the UBC MDS program.

Author: Ian Gault

Date: January 9, 2026
"""

from datetime import datetime, date
from config import PROGRAM_CONFIG_2025_2026
from helper_functions import normalize_date


def status(
    config,
    date_input=None
):
    """

    Return program status for a given date.

    Parameters
    ----------
    config : from the config.py file
        Contains program date information, block structure, and break periods.
    date_input : str or Python datetime object, optional
        Date at which program status is based upon.
        If None, defaults to today's date.

    Returns
    -------
    Dict
        Dictionary will be returned descibing academic position based on date.
        Dictionary is printed out in the console for viewing

    Examples
    --------
    >>> status(config)
    
    Displays program status from today's date.

    result = {
        "date": date,
        "day_of_week": date,
        "block": None,
        "week_in_block": None,
        "during_break": False,
        "break_name": None,
        "days_until_next_break": None,
        "next_break_name": None
    }

    """

    # if the date passed in are None, retrieve them from PROGRAM_CONFIG_2025_2026 in config.py
    if date_input is None:
        date_input = date.today()

    # normalize the dates that are passed in: if argument is a datetime.date, return date; if string, try to convert it to an accepted datetime format or throw an error
    date_input = normalize_date(date_input)

    return {
        "date": date_input,
        "day_of_week": date_input.strftime("%A"),
        "block": None,
        "week_in_block": None,
        "during_break": False,
        "break_name": None,
        "days_until_next_break": None,
        "next_break_name": None,
    }

output = status(PROGRAM_CONFIG_2025_2026, "Feb 8, 2026")

for key, value in output.items():
    print(f"{key}: {value}")
