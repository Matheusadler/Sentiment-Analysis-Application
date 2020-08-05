import pandas as pd

#Carregar csv
data = pd.read_csv('../Crawler_G1/spiders/CSV_Data/G1_Data/Comments/CommentsG1_2020-07-01T14-30-09.csv', error_bad_lines=False, delimiter="*")

#CSV para lista
#Aqui ocorre a gambiarra, a função de converter para lista automaticamente ja remove aquelas aspas duplas iniciais, que tavam causando todo o problema
coment = [str(x).replace("[", "").replace("]", "") for x in data.values]

#Inserir linha inicial, que será o nome dos campos
coment.insert(0, 'Author,Published,Comment,Likes,Dislikes,Article,Keyword')

#Salvar lista como csv
with open('g1_clean.csv', 'w') as f:
    for item in coment:
        f.write("%s\n" % item)
        

#Carregar novo CSV
test = pd.read_csv('g1_clean.csv', encoding='latin-1', error_bad_lines=False)


#Aqui a parte que converte de csv pra json, so que ainda ta dando uns problemas, so que o pior ja foi resolvido
'''
#Tranforma CSV em JSON
import csv
import json

json_data = [json.dumps(d) for d in csv.DictReader(open('g1_clean.csv'))]


with open('SO_jsonout.json', 'w') as outfile:
    json.dump(output_list, outfile)
'''