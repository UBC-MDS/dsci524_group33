def needed_to_pass(course_type: str, grades: dict) -> dict:
    """
    Calculate the minimum grades required on all remaining graded components
    for a student to achieve a final grade of 60% and pass the course.
    Has two distinct grading schemes for quiz and project based courses.

    Parameters
    ----------
    course_type : str
        The type of course. Must be input as "quiz" or "project".

        - "quiz": Course with 4 labs worth 12% each, 2 quizes worth 25% each and iclicker worth 2%
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
    pass