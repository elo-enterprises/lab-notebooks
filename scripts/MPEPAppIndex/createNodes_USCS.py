from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/interim/MPEPAppIndex/USCSections.csv')

for index, row in df.iterrows():
    pSection = str(row['Section'])
    pParg = str(row['Paragraph'])
    if pParg == 'nan':
        pName = pSection
    else:
        pName = pSection + ' - ' + pParg
    pUpdateStatus = str(row['Update Status'])
    pTitle = str(row['Title']).strip()
    newNode = Node("USCSection", name=pName, updateStatus=pUpdateStatus, title=pTitle)
    graph.create(newNode)

cypherTextFind = ''
cypherTextFind += "MATCH (n:USCSection) "
cypherTextFind += "RETURN n"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/MPEPAppIndex/createNodes_USCS.csv', index = False, header=True)
