from datetime import date, datetime

# list of allowable date formats. Got syntax help for each date format from: https://www.geeksforgeeks.org/python/python-datetime-strptime-function/
DATE_FORMATS = [
    '%B %d, %Y',# January 10, 2026
    '%B %d %Y', # January 10 2026
    '%b %d, %Y', # Jan 10, 2026
    '%b %d %Y', # Jan 10 2026
    '%Y-%m-%d', # 2026-01-10
    '%m-%d-%Y', # 01-10-2026
    '%Y/%m/%d', # 2026/01/10
    '%m/%d/%Y' # 01/10/2026
]

def normalize_date(value):
    '''
    Helper function to normalize dates passed in as strings or throw an error if the str cannot be converted to a date.
    '''
    # if the value is a date object, return the date object 
    if isinstance(value, date):
        return value 
    
    # if the value is a string object in the format (January 10, 2026, Jan 10, 2026, YYYY-MM-DD, MM-DD-YYYY, YYYY/MM/DD, MM/DD/YYYY), check if it can be parsed to at least one of these formatted dates above
    if isinstance(value, str):
        for date_format in DATE_FORMATS:
            try:
                return datetime.strptime(value, date_format).date()
            except ValueError:
                continue 
        
        # if the str passed in is not able to be converted to any of the above date formats, raise an error 
        raise ValueError(
            f"{value} must be a valid date string. "
            f"Accepted formats include:\n\n"
            f"January 10, 2026\nJanuary 10 2026\nJan 10, 2026\nJan 10 2026\n2026-01-10\n01-10-2026\n2026/01/10\n01/10/2026"
        )
    
    # if the value passed in is not a date object or str, raise a TypeError
    raise TypeError(f"{value} must be a Python datetime.date or str object.")


# used ChatGPT5 for help with the edge case of if the current date is past the capstone end date, making the number of days from start of program to current date larger than number of days from start of program to capstone start date
'''
Prompt used (also mentioned in issue #21: https://github.com/UBC-MDS/dsci524_group33/issues)

ACT AS A HELPFUL TUTOR WITHOUT GIVING ME THE ANSWER BUT GENTLY GUIDING ME TOWARDS IMPROVEMENTS I CAN MAKE WITH THE BELOW FUNCTION SPECIFICATION:
----

FUNCTION SPECIFICATION HERE
'''
def progress_percentage(start: date, current_dt: date, end: date) -> float:
    '''
    Helper function that calculates the total number of days from start to end date, 
    along with the number of days from the start date to current date parameter to 
    calculate the progress from the curremt date to the end date.
    '''
    # number of total days in the program (end date - start date)
    total_days = (end - start).days

    # raise an error if the total_days are less than 0 (if start date is incorrectly inputted as before end date)
    if total_days <= 0: 
        raise ValueError('End date must be after the start date.')
    
    # number of elapsed days from start date to current date 
    elapsed_days = (current_dt - start).days

    # clip the value between 0 and 1 
    return max(0, min(1, elapsed_days / total_days))