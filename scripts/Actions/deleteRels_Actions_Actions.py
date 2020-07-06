from py2neo import Graph, Node, Relationship
from pandas import DataFrame

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
cypherTextDelete = ''
cypherTextDelete += "MATCH (n:Action)-[r:Action_PreAction]->(m:Action) "
cypherTextDelete += "DELETE r"
graph.run(cypherTextDelete)

cypherTextFind = ''
cypherTextFind += "MATCH (n:Action)-[r:Action_PreAction]->(m:Action) "
cypherTextFind += "RETURN n.name, m.name"
df = DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/Actions/createRels_Actions_Actions.csv', index = False, header=True)
