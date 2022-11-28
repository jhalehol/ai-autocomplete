import os
import json
import sys

TOP_100_WORDS_FILE = '100_top_words'
TOP_1000_WORDS_FILE = '1000_top_words'
TOP_3000_WORDS_FILE = '3000_top_words'
SCORED_WORDS_FILE = 'words_scored'

SCORE_100_WEIGHT = 2
SCORE_1000_WEIGHT = 1
SCORE_3000_WEIGHT = 1

MINIMUM_WORD_LENGTH = 2

def __write_score_words(words_source_path: str):
    words_to_score = __build_words_array(words_source_path)
    if len(words_to_score) <= 0:
        return

    words_scored = __score_words(words_to_score)
    json_content = json.dumps(words_scored)
    os.remove(SCORED_WORDS_FILE)
    with open(SCORED_WORDS_FILE, 'w') as file:
        file.write(json_content)


def __score_words(words: list[str]) -> list[str]:
    top_100 = __build_words_array(TOP_100_WORDS_FILE)
    top_1000 = __build_words_array(TOP_1000_WORDS_FILE)
    top_3000 = __build_words_array(TOP_3000_WORDS_FILE)
    scored_words = []
    for word in words:
        if len(word) > MINIMUM_WORD_LENGTH:
            # Sets default score, then increments it according to occurrences in top words
            score = 1
            score += SCORE_100_WEIGHT if word in top_100 else 0
            score += SCORE_1000_WEIGHT if word in top_1000 else 0
            score += SCORE_3000_WEIGHT if word in top_3000 else 0
            scored_words.append({
                'word': word,
                'score': score
            })

    return scored_words        


def __build_words_array(source_path: str):
    if not os.path.exists(source_path):
        print("File '{}' not found, unable to build words array".format(source_path))
        return None

    with open(source_path, 'r') as file:
        file_content = file.read()
        words = file_content.split('\n')
        file.close()
    
    return words

if __name__ == "__main__":
    """Build an dictionary with words scored according to position in top words

    """
    words_file = sys.argv[1]
    print("Generating words scoring file '{}' using file '{}'".format(SCORED_WORDS_FILE, words_file))
    __write_score_words(words_file)
