from py2neo import Graph, Node, Relationship
from pandas import DataFrame

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
cypherTextDelete = ''
cypherTextDelete += "MATCH (n:USPTOForm) "
cypherTextDelete += "DETACH DELETE n"
graph.run(cypherTextDelete)

cypherTextFind = ''
cypherTextFind += "MATCH (n:USPTOForm) "
cypherTextFind += "RETURN n.name, n.category, n.title"
df = DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/USPTOForms/createNodes_USPTOForms.csv', index = False, header=True)
