import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def probability_of_letter(length, letters, num_indices):
    total_indices = len(letters)
    count_letter = letters.count('a')
    probability = 1 - ((1 - count_letter / total_indices) ** num_indices)
    return round(probability, 4)
