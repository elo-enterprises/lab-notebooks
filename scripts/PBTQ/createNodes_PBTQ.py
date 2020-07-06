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
    pCall = str(row['Call']).strip()
    pAnswerChoices = str(row['Answer Choices']).strip()
    pDiscussion = str(row['Discussion']).strip()
    newNode = Node("PatentBarTestQuestion", name=pbtqName, doc=pdoc, q=pq, call=pCall, answerChoices=pAnswerChoices, discussion=pDiscussion)
    graph.create(newNode)

cypherTextFind = ''
cypherTextFind += "MATCH (n:PatentBarTestQuestion) "
cypherTextFind += "RETURN n.name, n.doc, n.q"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/PBTQ/createNodes_PBTQ.csv', index = False, header=True)
