# Программа должна читать текст из файла и сообщать, есть ли в тексте хотя бы одна биграмма (два слова, стоящих в тексте друг за другом), встречающаяся больше двух раз. Регистр и знаки препинания нужно не учитывать. В программе хотя бы один раз нужно использовать list comprehensions.

import codecs, re

def open_file(title):
    a = codecs.open(title, 'r', 'utf-8')
    words = [word.strip(' ,.?!-:;').lower() for word in a.read().split()]
    return words

def find_bigramm(words):
    text = ''
    for word in words:
        text += word + ' '
    for x in range(len(words)):
        bigramm = words[x] + ' ' + words[x+1]
        m = re.findall(bigramm, text, flags = re.U)
        if len(m) > 2:
            print(True)
            break

def main():
    f = open_file('text.txt')
    z = find_bigramm(f)

main()
