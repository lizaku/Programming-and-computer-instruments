# coding: utf-8

import os, re
from pymystem3 import Mystem
m = Mystem()
punct = '@,.:!?"\'()'
re_ana = re.compile('\{.*?\}')

def mystem(sentence):
    sentence = sentence.strip()
    anas = m.analyze(sentence)
    return anas


def convert2brat(text):
    with open(text, 'r', encoding='utf-8') as f:
        lines = []
        with open(text[:-3] + 'ann', 'w', encoding='utf-8') as ann:
            new_text = ''
            t = 0
            a = 0
            position_text = 0
            for line in f:
                position_line = 0
                words = line.split()
                for word in words:
                    print(word, line)
                    if '<' in word or '>' in word:
                        new_word = re_ana.sub('', word)
                        position_line += len(new_word)
                        line = re.sub(re.escape(word), new_word, line)
                        continue
                    start_pos = line.index(word, position_line) + position_text
                    ana = re_ana.findall(word)
                    new_word = re_ana.sub('', word)
                    end_pos = start_pos + len(new_word.strip(punct))
                    if ana != []:
                        anas = ana[0][1:-1].split('|')
                        for an in anas:
                        #lemma = re.findall('[^=]*', an)[0]
                        #print(an, lemma)
                            params = {'T': str(t), 'start': str(start_pos), 'end': str(end_pos), 'a': str(a), 'an': an}
                            ann.write('T{T}\ttag {start} {end}\t\n#{a}\tAnnotatorNotes T{T}\t{an}\n'.format(**params))
                            t += 1
                            a += 1
                    position_line += len(new_word)
                    line = line.replace(word, new_word, 1)
                    #line = re.sub(re.escape(word), new_word, line)
                lines.append(line)
                position_text += len(line)
        with open('new_sample.txt', 'w', encoding='utf-8') as n:
            for line in lines:
                n.write(line)


if __name__ == '__main__':
    text = 'sample_ana.txt'
    convert2brat(text)
