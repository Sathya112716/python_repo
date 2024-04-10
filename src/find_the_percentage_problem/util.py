# util.py
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calc_average():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *marks = input().split()
        student_marks[name] = list(map(float, marks))
    query_name = input()
    marks = student_marks.get(query_name)
    average = sum(marks) / len(marks)
    result = "{:.2f}".format(average)
    logging.debug(result)