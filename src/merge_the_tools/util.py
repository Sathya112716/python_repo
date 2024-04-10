import logging #import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def merge_the_tools():
    s = input().strip()
    k = int(input().strip())
    n = len(s)
    result = []
    for i in range(0, n, k):
        sub_string = s[i:i + k]
        unique_chars = []
        for char in sub_string:
            if char not in unique_chars:
                unique_chars.append(char)
        result.append(''.join(unique_chars))
    return '\n'.join(result)
logging.debug(merge_the_tools())



