# Объявление переменных
questions_count = 0
questions = ['My name ___ Vova', 'I ___ a coder', 'I live ___ Moscow',
             'I ___ cookies']
answers = ['is', 'am', 'in', 'like']

# Вывод приветствия
print('''Привет! Предлагаю проверить свои знания английского!
Наберите "ready", чтобы начать!''')

# Проверка готовности играть
game_ready = input()
if game_ready == 'ready':

    # Алгоритм с вопросами и ответами
    for i in range(len(questions)):
        print(f'{questions[i]}')
        answer = input('Ответ: ')
        if answer == answers[i]:
            print('Ответ верный!')
            questions_count += 1
        else:
            print(f'Неправильно. Правильный ответ: {answers[i]}')

    # Вычисление процентов
    question_percent = round(questions_count / len(questions) * 100)

    # Склонение окончания вопросов
    if questions_count == 0:
        word_end = 'ов'
    elif questions_count == 1:
        word_end = ''
    else:
        word_end = 'a'

    # Вывод результатов
    print(f'''Вот и все!
Вы ответили на {questions_count} вопрос{word_end} из {len(questions)} верно.
Это {question_percent} процентов.''')

# Завершение работы, если пользователь не готов играть
else:
    print(f'Кажется, вы не хотите играть. Очень жаль.')
