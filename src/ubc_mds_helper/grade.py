"""
A grade calculator Python module that helps UBC MDS students check what grades they need to get for remaining course components to pass.

Author: Michael Kmetiuk

Date: January 9, 2026
"""


def needed_to_pass(course_type: str, grades: dict) -> dict:
    """
    Calculate the minimum grades required on all remaining graded components
    for a student to achieve a final grade of 60% and pass the course.
    Has two distinct grading schemes for quiz and project based courses.

    Parameters
    ----------
    course_type : str
        The type of course. Must be input as "quiz" or "project".

        - "quiz": Course with 4 labs worth 12.5% each and 2 quizes worth 25% each
        - "project": Course with 4 milestones worth 20% each and 4 individual assignments worth 5% each
    grades : dict
        A dictionary of submitted compon4ents and their related grades.

        Example:
        {
            "lab1": 85,
            "lab2: 66,
            "quiz1": 72
        }

    Returns
    -------
    dict
        A dictionary of each remaining graded component and their respective grades required
        to finish the course with at least 60%. We compute equal minimum grades for all remaining assignments needed to pass.

        Example:
        {
            "lab3": 61.5,
            "lab4": 61.5,
            "quiz2": 61.5
        }


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
