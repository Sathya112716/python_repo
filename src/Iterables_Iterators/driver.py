import logging

from util import probability_of_letter


length = int(input())
letters = input().split()
num_indices = int(input())

result = probability_of_letter(length, letters, num_indices)
logging.debug(result)
