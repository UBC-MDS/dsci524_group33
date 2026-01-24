"""
Test script for the assessment.py function

Author: Valeria 

Date: January 15, 2026
"""

from ubc_mds_helper.assessments import late_assignment


def test_lower_stakes_assignment():
    """Test that lower-stakes late submissions receive zero."""
    grade = late_assignment(raw_grade=80, late_count=2, is_lower_stakes=True)
    assert grade == 0.0

def test_first_late_high_stakes():
    """Test that the first late submission for higher-stakes is scaled to 75%."""
    grade = late_assignment(raw_grade=100, late_count=0, is_lower_stakes=False)
    expected_grade = 75.0
    assert grade == expected_grade 

def test_fifth_late_high_stakes():
    """Test that the fifth late submission for higher-stakes is scaled to 50%."""
    grade = late_assignment(raw_grade=90, late_count=4, is_lower_stakes=False)
    expected_grade = 45.0
    assert grade == expected_grade

def test_sixth_late_high_stakes():
    """Test that the sixth late submission for higher-stakes receives zero."""
    grade = late_assignment(raw_grade=70, late_count=5, is_lower_stakes=False)
    expected_grade = 0.0
    assert grade == expected_grade

def test_negative_late_count_raises_error():
    """Test that a negative late count raises a ValueError."""
    try:
        late_assignment(raw_grade=85, late_count=-1, is_lower_stakes=False)
        assert False, "Expected ValueError for negative late_count"
    except ValueError:
        pass
    
def test_raw_grade_out_of_bounds_raises_error():
    """Test that raw grades out of bounds raise a ValueError."""
    try:
        late_assignment(raw_grade=110, late_count=1, is_lower_stakes=False)
        assert False, "Expected ValueError for raw_grade > 100"
    except ValueError:
        pass

    try:
        late_assignment(raw_grade=-10, late_count=1, is_lower_stakes=False)
        assert False, "Expected ValueError for raw_grade < 0"
    except ValueError:
        pass

