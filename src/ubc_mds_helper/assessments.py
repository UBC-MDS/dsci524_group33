"""
The function prints the submission status of a lower-stake and
higher-stake assignment, the updated count, and the
scaling factor applied, and returns the scaled grade, following the
UBC MDS policy.

Author: Valeria Siciliano

Date: January 9, 2026
"""


def late_assignment(raw_grade, late_count, is_lower_stakes=False):
    """
    This function evaluates a late submission according to the program policy.
    For higher-stakes assessments, the grade is scaled based on the cumulative
    number of late submissions. For lower-stakes assessments, late submissions
    are not accepted and receive a grade of zero.


    Parameters
    ----------
    raw_grade : float or int
        The original grade before applying any late-submission penalty.
    late_count : int
        The number of late submissions prior to this one.
    is_lower_stakes : bool, optional
        Indicates whether the assessment is lower-stakes. If True, the late
        submission is not accepted and receives zero points. Default is False.

    Returns
    -------
    float
        The final grade after applying the late-submission scaling.

    Notes
    -----
    Late submissions for higher-stakes assessments follow this policy:
    - 1st late submission: 75% of the original grade
    - 2nd–5th late submissions: 50% of the original grade
    - 6th or later: 0 points

    Late submissions for lower-stakes assessments do not count toward the
    cumulative late count and always receive 0 points.

    Examples
    --------
    Higher-stakes assignment, first late submission:
    >>> late_assignment(80, 0)
    Status: Late (1st occurrence)
    Late count: 1
    Scaling factor: 0.75
    60.0

    Lower-stakes assignment, any late submission:
    >>> late_assignment(90, 2, is_lower_stakes=True)
    Status: Late not accepted (lower-stakes)
    Late count: 2
    Scaling factor: 0.0
    0.0
    0.0
    """

    if late_count < 0:
        raise ValueError("late_count must be a non-negative integer.")
    if raw_grade < 0:
        raise ValueError("raw_grade must be non-negative.")
    if is_lower_stakes:
        scaling = 0.0
        status = "Late not accepted (lower-stakes)"
    else:
        late_count += 1
        if late_count == 1:
            scaling = 0.75
            status = "Late (1st occurrence)"
        elif late_count <= 5:
            scaling = 0.50
            status = "Late (2nd–5th occurrence)"
        else:
            scaling = 0.0
            status = "Late (6+ occurrence)"

    print(f"Status: {status}")
    print(f"Late count: {late_count}")
    print(f"Scaling factor: {scaling}")

    return raw_grade * scaling
