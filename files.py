with open('text1.txt', 'w', encoding='utf-8') as f:
    f.write("Привет, мир!")

with open('text.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.upper()
        print(line)

#Задание из слайдов

def count_words(filename):
 
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    return words
 
 
def changer(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace(".", "!")
    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    return f'Файл создан, знаки препинания . заменены на !'

 
def main():
        words = count_words('referat.txt')
        res = changer('referat.txt')
        print(f'Кол-во слов: {len(words)}')
        print(res)
 
 
if __name__ == "__main__":
    main()