import csv
from polyglot.text import Text


with open('../CSV Cleaner/g1_clean.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    next(reader)
    for rows in reader:
        text = Text(rows[2])
        if(text.polarity > 0):
            sentiment = 1
        elif(text.polarity < 0):
            sentiment = -1
        else:
            sentiment = 0
        print("Nome: ", rows[0], "Sentiment: ", sentiment)




