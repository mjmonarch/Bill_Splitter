def grades(x):
    correct_grades = ['A', 'B', 'C', 'D', 'F']
    assert x in correct_grades
    return f"You have got {x}"
