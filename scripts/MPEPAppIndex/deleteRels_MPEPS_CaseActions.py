from py2neo import Graph, Node, Relationship
from pandas import DataFrame

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
cypherTextDelete = ''
cypherTextDelete += "MATCH (n:MPEPSection)-[r:MPEPS_CaseAction]->(m:CaseAction) "
cypherTextDelete += "DELETE r"
graph.run(cypherTextDelete)

cypherTextFind = ''
cypherTextFind += "MATCH (n:MPEPSection)-[r:MPEPS_CaseAction]->(m:CaseAction) "
cypherTextFind += "RETURN n.name, m.name"
df = DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/MPEPAppIndex/createRels_MPEPS_CaseActions.csv', index = False, header=True)
