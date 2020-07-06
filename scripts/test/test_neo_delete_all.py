from py2neo import Graph, Node, Relationship
from pandas import DataFrame

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

#graph.run("MATCH (n) DETACH DELETE n")
graph.delete_all()

df = DataFrame(graph.run("MATCH (n) RETURN n"))

df.to_csv (r'data/interim/test/test_neo_delete_all.csv', index = False, header=True)
