"""
Test script for the grade.py function

Author: Michael Kmetiuk

Date: January 15, 2026
"""

import pytest
from ubc_mds_helper.grade import needed_to_pass


def test_invalid_course_type():
    """Ensure a ValueError is raised when an invalid course type is provided."""
    with pytest.raises(ValueError, match="course_type"):
        needed_to_pass("capstone", {"lab1": 60})


def test_grade_not_dict():
    """Ensure a TypeError is raised when grades is not provided as a dictionary."""
    with pytest.raises(TypeError, match="grades"):
        needed_to_pass("quiz", 50)


def test_unknown_component():
    """Ensure a ValueError is raised when an unknown component is given for the selected course type."""
    with pytest.raises(ValueError):
        needed_to_pass("project", {"Milestone5": 60})


def test_out_of_range_grade():
    """Ensure a ValueError is raised when a grade is outside the valid range of 0 to 100."""
    with pytest.raises(ValueError):
        needed_to_pass("project", {"Milestone1": 120})


def test_quiz_math_case():
    """Verify correct required grades are computed for a quiz-based course with one submitted lab."""
    result = needed_to_pass("quiz", {"lab1": 80})
    expected = pytest.approx(57.142857, abs=1e-3)
    for k in ["lab2", "lab3", "lab4", "quiz1", "quiz2"]:
        assert result[k] == expected


def test_project_milestone_math_case():
    """Verify correct required grades are computed for a project-based course with one milestone submitted."""
    result = needed_to_pass("project", {"Milestone1": 80})
    expected = pytest.approx(55.0, abs=1e-3)

    for k in [
        "Milestone2",
        "Milestone3",
        "Milestone4",
        "IndividualAssignment1",
        "IndividualAssignment2",
        "IndividualAssignment3",
        "IndividualAssignment4",
    ]:
        assert result[k] == expected


def test_impossible_to_pass():
    """Ensure a ValueError is raised when it is mathematically impossible to reach a passing grade."""
    with pytest.raises(ValueError):
        needed_to_pass("quiz", {"lab1": 5, "lab2": 10, "quiz1": 5, "lab3": 10})
