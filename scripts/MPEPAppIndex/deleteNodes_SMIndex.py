from py2neo import Graph, Node, Relationship
from pandas import DataFrame

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

chapterNames = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#chapterNames = ['A']
for chapterText in chapterNames:
    cypherTextDelete = ''
    cypherTextDelete += "MATCH (n:MPEPSMIndexItem { chapter: '" + chapterText + "'}) "
    cypherTextDelete += "DETACH DELETE n"
    graph.run(cypherTextDelete)

    cypherTextFind = ''
    cypherTextFind += "MATCH (n:MPEPSMIndexItem { chapter: '" + chapterText + "'}) "
    cypherTextFind += "RETURN n"
    df = DataFrame(graph.run(cypherTextFind))

    df.to_csv (r'data/processed/MPEPAppIndex/createNodes_SMIndex' + chapterText + '.csv', index = False, header=True)
