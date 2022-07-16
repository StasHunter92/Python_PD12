# Создаем счетчик верных ответов и пустой словарь
count = 0
answers = {}

# Словари для разных уровней сложности
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
    }

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
    }

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
    }

# Ранг пользователя
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
    }

# Словарь сложности
change_level = {
    'easy': words_easy,
    'medium': words_medium,
    'hard': words_hard
    }

# Выбор сложности
level = input('Выберите уровень сложности (easy / medium / hard): ').lower()
words = change_level[level]

# Перебор по выбранному словарю
for word, translate in words.items():
    answer = input(
        f'{word}, {len(translate)} букв, начинается на {translate[0]}... ')
    if answer == translate:
        print(f'Верно, {word.capitalize()} - это {translate}')
        answers[word] = True
    else:
        print(f'Неверно, {word.capitalize()} - это {translate}')
        answers[word] = False

# Вывод результатов
print(f'\nПравильно отвечены слова:')
for answer, result in answers.items():
    if result:
        print(answer)
        count += 1
print(f'\nНеправильно отвечены слова:')
for answer, result in answers.items():
    if not result:
        print(answer)

# Вывод ранга
print(f'\nВаш ранг:\n{levels[count]}')
