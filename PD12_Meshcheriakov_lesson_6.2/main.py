import functions as f


def main():
    words_file = 'words.txt'
    history_file = 'history.txt'
    user_name = input('Введите ваше имя: ')
    words_list = f.reading_words(words_file)
    score = 0
    for word in words_list:
        print(f'\nУгадайте слово: {f.shuffle_word(word)}')
        result = input().lower().strip()
        if result == word:
            print('Верно! Вы получаете 10 очков')
            score += 10
        else:
            print(f'Неверно! Верный ответ - {word}')
    f.append_result(history_file, user_name, score)
    games_count = len(f.return_results(history_file))
    max_score = max(f.return_results(history_file))
    print(f'\nВсего игр сыграно: {games_count}\n'
          f'Максимальный рекорд: {max_score}')


if __name__ == '__main__':
    main()
