"""
A date and calendar-based Python module that describes position in the UBC MDS program and absence-related information.
"""

def status(
    config,
    date=None,
    days_missed=None
):
    """

    Return program status for a given date.
    
    If `days_missed` is a used argument, then program status will also return absence-related information.

    Parameters
    ----------
    config : from the config.py file
        Contains program date information, block structure, and break periods.
    date : str or Python datetime object, optional
        Date at which program status is based upon.
        If None, defaults to today's date.
    days_missed: default is None, optional
        Number of days missed from the 'date' argument.
        If argument is provided, information about absence also returned.

    Returns
    -------
    Dict
        Dictionary will be returned descibing academic position based on date.
        If 'days_missed' is included, then absence-related information will also be included.
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

    >>> status(config, date="Mar 16, 2026", days_missed=5)

    Displays program status from entered date.
    In  addition to the above results in `result`, the following keys will be included:

    result = {
        "days_missed": int,
        "return_date": date,
        "missed_blocks": str,
        "missed_week_in_block": int
    }

    """
    pass 
