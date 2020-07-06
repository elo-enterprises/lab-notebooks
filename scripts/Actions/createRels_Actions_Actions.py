from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/external/Actions/Actions.csv')

for index, row in df.iterrows():
    pTitle = str(row['Action Title']).strip()
    stringPrecedingTitles = str(row['Preceding \nAction Titles']).replace('\n','').strip()
    i = -2
    while stringPrecedingTitles.find(';',i+2) != -1: 
        prevI = int(i+2)
        i = stringPrecedingTitles.find(';',prevI)
        pPrecedingTitle = stringPrecedingTitles[prevI:i]
        cypherTextCreate = ''
        cypherTextCreate += "MATCH (n:Action { name: '" + pTitle + "' }),"
        cypherTextCreate += "(m:Action { name: '" + pPrecedingTitle + "' }) "
        cypherTextCreate += "CREATE (n)-[r:Action_PreAction]->(m)"
        graph.run(cypherTextCreate)

cypherTextFind = ''
cypherTextFind += "MATCH (n:Action)-[r:Action_PreAction]->(m:Action) "
cypherTextFind += "RETURN n.name, m.name"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/Actions/createRels_Actions_Actions.csv', index = False, header=True)
