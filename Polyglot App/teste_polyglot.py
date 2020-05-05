import polyglot
import csv

from polyglot.text import Text,Word
with open('CommentsG1_2020-03-14T22-15-50.csv', 'r', encoding='utf-8') as entrada:
    ler = csv.reader(entrada)
    next(ler)
    for linha in ler:
        text = Text(linha[2])
        if text.polarity > 0:
            sentiment = 1
            print('Nome: {} Sentiment: {}'.format(linha[0], sentiment))
        elif text.polarity == 0:
            sentiment = 0
            print('Nome: {} Sentiment: {}'.format(linha[0], sentiment))
        else:
            sentiment = -1
            print('Nome: {} Sentiment: {}'.format(linha[0], sentiment))


