import pandas as pd

# Load csv
data = pd.read_csv('../Crawler_G1/spiders/CSV_Data/G1_Data/Comments/CommentsG1_2020-07-01T14-30-09.csv', error_bad_lines=False, delimiter="*")

# Convert to list
coment = [str(x).replace("[", "").replace("]", "") for x in data.values]

# Insert initial line
coment.insert(0, 'Author,Published,Comment,Likes,Dislikes,Article,Keyword')

# Save file as csv
with open('g1_clean.csv', 'w') as f:
    for item in coment:
        f.write("%s\n" % item)
        

# Load new csv
test = pd.read_csv('g1_clean.csv', encoding='latin-1', error_bad_lines=False)


# json
'''
import csv
import json

json_data = [json.dumps(d) for d in csv.DictReader(open('g1_clean.csv'))]


with open('SO_jsonout.json', 'w') as outfile:
    json.dump(output_list, outfile)
'''