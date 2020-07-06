from py2neo import Graph, Node, Relationship
import pandas as pd

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/interim/MPEPAppIndex/CaseActions.csv')

for index, row in df.iterrows():
    caseActionName = str(row['name']).replace('\'','').strip()
    stringLinks = str(row['Links to MPEP'])
    i = -2
    while stringLinks.find(';',i+2) != -1: 
        prevI = int(i+2)
        i = stringLinks.find(';',prevI)
        mpepsName = stringLinks[prevI:i]
        cypherTextCreate = ''
        cypherTextCreate += "MATCH (n:MPEPSection { name: '" + mpepsName + "' }),"
        cypherTextCreate += "(m:CaseAction { name: '" + caseActionName + "' }) "
        cypherTextCreate += "CREATE (n)-[r:MPEPS_CaseAction]->(m)"
        graph.run(cypherTextCreate)

cypherTextFind = ''
cypherTextFind += "MATCH (n:MPEPSection)-[r:MPEPS_CaseAction]->(m:CaseAction) "
cypherTextFind += "RETURN n.name, m.name"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/MPEPAppIndex/createRels_MPEPS_CaseActions.csv', index = False, header=True)
