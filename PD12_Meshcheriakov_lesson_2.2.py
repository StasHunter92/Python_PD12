# Объявление переменных
score = 0
questions_count = 0

# Вывод приветствия
print('''Привет! Предлагаю проверить свои знания английского!
Расскажи, как тебя зовут!''')

# Ввод имени
user_name = input()
print(f'Привет, {user_name}, начинаем тренировку!')

# Алгоритм с вопросами и ответами
print('My name ___ Vova')
first_answer = input('Ответ: ')
if first_answer == 'is':
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
    score += 10
    questions_count += 1
else:
    print('Неправильно.')
    print('Правильный ответ: is')

print('I ___ a coder')
second_answer = input('Ответ: ')
if second_answer == 'am':
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
    score += 10
    questions_count += 1
else:
    print('Неправильно.')
    print('Правильный ответ: am')

print('I live ___ Moscow')
third_answer = input('Ответ: ')
if third_answer == 'in':
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
    score += 10
    questions_count += 1
else:
    print('Неправильно.')
    print('Правильный ответ: in')
  
# Вычисление процентов
question_percent = round(questions_count / 3 * 100)

# Склонение окончания вопросов
if questions_count == 0:
    word_end = 'ов'
elif questions_count == 1:
    word_end = ''
else:
    word_end = 'a'

# Склонение окончания процентов
if question_percent == 33:
    percent_end = 'а'
else:
    percent_end = 'ов'

# Вывод результатов
print(f'''Вот и все, {user_name}!
Вы ответили на {questions_count} вопрос{word_end} из 3 верно.
Вы заработали {score} баллов.
Это {question_percent} процент{percent_end}.''')
