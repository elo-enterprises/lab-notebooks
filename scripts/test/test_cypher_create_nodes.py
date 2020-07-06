import pandas as pd
import numpy as np

# Makes a txt file of Cypher nodes from the Patent Bar Test Questions
df = pd.read_csv('data/external/PatentBarTestQuestions.csv')

x = 0
cypherString = 'CREATE \n'
for index, row in df.iterrows():
    doc = str(row['Doc']).replace('\n',' ').strip()
    q = str(row['Q']).strip().replace('.0','')
    cypherString += '(pbtq' + str(x) + ':PatentBarTestQuestion { ' 
    cypherString += 'name: \'' + doc + ' - ' + q + '\', '
    cypherString += 'doc: \'' + doc + '\', '
    cypherString += 'q: \'' + q + '\''
    #cypherString += 'Call: \'' + str(row['Call']).strip() + '\', '
    #cypherString += 'Answer_Choices: \'' + str(row['Answer Choices']).strip() + '\', '
    #cypherString += 'Discussion: \'' + str(row['Discussion']).strip() + '\''
    cypherString += ' }),\n'
    x = x + 1
cypherString = cypherString[:-2]

text_file = open("data/interim/test/test_cypher_Create_Nodes_PatentBarTestQuestions.txt", "w")
text_file.write(cypherString)
text_file.close()