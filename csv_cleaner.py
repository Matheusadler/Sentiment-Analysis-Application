import pandas as pd
import icu
import csv
import seaborn as sns
from polyglot.text import Text
import matplotlib.pyplot as plt

# Load csv
data = pd.read_csv('CommentsG1_2020-07-01T14-30-09.csv', error_bad_lines=False, delimiter="*")

# Convert to list
coment = [str(x).replace("[", "").replace("]", "") for x in data.values]

# Insert initial line
coment.insert(0, 'Author,Published,Comment,Likes,Dislikes,Article,Keyword')

sentiment = []
# Save file as csv
with open('g1_clean.csv', 'w') as f:
    for item in coment:
        # sentiment.append(1)
        f.write("%s\n" % item)

# Load new csv
test = pd.read_csv('g1_clean.csv', encoding='latin-1', error_bad_lines=False)

for row in test['Comment'].values:
    text = Text(row)
    if text.polarity > 0:
        sentiment.append(1)
    elif text.polarity < 0:
        sentiment.append(-1)
    else:
        sentiment.append(0)

#Adcionar a coluna ano

test['Published'] = pd.to_datetime(test['Published'])
test['Year'] = test['Published'].dt.year
test['Month'] = test['Published'].dt.month
test['Day'] = test['Published'].dt.day
test['Sentiment'] = sentiment

#Salvando novo CSV
test.to_csv('g1_clean.csv')

#Comandos para acessar anos/meses especificos
#data_2014 = test[test['Year']==2014]
#data_janeiro = test[test['Month']=='January']
#data_sentiment_2014 = test[(test['Year']==2014) & (test['Sentiment']==1)]

month = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# 2013
total_sent_2013 = []
for i in range(12):
    data_2013 = test[(test['Year'] == 2013) & (test['Sentiment'] == -1) & (test['Month'] == i+1)]
    data_sentiment = test[(test['Year'] == 2013) & (test['Month'] == i+1)]
    total_pos_by_month = data_2013['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2013.append(percent)

#2014
total_sent_2014 = []
for i in range(12):
    data_2014 = test[(test['Year'] == 2014) & (test['Sentiment'] == -1) & (test['Month'] == i+1)]
    data_sentiment = test[(test['Year'] == 2014) & (test['Month'] == i+1)]
    total_pos_by_month = data_2014['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2014.append(percent)

#2015
total_sent_2015 = []
for i in range(12):
    data_2015 = test[(test['Year'] == 2015) & (test['Sentiment'] == -1) & (test['Month'] == i+1)]
    data_sentiment = test[(test['Year'] == 2015) & (test['Month'] == i+1)]
    total_pos_by_month = data_2015['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2015.append(percent)

#2016
total_sent_2016 = []
for i in range(12):
    data_2016 = test[(test['Year'] == 2016) & (test['Sentiment'] == -1) & (test['Month'] == i+1)]
    data_sentiment = test[(test['Year'] == 2016) & (test['Month'] == i+1)]
    total_pos_by_month = data_2015['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2016.append(percent)


plt.plot(month, total_sent_2013, marker='s', color='red')
plt.plot(month, total_sent_2014, marker='o', color='green', linestyle='--')
plt.plot(month, total_sent_2015, marker='o', color='purple', linestyle='--')
plt.plot(month, total_sent_2016, marker='o', color='yellow', linestyle='--')
plt.title("Negative Sentiment x Month")
plt.xlabel("Month")
plt.ylabel("Total in %")
plt.legend(["2013", "2014", "2015", "2016"], loc=1)




