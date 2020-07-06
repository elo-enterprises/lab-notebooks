from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/interim/MPEPAppIndex/CFRSections.csv')

for index, row in df.iterrows():
    pChapter = str(row['Chapter'])
    pPart = str(row['Part'])
    pSection = str(row['Section'])
    if len(pSection) > 5:
        pSection = str(round(float(pSection),3))
    pName = pSection
    pParg = str(row['Paragraph'])
    # if pParg == 'nan':
    #     pName = pSection
    # else:
    #     pName = pSection + ' - ' + pParg
    pUpdateStatus = str(row['Update Status'])
    pTitle = str(row['Title']).strip()
    newNode = Node("CFRSection", name=pName, updateStatus=pUpdateStatus, title=pTitle)
    graph.create(newNode)

cypherTextFind = ''
cypherTextFind += "MATCH (n:CFRSection) "
cypherTextFind += "RETURN n"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/MPEPAppIndex/createNodes_CFRS.csv', index = False, header=True)
