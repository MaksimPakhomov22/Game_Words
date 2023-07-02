from utils import load_words, change_word, write_history, read_history


history_txt = "history.txt"
words_txt = "words.txt"

print("Введите ваше имя")
user_name = input()
words = load_words(words_txt)
score = 0

for word in words:
    print(change_word(word))
    user_answer = input()
    if user_answer.lower().strip(" ") == word:
        print("Верно! Вы получаете 10 очков")
        score += 10
    else:
        print(f"Неверно! Верный ответ – {word}")

write_history(history_txt, user_name, score)
print(read_history(history_txt))
