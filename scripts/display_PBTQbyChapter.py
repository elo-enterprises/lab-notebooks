from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

chapterText = '2100'
cypherChapterText = chapterText.lstrip('0')
cypherTextFind = ''
cypherTextFind += "MATCH (n:PatentBarTestQuestion)-[r:PBTQ_MPEPS]->(m:MPEPSection) "
cypherTextFind += "WHERE m.chapter = '" + cypherChapterText + "' "
cypherTextFind += "RETURN n.name, m.name, n.call, n.answerChoices, n.discussion"
df = pd.DataFrame(graph.run(cypherTextFind))

# brute force method of removing duplicate rows
df.drop_duplicates(inplace = True)

#df.sort_values(by=['PBTQ','MPEPS'])
df.sort_index() #.to_csv (r'data/processed/display_PBTQbyChapter.csv', index = False, header=True)

dfA = pd.DataFrame(
    {
        "text": []
    }
)

## this is a way to print out the names of columns in a DataFrame
# for col in df.columns: 
#     print(col)

x = 0
for index, row in df.iterrows():
    #if x < 1:
    #    x = x + 1
    qName = str(row[0])
    # format the call of the question to fit the screen
    qCall = str(row[2])
    qLineCall = '\n'
    y = 0
    while y < len(qCall):
        nextBreak = int(qCall.find(' ',y+100))
        if nextBreak == -1:
            nextBreak = len(qCall)
        qLineCall += qCall[y:nextBreak] + '\n'
        y = nextBreak
    # format the answer choices to fit the screen
    qAC = str(row[3])
    qLineAC = '\n'
    y = 0
    while y < len(qAC):
        nextBreak = qAC.find(' ',y+100)
        if nextBreak == -1:
            nextBreak = len(qAC)
        newLineBreak = qAC.find('\n',y,y+100)
        if newLineBreak == -1:
            qLineAC += qAC[y:nextBreak] + '\n'
            y = nextBreak
        else:
            qLineAC += qAC[y:newLineBreak] + '\n'
            y = newLineBreak + 1
    qDiscussion = str(row[4])
    qLineDiscussion = '\n\n\n'
    y = 0
    while y < len(qDiscussion):
        nextBreak = int(qDiscussion.find(' ',y+100))
        if nextBreak == -1:
            nextBreak = len(qDiscussion)
        qLineDiscussion += qDiscussion[y:nextBreak] + '\n'
        y = nextBreak
    qLineDiscussion += '\n\n'
    dfB = pd.DataFrame(
        {
            "text": [qName, qLineCall, qLineAC, qLineDiscussion]
        }
    )
    dfA = pd.concat([dfA, dfB], ignore_index=True)
        
dfA.to_csv (r'data/processed/display_PBTQbyChapter.csv', index = False, header=True)


