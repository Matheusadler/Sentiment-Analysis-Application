import polyglot
import numpy as np
import pandas as pd
import csv
from polyglot.text import Text

csvFilePath = 'CommentsG1_2020-06-06T15-41-58.csv'
jsonFilePath = 'CommentsG1.json'

with open(csvFilePath, 'r', encoding='utf-8') as csvFile:
    reader = csv.reader(csvFile)
    next(reader)
    for rows in reader:
        print(rows)



# TESTE COMMIT


