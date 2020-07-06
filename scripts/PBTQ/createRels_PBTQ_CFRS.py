from py2neo import Graph, Node, Relationship
import pandas as pd

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/external/PBTQ/PatentBarTestQuestions.csv')

for index, row in df.iterrows():
    pdoc = str(row['Doc']).replace('\n',' ').strip()
    pq = str(row['Q']).strip().replace('.0','')
    pbtqName = pdoc + ' - ' + pq
    stringLinks = str(row['Links to \n37 CFR'])
    i = -2
    while stringLinks.find(';',i+2) != -1: 
        prevI = int(i+2)
        i = stringLinks.find(';',prevI)
        cfrsName = stringLinks[prevI:i]
        cypherTextCreate = ''
        cypherTextCreate += "MATCH (n:PatentBarTestQuestion { name: '" + pbtqName + "' }),"
        cypherTextCreate += "(m:CFRSection { name: '" + cfrsName + "' }) "
        cypherTextCreate += "CREATE (n)-[r:PBTQ_CFRS]->(m)"
        graph.run(cypherTextCreate)

cypherTextFind = ''
cypherTextFind += "MATCH (n:PatentBarTestQuestion)-[r:PBTQ_CFRS]->(m:CFRSection) "
cypherTextFind += "RETURN n.name, m.name"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/PBTQ/createRels_PBTQ_CFRS.csv', index = False, header=True)
