from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/external/USPTOForms/USPTOForms.csv')

for index, row in df.iterrows():
    pCategory = str(row['Category']).strip()
    pCode = str(row['Code']).strip()
    pTitle = str(row['Title']).strip()
    pUpdate = str(row['Update']).strip()
    pNotes = str(row['Notes']).strip()
    pFileName = str(row['File Name']).strip()
    newNode = Node("USPTOForm", name=pCode, category=pCategory, title=pTitle, updated=pUpdate, notes=pNotes, fileName=pFileName)
    graph.create(newNode)

cypherTextFind = ''
cypherTextFind += "MATCH (n:USPTOForm) "
cypherTextFind += "RETURN n.name, n.category, n.title"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/USPTOForms/createNodes_USPTOForms.csv', index = False, header=True)
