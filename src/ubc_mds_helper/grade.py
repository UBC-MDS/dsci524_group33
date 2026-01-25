"""
Grade calculator for UBC MDS courses.

This module contains functions that help students estimate the minimum grades
needed on remaining course components to finish with at least 60%.

Author: Michael Kmetiuk
Date: January 9, 2026
"""


def needed_to_pass(course_type: str, grades: dict) -> dict:
    """
    Compute the minimum equal grade needed on all remaining components to pass (>= 60%).

    The function supports two grading schemes:

    - **quiz**: 4 labs (12.5% each) and 2 quizzes (25% each)
    - **project**: 4 milestones (20% each) and 4 individual assignments (5% each)

    Parameters
    ----------
    course_type : str
        Course grading scheme. Must be `"quiz"` or `"project"`.
    grades : dict
        Dictionary mapping completed component names to earned grades (0 - 100).

        Example:
        `{"lab1": 80, "quiz1": 70}`

    Returns
    -------
    dict
        Dictionary mapping each remaining component to the minimum grade required
        on that component to reach at least 60%.

        The same minimum grade is applied to all remaining components.

    Raises
    ------
    ValueError
        If `course_type` is invalid.
        If a component name is unknown.
        If a grade is outside the range 0 - 100.
        If it is mathematically impossible to pass.
    TypeError
        If `grades` is not a dictionary.
        If any key is not a string or value is not numeric.

    Examples
    --------
    Quiz-based course with two labs and one quiz completed:

    >>> needed_to_pass("quiz", {"lab1": 80, "lab2": 70, "quiz1": 60})
    {'lab3': 52.5,
     'lab4': 52.5,
     'quiz2': 52.5}

    Project-based course with one milestone completed:

    >>> needed_to_pass("project", {"Milestone1": 80})
    {'Milestone2': 55.0,
     'Milestone3': 55.0,
     'Milestone4': 55.0,
     'IndividualAssignment1': 55.0,
     'IndividualAssignment2': 55.0,
     'IndividualAssignment3': 55.0,
     'IndividualAssignment4': 55.0}
    """
    if course_type not in {"quiz", "project"}:
        raise ValueError("course_type must be 'quiz' or 'project'")
    if not isinstance(grades, dict):
        raise TypeError("grades must be a dictionary")

    quiz_weights = {
        "lab1": 0.125,
        "lab2": 0.125,
        "quiz1": 0.25,
        "lab3": 0.125,
        "lab4": 0.125,
        "quiz2": 0.25,
    }
    project_weights = {
        "IndividualAssignment1": 0.05,
        "Milestone1": 0.2,
        "IndividualAssignment2": 0.05,
        "Milestone2": 0.2,
        "IndividualAssignment3": 0.05,
        "Milestone3": 0.2,
        "IndividualAssignment4": 0.05,
        "Milestone4": 0.2,
    }

    if course_type == "quiz":
        weights = quiz_weights
    elif course_type == "project":
        weights = project_weights

    earned = 0.0
    for key, value in grades.items():
        if not isinstance(key, str):
            raise TypeError("component name must be a string")
        if not isinstance(value, (int, float)):
            raise TypeError("component grade must be a number")
        if key not in weights:
            raise ValueError(f"Unknown component: {key}")
        if value < 0 or value > 100:
            raise ValueError("component grade must be between 0 and 100")
        earned += weights[key] * value

    remaining = []
    for component in weights:
        if component not in grades:
            remaining.append(component)

    remaining_weight = 0.0
    for component in remaining:
        remaining_weight += weights[component]

    if remaining_weight == 0:
        return {}

    points_needed = 60.0 - earned
    if points_needed <= 0:
        result = {}
        for component in remaining:
            result[component] = 0
        return result
    needed_grade = points_needed / remaining_weight

    if needed_grade > 100:
        raise ValueError("It is mathematically impossible to pass")

    result = {}
    for component in remaining:
        result[component] = needed_grade

    return result
