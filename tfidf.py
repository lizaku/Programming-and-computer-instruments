import os
import re
from math import log

punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'

def preprocessing(text): # функция предобработки текста
    text_wo_punct = re.sub(punct, '', text.lower()) # удаляем пунктуацию, приводим в нижний регистр
    words = text_wo_punct.strip().split() # делим по пробелам
    return words

def count_tf(word, text):
    i = 0
    for w in text:
        if w == word:
            i += 1
    #i = text.count(word)
    tf = i / len(text)
    return tf


def count_df(word, texts):
    i = 0
    #for text in texts:
    #    for w in text:
    #        if w == word:
    #            i += 1
    #            break
    i = [1 for text in texts if word in text]
    df = sum(i)
    return df


def count_idf(word, texts):
    df = count_df(word, texts)
    idf = len(texts)/ (1 + df)
    return idf


def count_tfidf(word, text, texts):
    tf = count_tf(word, text)
    idf = count_idf(word, texts)
    tfidf = log(tf, 10) * log(idf, 10)
    return tfidf
    

def main():
    for root, dirs, files in os.walk('wikipedia'):
        texts = {}
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='utf-8') as t:
                content = t.read()
                text = preprocessing(content)
                texts[f] = text
    raw_texts = list(texts.values())
    for text in texts:
        dic_tfidf = {}
        for word in texts[text]:
            if word in dic_tfidf:
                continue
            tfidf = count_tfidf(word, texts[text], raw_texts)
            dic_tfidf[word] = tfidf
        print('Ключевые слова для текста {}:'.format(text))
        i = 0
        for el in sorted(dic_tfidf, key=lambda x: dic_tfidf[x]):
            print(el, dic_tfidf[el])
            i += 1
            if i > 3:
                break

#main()
if __name__ == '__main__':
    main()
