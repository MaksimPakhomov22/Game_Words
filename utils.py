import random


def load_words(filename):
    new_lines = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            new_lines.append(line.strip("\n"))
    return new_lines


def change_word(word):
    word = list(word)
    random.shuffle(word)
    return "".join(word)


def write_history(filename, user_name, score):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{user_name} {score}\n")


def read_history(filename):
    max = 0
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            count += 1
            score = int(line.split(' ')[1])
            if score > max:
                max = score
    return f"Всего игр сыграно: {count}\n" \
           f"Максимальный рекорд: {max}"
