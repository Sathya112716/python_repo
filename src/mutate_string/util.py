import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def mutate_string(s, position, character):
    s = input("Enter the string").strip()
    position, character = input("Enter the character and position").split()
    position = int(position)

    return s[:position] + character + s[position + 1:]




