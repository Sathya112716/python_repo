import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def count_word_occurrences(n,words):
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
    n=int(input().strip())
    words=[input().strip() for _ in range(n)]

    distinct_words = len(word_count)
    logging.debug(distinct_words)

    occurences=''.join(map(str,word_count.values()))
    logging.debug(occurences)

