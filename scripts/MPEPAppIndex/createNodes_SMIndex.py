from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

chapterNames = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#chapterNames = ['A']
for chapterText in chapterNames:
    df = pd.read_csv('data/interim/MPEPAppIndex/SMIndex' + chapterText + '.csv')
    
    for index, row in df.iterrows():
        pChapter = chapterText
        pTopic = str(row['Topic']).replace('\'','')
        pSubtopic1 = str(row['Subtopic1']).replace('\'','')
        pSubtopic2 = str(row['Subtopic2']).replace('\'','')
        pSubtopic3 = str(row['Subtopic3']).replace('\'','')
        pSubtopic4 = str(row['Subtopic4']).replace('\'','')
        pName = pTopic
        if pSubtopic1 != 'nan':
            pName += ' - ' + pSubtopic1
            if pSubtopic2 != 'nan':
                pName += ' - ' + pSubtopic2
                if pSubtopic3 != 'nan':
                    pName += ' - ' + pSubtopic3
                    if pSubtopic4 != 'nan':
                        pName += ' - ' + pSubtopic4
        newNode = Node("MPEPSMIndexItem", name=pName, chapter=pChapter)
        graph.create(newNode)
    
    cypherTextFind = ''
    cypherTextFind += "MATCH (n:MPEPSMIndexItem { chapter: '" + chapterText + "'}) "
    cypherTextFind += "RETURN n"
    df = pd.DataFrame(graph.run(cypherTextFind))

    df.to_csv (r'data/processed/MPEPAppIndex/createNodes_SMIndex' + chapterText + '.csv', index = False, header=True)
