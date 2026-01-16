"""
A date and calendar-based Python module that describes position in the UBC MDS program.

Author: Ian Gault

Date: January 9, 2026
"""

from datetime import date, timedelta
from .config import PROGRAM_CONFIG_2025_2026
from .helper_functions import normalize_date

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

            DATE: general information on the input date

            BLOCK: calculates which block you are in and the week within the block

            BREAK: determines if you're in a block or on holidays; if you are in a block, will tell you the next upcoming break and how far away it is; disingtuishes between holidays and weekends between blocks

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
        "next_break_name": None,
        "between_blocks" = False
    }

    """

    # --- DATE ---
    # If the date passed in are None, retrieve them from PROGRAM_CONFIG_2025_2026 in config.py
    if date_input is None:
        date_input = date.today()

    # normalize_data() taken from progress.py:
    # Normalizes the dates that are passed in: if argument is a datetime.date, return date; if string, try to convert it to an accepted datetime format or throw an error
    date_input = normalize_date(date_input)

    if date_input < config['program_start'] or date_input > config['program_end']:
        raise ValueError("Entered date is not within the 2025-2026 MDS program cycle")

    # --- INITIALIZE ---
    block = None
    week_in_block = None
    during_break = False
    break_name = None
    days_until_next_break = None
    next_break_name = None
    between_blocks = False

    # NOTE: ChatGPT5 helped correct my code below to effectively get the BLOCK and BREAK infomation into the returned dictionary.

    # --- BLOCK ---
    # NOTE: Through iterative testing, realized that the first block first week starts on a Friday, and the first week of block 1 actually runs for 9 days. I asked ChatGPT5 how to implement this, and the code was updated as below.

    for b in config['blocks']:
        if b['start'] <= date_input <= b['end']:
            block = b['block']
            if block == 1:
                first_week_end = b['start'] + timedelta(days=9)
                if date_input <= first_week_end:
                    week_in_block = 1
                else:
                    block_week_start = first_week_end + timedelta(days=1)
                    week_start = date_input - timedelta(days=date_input.weekday())
                    week_in_block = ((week_start - block_week_start).days // 7) + 2
            else:
                block_week_start = b['start'] - timedelta(days=b['start'].weekday())
                week_start = date_input - timedelta(days=date_input.weekday())
                week_in_block = ((week_start - block_week_start).days // 7) + 1
            break

    # --- BREAK ---
    # Update Break general info
    for br in config['breaks']:
        if br['start'] <= date_input <= br['end']:
            during_break = True
            break_name = br['name']
            break
    
    # Assessment of upcoming breaks and days until it starts
    upcoming_breaks = [br for br in config['breaks'] if br['start'] > date_input]

    if upcoming_breaks:
        next_break = min(upcoming_breaks, key=lambda br: br['start'])
        days_until_next_break = (next_break['start'] - date_input).days
        next_break_name = next_break['name']

    if block is None and not during_break:
        between_blocks = True

    # RETURN the dictionary of metrics
    return {
        "date": date_input,
        "day_of_week": date_input.strftime("%A"),
        "block": block,
        "week_in_block": week_in_block,
        "during_break": during_break,
        "break_name": break_name,
        "days_until_next_break": days_until_next_break,
        "next_break_name": next_break_name,
        "between_blocks": between_blocks,
    }

# Test output of status()
if __name__ == "__main__":
    output = status(PROGRAM_CONFIG_2025_2026)

    for key, value in output.items():
        print(f"{key}: {value}")
