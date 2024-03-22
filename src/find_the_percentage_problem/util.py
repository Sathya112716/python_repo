# util.py
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calc_average(n,student_input,query_name):
    student_marks={}

    for _ in range(n):
        name, *marks = student_input[_].split()
        scored_value= list(map(float, marks))
        student_marks[name] = scored_value

    if query_name in student_marks:
        average = sum(student_marks[query_name]) / len(student_marks[query_name])
        return f"{average:.2f}"
    else:
        return "Student not there"

