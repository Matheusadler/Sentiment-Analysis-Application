import csv
import datetime

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
        if text.polarity > 0:
            sentiment = 1
            pos += 1
        elif text.polarity < 0:
            sentiment = -1
            neg += 1
        else:
            sentiment = 0
            neutral += 1
        print("Nome:", rows[0].replace("'", ""), "| Data:", rows[1], "| Sentiment:", sentiment)
        try:
            date = datetime.datetime.strptime(rows[1], "%Y-%m-%dT%H:%M:%S")
        except:
            pass
        try:
            date = datetime.datetime.strptime(rows[1], "%d-%m-%Y %H:%M:%S")
        except:
            pass
        print("Year:", date.year)

    print("Sentiment Positive: ", pos, "| Sentiment Negative: ", neg, "| Sentiment Neutral: ", neutral)
