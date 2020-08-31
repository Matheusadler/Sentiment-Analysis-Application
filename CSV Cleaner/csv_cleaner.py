import pandas as pd
import icu
import csv
import seaborn as sns
from polyglot.text import Text
import matplotlib.pyplot as plt

# Load csv
data = pd.read_csv('CommentsG1_KeywordsITA-Preprocessed.csv', error_bad_lines=False, delimiter="*")

# Convert to list
coment = [str(x).replace("[", "").replace("]", "") for x in data.values]

# Insert initial line
coment.insert(0, 'Author,Published,Comment,Likes,Dislikes,Article,Keyword')

sentiment = []
# Save file as csv
with open('g1_clean.csv', 'w', encoding='utf-8') as f:
    for item in coment:
        # sentiment.append(1)
        f.write("%s\n" % item)

test = pd.read_csv('g1_clean.csv', error_bad_lines=False)
test.to_csv('g1_clean.csv')

'''
test = pd.read_csv('g1_clean.csv', encoding='latin-1', error_bad_lines=False)

for row in test['Comment'].values:
     try:
         text = Text(row)
         print(text.polarity)
         if text.polarity > 0:
             sentiment.append(1)
         elif text.polarity < 0:
             sentiment.append(-1)
         else:
             sentiment.append(0)
     except:
         print("An exception occurred")
         error =+ 1
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

# 2011
total_sent_2011 = []
for i in range(12):
    data_2011 = test[(test['Year'] == 2011) & (test['Sentiment'] == -1) & (test['Month'] == i+1)]
    data_sentiment = test[(test['Year'] == 2011) & (test['Month'] == i+1)]
    total_pos_by_month = data_2011['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2011.append(percent)

# 2012
total_sent_2012 = []
for i in range(12):
    data_2012 = test[(test['Year'] == 2012) & (test['Sentiment'] == -1) & (test['Month'] == i+1)]
    data_sentiment = test[(test['Year'] == 2012) & (test['Month'] == i+1)]
    total_pos_by_month = data_2012['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2012.append(percent)
    
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
    total_pos_by_month = data_2016['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2016.append(percent)
    
#2017
total_sent_2017 = []
for i in range(12):
    data_2017 = test[(test['Year'] == 2017) & (test['Sentiment'] == -1) & (test['Month'] == i+1)]
    data_sentiment = test[(test['Year'] == 2017) & (test['Month'] == i+1)]
    total_pos_by_month = data_2017['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2017.append(percent)
    
#2018
total_sent_2018 = []
for i in range(12):
    data_2018 = test[(test['Year'] == 2018) & (test['Sentiment'] == -1) & (test['Month'] == i+1)]
    data_sentiment = test[(test['Year'] == 2018) & (test['Month'] == i+1)]
    total_pos_by_month = data_2018['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2018.append(percent)

#2019
total_sent_2019 = []
for i in range(12):
    data_2019 = test[(test['Year'] == 2019) & (test['Sentiment'] == -1) & (test['Month'] == i+1)]
    data_sentiment = test[(test['Year'] == 2019) & (test['Month'] == i+1)]
    total_pos_by_month = data_2019['Sentiment'].count()
    total_sent_by_month = data_sentiment['Sentiment'].count()
    if(total_pos_by_month == 0):
        percent = 0
    else:
        percent = ((total_pos_by_month*100)/total_sent_by_month)
    total_sent_2019.append(percent)
    
    


plt.plot(monthList, total_sent_2011, marker='s', color='red')
plt.plot(monthList, total_sent_2012, marker='o', color='blue', linestyle='--')
plt.plot(monthList, total_sent_2013, marker='o', color='black', linestyle='--')
plt.plot(monthList, total_sent_2014, marker='o', color='green', linestyle='--')
plt.plot(monthList, total_sent_2015, marker='o', color='purple', linestyle='--')
plt.plot(monthList, total_sent_2016, marker='o', color='yellow', linestyle='--')
plt.plot(monthList, total_sent_2017, marker='o', color='grey', linestyle='--')
plt.plot(monthList, total_sent_2018, marker='o', color='orange', linestyle='--')
plt.plot(monthList, total_sent_2019, marker='o', color='cyan', linestyle='--')
plt.title("Negative Sentiment x Month")
plt.xlabel("Month")
plt.ylabel("Total in %")
plt.legend(["2011", "2012", "2013", "2014", "2015", "2016","2017", "2018", "2019"], loc=1)


for row in test['Comment'].values:
     try:
         text = Text(row)
         print("caso:", i)
         print(text.polarity)
         i += 1
     except:
         print("An exception occurred")
         
         
         
import datetime

dateD = []
dateM = []
dateY = []

data = dateparser.parse(u'07 Set 2013 10:14:48')

import dateparser
for row in test['Published'].values:
     day = dateparser.parse(row).day
     dateD.append(day)
     month = dateparser.parse(row).month
     dateM.append(month)
     year = dateparser.parse(row).year
     dateY.append(year)
     
     
     test['Year'] = dateY
     test['Month'] = dateM
     test['Day'] = dateD
     
     
     
     
     
     
     
     
     
     
     
     # 2011
   ...: total_sent_2011 = []
   ...: for i in range(12):
   ...:     data_2011 = test[(test['Year'] == 2011) & (test['Sentiment'] == -1) & (test['Month'] == i + 1)]
   ...:     data_sentiment = test[(test['Year'] == 2011) & (test['Month'] == i + 1)]
   ...:     total_pos_by_month = data_2011['Sentiment'].count()
   ...:     total_sent_by_month = data_sentiment['Sentiment'].count()
   ...:     if (total_pos_by_month == 0):
   ...:         percent = 0
   ...:     else:
   ...:         percent = ((total_pos_by_month * 100) / total_sent_by_month)
   ...:     total_sent_2011.append(percent)
   ...:     totalNeg.append(-1)
   ...: 
   ...: # 2012
   ...: total_sent_2012 = []
   ...: for i in range(12):
   ...:     data_2012 = test[(test['Year'] == 2012) & (test['Sentiment'] == -1) & (test['Month'] == i + 1)]
   ...:     data_sentiment = test[(test['Year'] == 2012) & (test['Month'] == i + 1)]
   ...:     total_pos_by_month = data_2012['Sentiment'].count()
   ...:     total_sent_by_month = data_sentiment['Sentiment'].count()
   ...:     if (total_pos_by_month == 0):
   ...:         percent = 0
   ...:     else:
   ...:         percent = ((total_pos_by_month * 100) / total_sent_by_month)
   ...:     total_sent_2012.append(percent)
   ...:     totalNeg.append(-1)
   ...: 
   ...: # 2013
   ...: total_sent_2013 = []
   ...: for i in range(12):
   ...:     data_2013 = test[(test['Year'] == 2013) & (test['Sentiment'] == -1) & (test['Month'] == i + 1)]
   ...:     data_sentiment = test[(test['Year'] == 2013) & (test['Month'] == i + 1)]
   ...:     total_pos_by_month = data_2013['Sentiment'].count()
   ...:     total_sent_by_month = data_sentiment['Sentiment'].count()
   ...:     if (total_pos_by_month == 0):
   ...:         percent = 0
   ...:     else:
   ...:         percent = ((total_pos_by_month * 100) / total_sent_by_month)
   ...:     total_sent_2013.append(percent)
   ...:     totalNeg.append(-1)
   ...: 
   ...: # 2014
   ...: total_sent_2014 = []
   ...: for i in range(12):
   ...:     data_2014 = test[(test['Year'] == 2014) & (test['Sentiment'] == -1) & (test['Month'] == i + 1)]
   ...:     data_sentiment = test[(test['Year'] == 2014) & (test['Month'] == i + 1)]
   ...:     total_pos_by_month = data_2014['Sentiment'].count()
   ...:     total_sent_by_month = data_sentiment['Sentiment'].count()
   ...:     if (total_pos_by_month == 0):
   ...:         percent = 0
   ...:     else:
   ...:         percent = ((total_pos_by_month * 100) / total_sent_by_month)
   ...:     total_sent_2014.append(percent)
   ...:     totalNeg.append(-1)
   ...: 
   ...: # 2015
   ...: total_sent_2015 = []
   ...: for i in range(12):
   ...:     data_2015 = test[(test['Year'] == 2015) & (test['Sentiment'] == -1) & (test['Month'] == i + 1)]
   ...:     data_sentiment = test[(test['Year'] == 2015) & (test['Month'] == i + 1)]
   ...:     total_pos_by_month = data_2015['Sentiment'].count()
   ...:     total_sent_by_month = data_sentiment['Sentiment'].count()
   ...:     if (total_pos_by_month == 0):
   ...:         percent = 0
   ...:     else:
   ...:         percent = ((total_pos_by_month * 100) / total_sent_by_month)
   ...:     total_sent_2015.append(percent)
   ...:     totalNeg.append(-1)
   ...: 
   ...: # 2016
   ...: total_sent_2016 = []
   ...: for i in range(12):
   ...:     data_2016 = test[(test['Year'] == 2016) & (test['Sentiment'] == -1) & (test['Month'] == i + 1)]
   ...:     data_sentiment = test[(test['Year'] == 2016) & (test['Month'] == i + 1)]
   ...:     total_pos_by_month = data_2016['Sentiment'].count()
   ...:     total_sent_by_month = data_sentiment['Sentiment'].count()
   ...:     if (total_pos_by_month == 0):
   ...:         percent = 0
   ...:     else:
   ...:         percent = ((total_pos_by_month * 100) / total_sent_by_month)
   ...:     total_sent_2016.append(percent)
   ...:     totalNeg.append(-1)
   ...: 
   ...: # 2017
   ...: total_sent_2017 = []
   ...: for i in range(12):
   ...:     data_2017 = test[(test['Year'] == 2017) & (test['Sentiment'] == -1) & (test['Month'] == i + 1)]
   ...:     data_sentiment = test[(test['Year'] == 2017) & (test['Month'] == i + 1)]
   ...:     total_pos_by_month = data_2017['Sentiment'].count()
   ...:     total_sent_by_month = data_sentiment['Sentiment'].count()
   ...:     if (total_pos_by_month == 0):
   ...:         percent = 0
   ...:     else:
   ...:         percent = ((total_pos_by_month * 100) / total_sent_by_month)
   ...:     total_sent_2017.append(percent)
   ...:     totalNeg.append(-1)
   ...: 
   ...: # 2018
   ...: total_sent_2018 = []
   ...: for i in range(12):
   ...:     data_2018 = test[(test['Year'] == 2018) & (test['Sentiment'] == -1) & (test['Month'] == i + 1)]
   ...:     data_sentiment = test[(test['Year'] == 2018) & (test['Month'] == i + 1)]
   ...:     total_pos_by_month = data_2018['Sentiment'].count()
   ...:     total_sent_by_month = data_sentiment['Sentiment'].count()
   ...:     if (total_pos_by_month == 0):
   ...:         percent = 0
   ...:     else:
   ...:         percent = ((total_pos_by_month * 100) / total_sent_by_month)
   ...:     total_sent_2018.append(percent)
   ...:     totalNeg.append(-1)
   ...: 
   ...: # 2019
   ...: total_sent_2019 = []
   ...: for i in range(12):
   ...:     data_2019 = test[(test['Year'] == 2019) & (test['Sentiment'] == -1) & (test['Month'] == i + 1)]
   ...:     data_sentiment = test[(test['Year'] == 2019) & (test['Month'] == i + 1)]
   ...:     total_pos_by_month = data_2019['Sentiment'].count()
   ...:     total_sent_by_month = data_sentiment['Sentiment'].count()
   ...:     if (total_pos_by_month == 0):
   ...:         percent = 0
   ...:     else:
   ...:         percent = ((total_pos_by_month * 100) / total_sent_by_month)
   ...:     total_sent_2019.append(percent)
   ...:     totalNeg.append(-1)
   ...:     

'''



