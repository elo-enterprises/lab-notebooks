from py2neo import Graph, Node, Relationship
import pandas as pd

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/interim/MPEPAppIndex/CaseActions.csv')

for index, row in df.iterrows():
    caseActionName = str(row['name']).replace('\'','').strip()
    caseActionYear = str(row['year']).replace('.0','')
    if caseActionYear != 'nan':
        cypherTextCreate = ''
        cypherTextCreate += "MATCH (n:CaseAction { name: '" + caseActionName + "' }),"
        cypherTextCreate += "(m:Year { name: " + caseActionYear + " }) "
        cypherTextCreate += "CREATE (n)-[r:CaseAction_Year]->(m)"
        graph.run(cypherTextCreate)

cypherTextFind = ''
cypherTextFind += "MATCH (n:CaseAction)-[r:CaseAction_Year]->(m:Year) "
cypherTextFind += "RETURN n.name, m.name"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/MPEPAppIndex/createRels_CaseActions_Years.csv', index = False, header=True)

#This cypher query returns the entire timeline, but there are too many nodes to easily display
#MATCH (n:Year) OPTIONAL MATCH (m:CaseAction)-[r:CaseAction_Year]->(n) RETURN n,m