### Reflection notes in exercises.md ###

import pytest
import System as Sys
from System import System
from RestoreData import Restore

# New Tests #

# Test 11
def test_wrong_password(grading_system: System):
    '''Tests for a successful login when an incorrect password is given'''
    Restore()
    username = 'akend3'
    password =  'abc12345'
    grading_system.login(username,password)
    assert grading_system.usr == None


# Test 12 
def test_override_assignment(grading_system: System):
    '''
    Creates an assigment for a given course with the same name.
    Because there is no update_assignment function, I am assuming that being
    able to override information this way would be unintended behavior.
    '''
    Restore()
    username = 'goggins'
    password = 'augurrox'
    new_date = '10/6/22'
    grading_system.login(username, password)
    grading_system.usr.create_assignment('assignment1', new_date,'databases')
    assert new_date != grading_system.courses['databases']['assignments']['assignment1']['due_date']
    
# Test 13
def test_access_illegal_course(grading_system: System):
    '''A professor shouldn't be allowed to add a student to a course they don't teach.'''
    Restore()
    username = 'goggins'
    password = 'augurrox'
    course = 'cloud_computing'
    grading_system.login(username, password)
    grading_system.usr.add_student('akend3', course)
    assert course not in grading_system.users['akend3']['courses']

# Test 14
def test_view_illegal_assignments(grading_system: System):
    '''A student should only be able to view the assignments for a course they are enrolled in'''
    Restore()
    grading_system.login('akend3', '123454321')
    assignments = grading_system.usr.view_assignments('software_engineering')
    assert assignments == None



# Test 15
def test_submit_illegal_assignment(grading_system: System):
    '''A student should only be able to turn in an assignment for a class they are enrolled in'''
    Restore()
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('computer_science', 'assignment1', 'this shouldn\'t work', '1/1/2099')
    


@pytest.fixture
def grading_system():
    gradingSystem = Sys.System()
    gradingSystem.load_data()
    return gradingSystem
