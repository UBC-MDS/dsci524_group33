# Welcome to ubc_mds_helper

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/ubc_mds_helper.svg)](https://pypi.org/project/ubc_mds_helper/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/ubc_mds_helper.svg)](https://pypi.org/project/ubc_mds_helper/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them.*

## Project Purpose

ubc_mds_helper is a project that helps students in the UBC Masters of Data Science (MDS) program better understand and plan their academic timeline.

The MDS program follows 6 blocks of instruction, each consisting of 4 courses delivered over a standard cycle of 5 weeks. At the end of the 6 blocks, a 2 month capstones project is required to complete the program, resulting in a total program length of 10 months.

With the large number of deadlines and the variability in workload across the 5 weeks within each block, it is difficult for students to get a sense of where they are in the program at a given time. This helper package provides date-based tools to describe a student's academic position, program phase, and progress, and support planning for personal commitments, absences, late submissions, and meeting course-level requirements. 

This helper is based on a program cofiguration for the 2025/2026 cohort, and would need to be adapted for other program cycles.

There is no package that is specific to the MDS program. However, we will be using the python standard library of datetime and calendar to streamline date calculations and interpretations.

### Use case examples

"I have a family committment to go to on December 2-4th, 2025. Am I able to make it work based on positioning in the 6 week cycle?"

"When is the next break for me to plan my holiday?"

"I failed the first quiz, and need to make sure I pass the course. What do I have to get on the second quiz?"

"I already have 2 late assignments. What penalty will I receive on the next late assignment?"

"I'm a visual learner - what is my progress?"

## Functions

1. Status()

- A date and calendar-based Python module that describes position in the UBC MDS program.

2. Late_assignments()

- The function prints the submission status, the updated late count, and the scaling factor applied, and returns the scaled grade.

3. Grade()

- A grade calculator Python module that helps UBC MDS students check what grades they need to get for remaining course components to pass.

4. Progression()

- Visualizes program progress (in %) from a date to the capstone and program end date.

## Cycle Configuration

*config.py*

- Program info to be adjusted based on cohort cycle
- This config file will be an arugment in some of relevant functions so that the hardcoding can be set in the config file and not in the functions themselves.

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install ubc_mds_helper
```

TODO: Add a brief example of how to use the package to this section

To use ubc_mds_helper in your code:

```python
>>> import ubc_mds_helper
>>> ubc_mds_helper.status(config, date="Mar 20, 2026")
```

## Contributors

Valeria Siciliano, Michael Kmetiuk, Ian Gault, Jasjot Parmar, Ian Gault

## Copyright

- Copyright © 2026 Jasjot Parmar, Ian Gault, Michael Kmetiuk, Valeria Siciliano.
- Free software distributed under the [MIT License](./LICENSE).
