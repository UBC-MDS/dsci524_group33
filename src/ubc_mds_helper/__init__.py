# MIT License
#
# Copyright (c) 2026 Jasjot Parmar, Ian Gault, Michael Kmetiuk, Valeria Siciliano
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Expose functions from each module in src/ubc_mds_helper (from assessments.py, config.py, grade.py, helper_functions.py, progress.py, and status.py).
Allows the user to import functions from src/ubc_mds_helper without knowing the internal file structure.
Example: Instead of from ubc_mds_helper.grade import needed_to_pass, user can instead import:  from ubc_mds_helper import needed_to_pass
"""
from .assessments import late_assignment
from .config import PROGRAM_CONFIG_2025_2026
from .grade import needed_to_pass
from .helper_functions import normalize_date, progress_percentage
from .progress import visualize_program_progress
from .status import status

__all__ = [
    'late_assignment',
    'PROGRAM_CONFIG_2025_2026',
    'needed_to_pass',
    'normalize_date',
    'progress_percentage',
    'visualize_program_progress',
    'status'
    ]