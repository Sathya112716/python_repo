import logging #import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def mutate_string():
    s = input("").strip()
    position, character = input("").split()
    position = int(position)

    return s[:position] + character + s[position + 1:]
logging.debug(mutate_string())




