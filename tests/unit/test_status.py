import pytest 
from datetime import date

from ubc_mds_helper.status import status
from ubc_mds_helper.config import PROGRAM_CONFIG_2025_2026
from ubc_mds_helper.helper_functions import progress_percentage

# test that function raises an error if one of the dates passed in are not a date object or string
# got syntax help with validating the exception message from the Assertions about expected exceptions section from PyTest docs: https://docs.pytest.org/en/7.1.x/how-to/assert.html
def test_non_date_str_parameter():
    with pytest.raises(TypeError) as exception_info:
        status(PROGRAM_CONFIG_2025_2026, 12345)
        
    # make sure the exception message matches our exception message passed in 
    assert "must be a Python datetime.date or str object" in str(exception_info.value)

def test_special_block1_week1():
    result = status(PROGRAM_CONFIG_2025_2026, "Aug 29, 2025")
    assert result['block'] == 1
    assert result['week_in_block'] == 1

def test_out_of_bounds():
    with pytest.raises(ValueError) as exception_info:
        status(PROGRAM_CONFIG_2025_2026, "Jan 10, 2023")

    # make sure the exception message matches our exception message passed in
    assert "Entered date is not within the 2025-2026 MDS program cycle" in str(
        exception_info.value
    )

def between_block_test():
    result = status(PROGRAM_CONFIG_2025_2026, "Feb 7, 2026")
    assert result['block'] == None
    assert result['week_in_block'] == None
    assert result['between_blocks'] == True

def test_today():
    result = status(PROGRAM_CONFIG_2025_2026)
    assert result['date'] == date.today()

# NOTE: asked ChatGPT5 how to get up an integration function based on unit tests and main function
def test_status_integration():
    result = status(PROGRAM_CONFIG_2025_2026, "Oct 20, 2025")
    assert result["block"] == 2
    assert result["week_in_block"] == 3
    assert result["during_break"] is False
    assert result["break_name"] is None
    assert result["days_until_next_break"] == 19
    assert result["next_break_name"] == "Fall break"
