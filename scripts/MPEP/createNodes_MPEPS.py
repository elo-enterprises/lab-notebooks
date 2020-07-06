from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

chapterNumbers = np.arange(1, 30, 1).tolist()
#chapterNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#chapterNumbers = [18]
for chapterNumber in chapterNumbers:
    chapterText = ('00'+str(chapterNumber*100))[-4:]
    df = pd.read_csv('data/interim/MPEP/MPEPChapter' + chapterText + 'Sections.csv')
    
    for index, row in df.iterrows():
        pChapter = str(row['Chapter'])
        pSection = str(row['Section'])
        pParg = str(row['Paragraph'])
        if pParg == 'nan':
            pName = pSection
        else:
            pName = pSection + ' - ' + pParg
        pUpdateStatus = str(row['Update Status'])
        pTitle = str(row['Title']).strip()
        newNode = Node("MPEPSection", name=pName, chapter=pChapter, updateStatus=pUpdateStatus, title=pTitle)
        graph.create(newNode)
    
    cypherChapterText = chapterText.lstrip('0')
    cypherTextFind = ''
    cypherTextFind += "MATCH (n:MPEPSection { chapter: '" + cypherChapterText + "'}) "
    cypherTextFind += "RETURN n"
    df = pd.DataFrame(graph.run(cypherTextFind))

    df.to_csv (r'data/processed/MPEP/createNodes_MPEPS_' + chapterText + '.csv', index = False, header=True)
