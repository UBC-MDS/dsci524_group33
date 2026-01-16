import pytest
from ubc_mds_helper.grade import needed_to_pass

def test_invalid_course_type():
    with pytest.raises(ValueError, match = "course_type"): #match suggested by ChatGPT
        needed_to_pass("capstone", {"lab1":60})