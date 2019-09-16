# Вывести последнюю букву в слове
word = 'Архангельск'
def last_letter(word):
    print(f'Последнняя буква в слове {word}: {word[-1]}')

#last_letter(word)


# Вывести количество букв "а" в слове
word = 'Архангельск'

def count_letters(word):
    letters = []
    res = 0
    letters = list(word)
    for letter in letters:
        if letter == 'а':
            res += 1
    print(f'Количество букв \'а\' в слове: {res}')

#count_letters(word)


# Вывести количество гласных букв в слове
word = 'Архангельск'
def vowel(word):
    vowel_list = ['а', 'о', 'у', 'э', 'е', 'ы', 'я', 'и']
    vowel = 0
    word_letters = list(word.lower())
    for vowel_letter in word_letters:
        if vowel_letter in vowel_list:
            vowel += 1

    print(f'Количество гласных букв в слове: {vowel}')

#vowel(word)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
def count_words(sentence):
    words = sentence.split()
    print(f'Количество слов в предложении: {len(words)}')

#count_words(sentence)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
def first_letter(sentence):
    words = sentence.split()
    for i in words:
        print(i[0])

#first_letter(sentence)


# Вывести усреднённую длину слова.
from statistics import mean

sentence = 'Мы приехали в гости'

def average_word_len(sentence):
    words_average_list = []
    words = sentence.split()
    for i in words:
        words_average_list.append(len(i))
    print(f'Средняя длина слова: {mean(words_average_list)}')

#average_word_len(sentence)

if __name__ == '__main__':
    last_letter(word)
    count_letters(word)
    vowel(word)
    count_words(sentence)
    first_letter(sentence)
    average_word_len(sentence)
