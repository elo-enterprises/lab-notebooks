from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/interim/MPEPAppIndex/CaseActions.csv')

for index, row in df.iterrows():
    pName = str(row['name']).replace('\'','')
    newNode = Node("CaseAction", name=pName, source="MPEP")
    graph.create(newNode)

cypherTextFind = ''
cypherTextFind += "MATCH (n:CaseAction {source: 'MPEP'}) "
cypherTextFind += "RETURN n"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/MPEPAppIndex/createNodes_CaseActions.csv', index = False, header=True)
