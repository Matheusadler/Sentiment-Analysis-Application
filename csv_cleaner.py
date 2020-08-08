import pandas as pd
import icu
import csv
from polyglot.text import Text

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
test['Month'] = test['Published'].dt.month_name()
test['Day'] = test['Published'].dt.day
test['Sentiment'] = sentiment

#Salvando novo CSV
test.to_csv('g1_clean.csv')

#Comandos para acessar anos/meses especificos
#data_2014 = test[test['Year']==2014]
#data_janeiro = test[test['Month']=='January']
