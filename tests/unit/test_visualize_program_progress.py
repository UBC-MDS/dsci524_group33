"""
Test script for the progress.py function

Author: Jasjot Parmar

Date: January 15, 2026
"""

import sys 
import os 
import pytest 
from datetime import date

from ubc_mds_helper.progress import visualize_program_progress
from ubc_mds_helper.config import PROGRAM_CONFIG_2025_2026
from ubc_mds_helper.helper_functions import progress_percentage

# test that function raises an error if one of the dates passed in are not a date object or string
# got syntax help with validating the exception message from the Assertions about expected exceptions section from PyTest docs: https://docs.pytest.org/en/7.1.x/how-to/assert.html
def test_non_date_str_parameter():
    with pytest.raises(TypeError) as exception_info:
        visualize_program_progress(
        date.today(), 
        'August 26, 2025', 
        'June 30, 2026', 
        1
    )
        
    # make sure the exception message matches our exception message passed in 
    assert "must be a Python datetime.date or str object" in str(exception_info.value)

# when the current date is equal to the program start date, the program and capstone progress should return 0
def test_curr_date_equals_end():
    capstone_progess_percentage, completion_percentage = visualize_program_progress(current_date = PROGRAM_CONFIG_2025_2026['program_start'])

    # capstone_progress_percentage AND completion_percentage should both return 0, as if the current date is set to the program start date, there are 0 elapsd days 
    assert capstone_progess_percentage == 0 
    assert completion_percentage == 0 

# when the currnt date is equal to the capstone start date, capstone progress should be 1
def test_curr_date_equals_capstone():
    capstone_progess_percentage, completion_percentage = visualize_program_progress(current_date = PROGRAM_CONFIG_2025_2026['capstone']['start'])

    # capstone_progress_percentage AND completion_percentage should both return 0, as if the current date is set to the program start date, there are 0 elapsd days 
    assert capstone_progess_percentage == 1
    assert completion_percentage < 1

# when the current date is equal to the program end date, the program progress should be 1 and the capstone start date should be 1 as we clipped these values to be [0, 1]
def test_curr_date_equals_program_end():
    capstone_progess_percentage, completion_percentage = visualize_program_progress(current_date = PROGRAM_CONFIG_2025_2026['program_end'])

    # capstone_progress_percentage AND completion_percentage should both return 0, as if the current date is set to the program start date, there are 0 elapsd days 
    assert capstone_progess_percentage == 1
    assert completion_percentage == 1

# when the current date is before the program start date, the capstone and program progress should be 0 and not negative
def test_curr_date_before_program_start():
    capstone_progess_percentage, completion_percentage = visualize_program_progress(current_date = 'August 26, 2025') # plug in a current date before the program start date of August, 29, 2025 in config.py

    # capstone_progress_percentage AND completion_percentage should both return 0, as if the current date is set to before the program start date, there are negative elapsd days, which is clipped to [0, 1]
    assert capstone_progess_percentage == 0
    assert completion_percentage == 0

# if there are no dates passed in, the current date should default to today's date and calculate the progress from the default program_start_date, program_end_date, and capstone_start_date in config.py
def test_no_parameters():
    capstone_progess_percentage, completion_percentage = visualize_program_progress()

    # set the current date and grab the program_start_date, program_end_date and capstone_start_date from config 
    current_date = date.today()
    program_start_date = PROGRAM_CONFIG_2025_2026['program_start']
    program_end_date = PROGRAM_CONFIG_2025_2026['program_end']
    capstone_start_date = PROGRAM_CONFIG_2025_2026['capstone']['start']

    # caluclate the manual capstone_progress_percentage and manual completion_percentage from today's date, and the default dates from the config file
    manual_capstone_progress = progress_percentage(
        program_start_date,
        current_date,
        capstone_start_date
    )

    manual_completion_progress = progress_percentage(
        program_start_date,
        current_date,
        program_end_date
    )

    # assert if the manual capstone_progress_percentage and manual completion_percentage are equal to the capstone_progress_percentage and completion_percentage after passing in no paraeeters
    assert manual_capstone_progress == capstone_progess_percentage
    assert manual_completion_progress == completion_percentage
