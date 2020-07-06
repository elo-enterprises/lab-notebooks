from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/external/PBTQ/PatentBarTestQuestions.csv')

for index, row in df.iterrows():
    pdoc = str(row['Doc']).replace('\n',' ').strip()
    pq = str(row['Q']).strip().replace('.0','')
    pbtqName = pdoc + ' - ' + pq
    stringLinks = str(row['Links to \nCases & Actions'])
    i = -2
    while stringLinks.find(';',i+2) != -1: 
        prevI = int(i+2)
        i = stringLinks.find(';',prevI)
        caseActionName = stringLinks[prevI:i]
        #existingNodes = list(graph.find('CaseAction', property_key='name', property_value=caseActionName))
        cypherTextFind = ''
        cypherTextFind += "MATCH (n:CaseAction {name: '" + caseActionName + "'}) "
        cypherTextFind += "RETURN n"
        existingNodes = list(graph.run(cypherTextFind))
        if len(existingNodes) == 0:
            newNode = Node("CaseAction", name=caseActionName, source="PBTQ")
            graph.create(newNode)

cypherTextFind = ''
cypherTextFind += "MATCH (n:CaseAction {source: 'PBTQ'}) "
cypherTextFind += "RETURN n"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/PBTQ/createNodes_CaseActions.csv', index = False, header=True)
