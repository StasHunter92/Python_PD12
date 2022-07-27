import random


def reading_words(filename):
    """Return list of words from file"""
    clean_word_list = []
    with open(filename, 'r', encoding='utf-8') as words:
        for read_line in words:
            word_clean = read_line.strip()
            clean_word_list.append(word_clean)
    return clean_word_list


def shuffle_word(word_clean):
    """Return shuffled word"""
    letter_list = list(word_clean)
    random.shuffle(letter_list)
    shuffled_word = ''.join(letter_list)
    return shuffled_word


def append_result(filename, user, final_score):
    """Write result in file"""
    with open(filename, 'a', encoding='utf-8') as history:
        history.write(f'{user} {final_score}\n')


def return_results(filename):
    """Read and return scores list"""
    total_games = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            history_score = line.strip().split()
            total_games.append(history_score[1])
    return total_games
