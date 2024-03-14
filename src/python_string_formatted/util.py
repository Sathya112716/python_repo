import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        formatted_decimal = decimal.rjust(width)
        formatted_octal = octal.rjust(width)
        formatted_hexadecimal = hexadecimal.rjust(width)
        formatted_binary = binary.rjust(width)

        logging.debug(f"{formatted_binary} {formatted_octal}{formatted_hexadecimal}{formatted_decimal}")