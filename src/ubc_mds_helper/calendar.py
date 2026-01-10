"""
A date and calendar-based Python module that helps UBC MDS students check specific 
program level details using UBC MDS specific dates using a config file containing dates.

Author: Jasjot Parmar

Date: January 9, 2026
"""

def visualize_program_progress(
        current_date = None,
        program_start_date = None,
        program_end_date = None,
        capstone_start_date = None
):
    """
    Visualizes program progress (in %) from a date to the capstone and program end date.

    Calculates the percentage of elapsed time between the program start date to the capstone start date and program end date
    of the UBC MDS program, and visualizes the result as a bar chart.
    
    Parameters
    ----------
    current_date : str or Python datetime object, optional
        Date at which visualize progress from. If None, defaults to today's date.
    program_start_date : str or Python datetime object, optional
        Start date of UBC MDS Program. If None, defaults to the configured start date defined in config.py as PROGRAM_CONFIG_2025_2026['program_start']. 
    program_end_date : str or Python datetime object, optional
        End date of UBC MDS Program. If None, defaults to configured end date defined in config.py as PROGRAM_CONFIG_2025_2026['program_end']. 
    capstone_start_date : str or Python datetime object, optional
        Start date of UBC MDS Capstone Project. If None, defaults to configured start date of the UBC MDS Capstone project in config.py as PROGRAM_CONFIG_2025_2026['capstone']['start']. 
    
    Returns
    -------
    None
        This function displays a bar chart visualizing progress toward the
        capstone and the end of the program. The figure is then saved to the `img/`
        directory with the current date appended to the filename. 

    Examples
    --------
    >>> visualize_program_progress()
    Displays and saves bar chart with progress towards the capstone and end of the program from today's date.

    >>> visualize_program_progress('January 1, 2026', 
    ...                             'August 26, 2025', 
    ...                             'June 30, 2026', 
    ...                             'April 24, 2026'
                                )
    Displays and saves bar chart with progress towards the capstone start date (April 24, 2026) and end of the program (June 30, 2026) from today's date (August 26, 2025).
    """
    pass 
