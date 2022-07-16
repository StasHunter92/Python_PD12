from random import choice

# declaring variables
answers_list = []


def morse_encode(word):
    """
    Return word encoded by morse alphabet
    """
    morse_word_list = []
    morse_alphabet = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }
    word = word.replace(" ", "")
    word_list = list(word)
    for letter in word_list:
        morse_word_list.append(morse_alphabet[letter])
    morse_word_result = " ".join(morse_word_list)
    return morse_word_result


def get_word():
    """
    Return random word from list
    """
    words = ["sos", "life", "health", "python", "developer", "well done"]
    word = choice(words)
    return word


def print_statistics(answers):
    """
    Return detailed statistics for answers
    """
    tasks_count = len(answers)
    correct_answers = answers.count(True)
    incorrect_answers = answers.count(False)
    statistics = \
        f"Всего задачек: {tasks_count}" \
        f"\nОтвечено верно: {correct_answers}" \
        f"\nОтвечено неверно: {incorrect_answers}"
    return statistics


def main():
    print(f"Сегодня мы потренируемся расшифровывать азбуку Морзе"
          f"\nНажмите Enter и начнем")
    input()
    for i in range(1, 6):
        random_word = get_word()
        morse_word = morse_encode(random_word)
        print(f"Слово {i}: {morse_word}")
        answer = input("Введите ответ: ").lower().strip()
        if answer == random_word:
            print(f"Верно, {random_word}!\n")
            answers_list.append(True)
        else:
            print(f"Неверно, {random_word}!\n")
            answers_list.append(False)
    result = print_statistics(answers_list)
    print(result)


if __name__ == "__main__":
    main()
