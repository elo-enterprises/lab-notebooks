#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# Practice reading from and writing to a local csv file.
# This csv was created in Google Apps Script. 
# The data came from the MPEP as a pdf, opened in Google Docs, massaged manually and imported to Google Sheets.
df = pd.read_csv('00_CSV_JSON_Cypher/MPEP_Chapter_2100_Table_of_Contents.csv')

df['Section'] = np.where(df['Section'] == '2103', 
                     df['Section'] + 'add a string', 
                     df['Section'])

df.to_csv (r'00_CSV_JSON_Cypher/MPEP_Chapter_2100_Table_of_Contents_Modified.csv', index = False, header=True)

df


# In[2]:


import json

# Practice reading from a local json file.
# This json file was created by Google Apps Script from data in a Google Sheets worksheet.
f = open("00_CSV_JSON_Cypher/21_MPEP_Chapter2100_JSON.txt",)
data = json.loads(f.read())
for i in data['MPEPSection']: 
     print(i) 
f.close()


# In[7]:


import pandas as pd
import numpy as np

# Practice reading from and writing to a local txt file the Cypher code to create a list of nodes.
# This csv was created in Google Apps Script. 
# The data came from the MPEP as a pdf, opened in Google Docs, massaged manually and imported to Google Sheets.
df = pd.read_csv('00_CSV_JSON_Cypher/MPEP_Chapter_2100_Table_of_Contents.csv')

#CREATE (n:Person { name: 'Andy', title: 'Developer' })
x = 0
cypherString = 'CREATE \n'
for index, row in df.iterrows():
    cypherString += '(mpeps' + str(x) + ':MPEPSection { ' 
    cypherString += 'Part: \'' + str(row['Part']) + '\', '
    cypherString += 'Chapter: \'' + str(row['Chapter']) + '\', '
    cypherString += 'Section: \'' + str(row['Section']) + '\'},\n'
    x = x + 1
cypherString = cypherString[:-2] + '\n)'

text_file = open("00_CSV_JSON_Cypher/Practice_Cypher_Create_Nodes.txt", "w")
text_file.write(cypherString)
text_file.close()


# In[9]:


from py2neo import Graph

#graphURI = "bolt://hobby-hinpjibellpegbkeenkdffdl.dbs.graphenedb.com:24787"
graphURI = "neo4j://neo4j.lab.elo.enterprises:7687"
#userName = "obie"
userName = "neo4j"
#pw = "b.bUGEl3MVJ2uE.sNNkyu229ztdhTA9"
pw = "bitnami"

#graph = Graph(graphURI, user=userName, password=pw, secure=True)
#graph = Graph(graphURI, user=userName, password=pw, scheme='bolt', secure=True)
#graph = Graph(graphURI,auth=(userName, pw), scheme='bolt', secure=True)
#graph = Graph(graphURI, auth=(userName, pw), port=24787, secure=True)
#graph = Graph("https://arthur:excalibur@camelot:1150/db/data/")
#graph = Graph("http://" + userName + ":" + pw + "@" + graphURI + "/db/data/")
graph = Graph("http://neo4j:bitnami@neo4j://neo4j.lab.elo.enterprises:7687/db/data/")

graph.run("CREATE (n:Person {name:'Bob'})")
result = graph.run("MATCH (n:Person) RETURN n")
for record in result:
    print(record)


# In[ ]:




