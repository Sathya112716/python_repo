import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

from collections import namedtuple

def calculate_average(students):
    Student = namedtuple('Student', students[0])
    total_marks = sum(float(Student[students[0].index('MARKS')]) for Student in students[1:])
    average = total_marks / (len(students)-1)
    return "{:.2f}".format(average)
