import csv
import datetime
import seaborn as sns; sns.set()
import pandas as pd
import matplotlib.pyplot as plt

from polyglot.text import Text


with open('../CSV Cleaner/g1_clean.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    next(reader)
    pos = 0
    neg = 0
    neutral = 0
    total = 0
    for rows in reader:
        text = Text(rows[2])
        total += 1
        print(rows)
        '''if text.polarity > 0:
            sentiment = 1
            pos += 1
        elif text.polarity < 0:
            sentiment = -1
            neg += 1
        else:
            sentiment = 0
            neutral += 1'''
        #print("Nome:", rows[0].replace("'", ""), "| Data:", rows[1], "| Sentiment:", sentiment)
        try:
            date = datetime.datetime.strptime(rows[1], "%Y-%m-%dT%H:%M:%S")
        except:
            pass
        try:
            date = datetime.datetime.strptime(rows[1], "%d-%m-%Y %H:%M:%S")
        except:
            pass
        #print("Year:", date.year)

    #print("Sentiment Positive: ", pos, "| Sentiment Negative: ", neg, "| Sentiment Neutral: ", neutral)

'''
    plt.plot(date.month, pos, marker = 'o', color = 'blue', linestyle = '--')
    #plt.plot(date.month, costs, marker='s', color='red')

    # plt.title -> título do gráfico
    # plt.xlabel -> rótulo do eixo x
    # plt.ylabel -> rótulo do eixo y
    plt.title("Positive Sentiment x Month")
    plt.xlabel("Month")
    plt.ylabel("Total")

    plt.legend(["All Years"], loc=4)

    plt.show()
'''