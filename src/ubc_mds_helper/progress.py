"""
A date and calendar-based Python module that helps UBC MDS students check specific 
program level details using UBC MDS specific dates using a config file containing dates.

Author: Jasjot Parmar

Date: January 9, 2026
"""

from datetime import date
from .config import PROGRAM_CONFIG_2025_2026
from .helper_functions import normalize_date, progress_percentage
from pathlib import Path
import matplotlib.pyplot as plt

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
        Date at which to visualize progress from. If None, defaults to today's date.
    program_start_date : str or Python datetime object, optional
        Start date of UBC MDS Program. If None, defaults to the configured start date defined in config.py as PROGRAM_CONFIG_2025_2026['program_start']. 
    program_end_date : str or Python datetime object, optional
        End date of UBC MDS Program. If None, defaults to configured end date defined in config.py as PROGRAM_CONFIG_2025_2026['program_end']. 
    capstone_start_date : str or Python datetime object, optional
        Start date of UBC MDS Capstone Project. If None, defaults to configured start date of the UBC MDS Capstone project in config.py as PROGRAM_CONFIG_2025_2026['capstone']['start']. 
    
    Returns
    -------
    capstone_progress_percentage, completion_percentage : floats
        This function saves a bar chart visualizing progress toward the
        capstone and the end of the program. The figure is saved to the `img/`
        directory with the current date appended to the filename. The function also 
        returns the proportion of progress that is left until the start of the capstone 
        and the end of the program.

    Examples
    --------
    >>> visualize_program_progress()
    Saves bar chart with progress towards the capstone and end of the program from today's date.

    >>> visualize_program_progress('January 1, 2026', 
    ...                             'August 26, 2025', 
    ...                             'June 30, 2026', 
    ...                             'April 24, 2026'
                                )
    Saves bar chart with progress towards the capstone start date (April 24, 2026) and end of the program (June 30, 2026) from today's date (August 26, 2025).
    """

    # if the date passed in are None, retrieve them from PROGRAM_CONFIG_2025_2026 in config.py
    if current_date is None:
        current_date = date.today()

    if program_start_date is None:
        program_start_date = PROGRAM_CONFIG_2025_2026['program_start']

    if program_end_date is None:
        program_end_date = PROGRAM_CONFIG_2025_2026['program_end']

    if capstone_start_date is None:
        capstone_start_date = PROGRAM_CONFIG_2025_2026['capstone']['start']
    
    # normalize the dates that are passed in: if argument is a datetime.date, return date; if string, try to convert it to an accepted datetime format or throw an error 
    current_date = normalize_date(current_date)
    program_start_date = normalize_date(program_start_date)
    program_end_date = normalize_date(program_end_date)
    capstone_start_date = normalize_date(capstone_start_date)
   
    # compute the progress to the capstone and emnd of the program based on current date
    capstone_progress_percentage = progress_percentage(
        program_start_date,
        current_date,
        capstone_start_date
    )

    completion_percentage = progress_percentage(
        program_start_date,
        current_date,
        program_end_date
    )

    labels = ['To Capstone Start', 'To Program End']
    values = [capstone_progress_percentage * 100, completion_percentage * 100]

    fig, ax = plt.subplots(figsize = (9, 4))

    # got help for the plotting approach from: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html
    ax.barh(labels, values) # labels on the y axis (capsone start and program end) and completion % (values) are the bar lengths
    ax.set_xlim(0, 100)
    ax.set_xlabel("Progress (%)")
    ax.set_title("UBC MDS Program Progress")

    # completion line at the end of each bar at x = 100. Got syntax help from: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html and the following to label the text: https://stackoverflow.com/questions/75477749/how-can-i-add-text-to-the-same-position-in-multiple-matplotlib-plots-with-differ
    ax.axvline(100, linestyle = "--", linewidth = 1)
    ax.text(105, -0.75, "Completion", ha = 'right', va = 'center')

    # label the values on each bar (capstone progress percentage and the completion percentage)
    for i, value in enumerate(values):
        ax.text(
            min(value + 1, 99), # add 1 so the text is not overlapping with the bar
            i, 
            f"{value:.1f}%", 
            va = "center"
        )
    
    # add annotations for the current date and program start date 
    ax.text(
        0,
        -0.95, 
        f"Today: {current_date.isoformat()} | Start: {program_start_date.isoformat()}",
        fontsize = 10
    )

    plt.tight_layout()

    # define the directory and the filename to save the graph in 
    output_dir = Path('img')
    output_dir.mkdir(parents = True, exist_ok = True)
    filepath = Path(output_dir) / f'completion_progress_{current_date}.png'

    fig.savefig(filepath)

    return capstone_progress_percentage, completion_percentage

if __name__ == "__main__":
    capstone_progress_percentage, completion_percentage = visualize_program_progress(
        current_date = PROGRAM_CONFIG_2025_2026['program_start']
    )

    print(capstone_progress_percentage, completion_percentage)