import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def merge_the_tools(string, k):
    n = len(string)
    substrings = [string[i:i + k] for i in range(0, n, k)]

    for substring in substrings:
        unique_chars = []
        for char in substring:
            if char not in unique_chars:
                unique_chars.append(char)
        result=''.join(unique_chars)
        logging.debug(result)
    return result
