import pytest
from ubc_mds_helper.grade import needed_to_pass

def test_invalid_course_type():
    with pytest.raises(ValueError, match = "course_type"):
        needed_to_pass("capstone", {"lab1":60})

def test_grade_not_dict():
    with pytest.raises(TypeError, match = "grades"): 
        needed_to_pass("quiz", 50)
def test_unknown_component():
    with pytest.raises(ValueError):
        needed_to_pass("project", {"Milestone5":60})  
def test_out_of_range_grade():
    with pytest.raises(ValueError):
        needed_to_pass("project", {"Milestone1":120})  