### Reflection notes in exercises.md ###

import pytest
import System as Sys
from System import System
from RestoreData import Restore

username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'

# Assigned Tests #

# Test 1. Fail
def test_login(grading_system: System):
    Restore()
    username = 'thtrhg'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)

# Test 2. Pass
def test_check_password(grading_system: System):
    Restore()
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False

# Test 3. Fail
def test_change_grade(grading_system: System):
    Restore()
    grading_system.login('goggins', 'augurrox')
    assigned_grade = 95
    grading_system.usr.change_grade('hdjsr7', 'software_engineering', 'assignment1', assigned_grade)
    grading_system.reload_data()
    grade = grading_system.users['hdjsr7']['courses']['software_engineering']['assignment1']['grade']
    if assigned_grade != grade:
        assert False

# Test 4. Pass
def test_create_assignment(grading_system: System):
    Restore()
    grading_system.login('goggins', 'augurrox')
    new_due_date = '5/20/22'
    assgn_name = 'test_assgn'
    grading_system.usr.create_assignment(assgn_name, new_due_date, 'software_engineering')
    grading_system.reload_data()
    date = grading_system.courses['software_engineering']['assignments'][assgn_name]['due_date']
    if new_due_date != date:
        assert False

# Test 5. Fail
def test_add_student(grading_system: System):
    Restore()
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('akend3', 'software_engineering')
    grading_system.reload_data()
    if 'software_engineering' not in grading_system.users['akend3']['courses'].keys():
        assert False

# Test 6. Pass
def test_drop_student(grading_system: System):
    Restore()
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student('akend3', 'comp_sci')
    grading_system.reload_data()
    if 'comp_sci' in grading_system.users['akend3']['courses'].keys():
        assert False

# Test 7. Pass
def test_submit_assignment(grading_system: System):
    Restore()
    grading_system.login('hdjsr7', 'pass1234')
    course = 'cloud_computing'
    assignment = 'assignment1'
    submission = 'I did this right, right?'
    date = '12/12/21'
    grading_system.usr.submit_assignment(course, assignment, submission, date)
    grading_system.reload_data()
    if submission != grading_system.users['hdjsr7']['courses'][course][assignment]['submission']:
        assert False
    if date != grading_system.users['hdjsr7']['courses'][course][assignment]['submission_date']:
        assert False

# Test 8. Fail
def test_check_ontime(grading_system: System):
    Restore()
    grading_system.login('hdjsr7', 'pass1234')
    course = 'cloud_computing'
    assignment = 'assignment1'
    submission = 'I did this right, right?'
    date = '12/12/99'
    grading_system.usr.submit_assignment(course, assignment, submission, date)
    grading_system.reload_data()
    if grading_system.users['hdjsr7']['courses'][course][assignment]['ontime'] != False:
        assert False
    
# Test 9. Pass
def test_check_grades(grading_system: System):
    Restore()
    grading_system.login('yted91', 'imoutofpasswordnames')
    fn_grades_stud = grading_system.usr.check_grades('software_engineering')
    grading_system.login('goggins', 'augurrox')
    fn_grades_prof = grading_system.usr.check_grades('yted91', 'software_engineering')
    grades = []
    for key in grading_system.users['yted91']['courses']['software_engineering'].keys():
        assgn_grade = grading_system.users['yted91']['courses']['software_engineering'][key]['grade']
        grades.append([key, assgn_grade])

    if len(grades) != len(fn_grades_stud) or len(grades) != len(fn_grades_prof):
        assert False

    for i in range(0, len(grades)):
        if grades[i][0] != fn_grades_stud[i][0]:
            assert False
        if grades[i][1] != fn_grades_stud[i][1]:
            assert False
        if grades[i][0] != fn_grades_prof[i][0]:
            assert False
        if grades[i][1] != fn_grades_prof[i][1]:
            assert False


# Test 10. Fail
def test_view_assignments(grading_system: System):
    Restore()
    grading_system.login('akend3', '123454321')
    given_assgn = grading_system.usr.view_assignments('databases')
    real_assgn = []
    for key in grading_system.courses['databases']['assignments'].keys():
        due_date = grading_system.courses['databases']['assignments'][key]['due_date']
        real_assgn.append([key, due_date])

    if len(real_assgn) != len(given_assgn):
        assert False

    for i in range(0, len(real_assgn)):
        if real_assgn[i][0] != given_assgn[i][0]:
            assert False
        if real_assgn[i][1] != given_assgn[i][1]:
            assert False

@pytest.fixture
def grading_system():
    gradingSystem = Sys.System()
    gradingSystem.load_data()
    return gradingSystem
