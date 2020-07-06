from py2neo import Graph, Node, Relationship
from pandas import DataFrame

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

chapterNumbers = np.arange(1, 30, 1).tolist()
#chapterNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#chapterNumbers = [18]
for chapterNumber in chapterNumbers:
    chapterText = ('00'+str(chapterNumber*100))[-4:]
    cypherChapterText = chapterText.lstrip('0')
    
    cypherTextDelete = ''
    cypherTextDelete += "MATCH (n:MPEPSection { chapter: '" + cypherChapterText + "'}) "
    cypherTextDelete += "DETACH DELETE n"
    graph.run(cypherTextDelete)
    
    cypherTextFind = ''
    cypherTextFind += "MATCH (n:MPEPSection { chapter: '" + cypherChapterText + "'}) "
    cypherTextFind += "RETURN n"
    df = DataFrame(graph.run(cypherTextFind))

    df.to_csv (r'data/processed/MPEP/createNodes_MPEPS_' + chapterText + '.csv', index = False, header=True)
