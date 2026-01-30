# Welcome to ubc_mds_helper

[![CI](https://github.com/UBC-MDS/dsci524_group33/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/dsci524_group33/actions)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

## Project Purpose

ubc_mds_helper is a project that helps students in the UBC Masters of Data Science (MDS) program better understand and plan their academic timeline.

The MDS program follows 6 blocks of instruction, each consisting of 4 courses delivered over a standard cycle of 5 weeks. At the end of the 6 blocks, a 2 month capstones project is required to complete the program, resulting in a total program length of 10 months.

With the large number of deadlines and the variability in workload across the 5 weeks within each block, it is difficult for students to get a sense of where they are in the program at a given time. This helper package provides date-based tools to describe a student's academic position, program phase, and progress, and support planning for personal commitments, absences, late submissions, and meeting course-level requirements. 

This helper is based on a program configuration for the 2025/2026 cohort, and would need to be adapted for other program cycles.

There is no package that is specific to the MDS program. However, we will be using the python standard library of datetime and calendar to streamline date calculations and interpretations.

### Use case examples

"I have a family commitment to go to on December 2-4th, 2025. Am I able to make it work based on positioning in the 6 week cycle?"

"When is the next break for me to plan my holiday?"

"I failed the first quiz, and need to make sure I pass the course. What do I have to get on the second quiz?"

"I already have 2 late assignments. What penalty will I receive on the next late assignment?"

"I'm a visual learner - what is my progress?"

## Functions

1. status.status()

- A date and calendar-based Python module that describes position in the UBC MDS program.

2. assessments.late_assignment()

- The function prints the submission status, the updated late count, and the scaling factor applied, and returns the scaled grade.


3. grade.needed_to_pass()

- A grade calculator Python module that helps UBC MDS students check what grades they need to get for remaining course components to pass.

4. progress.visualize_program_progress()

- Visualizes program progress (in %) from a date to the capstone and program end date.

## Cycle Configuration

*config.py*

- Program info to be adjusted based on cohort cycle
- This config file will be an argument in some of relevant functions so that the hardcoding can be set in the config file and not in the functions themselves.

## Get started

To install this package for use:

```bash
pip install -i https://test.pypi.org/simple/ ubc-mds-helper
```

To install this package for development:

```bash
git clone https://github.com/UBC-MDS/dsci524_group33.git
cd dsci524_group33
pip install -e ".[tests,dev,docs]"
```
This project uses Hatch to manage environments, run tests, and build documentation
in a reproducible way via `pyproject.toml`.

To create the default development environment:

```bash
hatch env create
```


## To use ubc_mds_helper in your code:

### Our late_assignment function 

This function evaluates a late submission according to the program policy.
For higher-stakes assessments, the grade is scaled based on the cumulative
number of late submissions. For lower-stakes assessments, late submissions
are not accepted and receive a grade of zero.
    
**Inputs**

- `raw_grade` (float or int): The original grade before applying any late-submission penalty.
- `late_count` (int): The number of late submissions prior to this one.
- `is_lower_stakes` (bool): Indicates whether the assessment is lower-stakes. 
    If `True`, the late submission is not accepted and receives zero points. 
    Default is `False`.

Outputs 

The final grade after applying the late-submission scaling. 

```python
>>> from ubc_mds_helper.assessments import late_assignment
>>> late_assignment(80, 0)
```


### Our grade function

This function helps students estimate the minimum grades
needed on remaining course components to finish with at least 60%.


Inputs 
course_type (str) - Course grading scheme. Must be `"quiz"` or `"project"`.
grades (dict) - Dictionary mapping completed component names to earned grades (0 - 100).


Outputs

Dictionary mapping each remaining component to the minimum grade required
on that component to reach at least 60%.

```python
>>> from ubc_mds_helper.grade import needed_to_pass
>>> needed_to_pass("quiz", {"lab1": 80, "lab2": 70, "quiz1": 60})
```

### Our progress.visualize function

This function visualizes program progress (in %) from a date to the capstone and program end date.

Calculates the percentage of elapsed time between the program start date to the capstone start date and program end date
of the UBC MDS program, and visualizes the result as a bar chart.

Inputs:

current_date (str or Python datetime object) - Date at which to visualize progress from. If None, defaults to today's date.
program_start_date (str or Python datetime object) - Start date of UBC MDS Program. If None, defaults to the configured start date defined in config.py as PROGRAM_CONFIG_2025_2026['program_start'].
program_end_date (str or Python datetime object) - End date of UBC MDS Program. If None, defaults to configured end date defined in config.py as PROGRAM_CONFIG_2025_2026['program_end'].
capstone_start_date (str or Python datetime object) - Start date of UBC MDS Capstone Project. If None, defaults to configured start date of the UBC MDS Capstone project in config.py as PROGRAM_CONFIG_2025_2026['capstone']['start'].

Outputs:

capstone_progress_percentage and completion_percentage.
This function saves a bar chart visualizing progress toward the
capstone and the end of the program. The figure is saved to the `img/`
directory with the current date appended to the filename. The function also
returns the proportion of progress that is left until the start of the capstone
and the end of the program.


```python
>>> from ubc_mds_helper.progress import visualize_program_progress
>>> visualize_program_progress(
    current_date="January 1, 2026",
    program_start_date="August 26, 2025",
    program_end_date="June 30, 2026",
    capstone_start_date="April 24, 2026",
)
```

### Our status function

This function returns program status for a given date.

Inputs:

config (config.py) - Contains program date information, block structure, and break periods.
date_input (str or Python datetime object) - Date at which program status is based upon.
If None, defaults to today's date.

Outputs:

Dictionary describing academic position based on date.

```python
>>> from ubc_mds_helper.status import status
>>> from ubc_mds_helper.config import PROGRAM_CONFIG_2025_2026
>>> status(PROGRAM_CONFIG_2025_2026, "March 20, 2026")
```


Extensive documentation for each function including more example uses can be found on our website https://ubc-mds.github.io/dsci524_group33/

## Development environment (conda)

A conda environment is provided for development and testing.

To create the environment:

```bash
conda env create -f environment.yml
```

```bash
conda activate ubc_mds_helper
```



### Running Tests

To run the full test suite with coverage reporting:
```bash
hatch run test:run
```

### Code Style

The project uses ruff for formatting.

To check formatting

```bash
ruff check .
```

To format files: 

```bash
ruff format .
```

## Documentation

### Build documentation locally

To generate the API reference pages using quartodoc:

```bash
quartodoc build --verbose
```

To render and preview the documentation:
```bash
quarto render
```
To preview the documentation locally:
```bash
quarto preview
```


## Continuous Integration

All tests, formatting checks, and documentation builds are automatically run
using GitHub Actions on pull requests and merges to `main`.

## Contributors

Valeria Siciliano, Michael Kmetiuk, Ian Gault, Jasjot Parmar.

Contributors are expected to follow the guidelines outlined in **[CONTRIBUTING.md](./CONTRIBUTING.md)**. Please review this document before submitting issues or pull requests.

## Copyright

- Copyright © 2026 Jasjot Parmar, Ian Gault, Michael Kmetiuk, Valeria Siciliano.
- Free software distributed under the [MIT License](./LICENSE).
