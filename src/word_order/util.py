import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def count_word_occurrences():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    distinct_words = len(word_count)
    occurrences = ' '.join(map(str, word_count.values()))

    return distinct_words, occurrences
distinct_words, occurrences = count_word_occurrences()
logging.debug(distinct_words)
logging.debug(occurrences)