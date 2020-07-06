from py2neo import Graph, Node, Relationship
import pandas as pd

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
        stringLinks = str(row['MPEPLink'])
        i = -2
        while stringLinks.find(';',i+2) != -1: 
            prevI = int(i+2)
            i = stringLinks.find(';',prevI)
            mpepsName = stringLinks[prevI:i]
            cypherTextCreate = ''
            cypherTextCreate += "MATCH (n:MPEPSection { name: '" + mpepsName + "' }),"
            cypherTextCreate += "(m:MPEPSMIndexItem { name: '" + pName + "' }) "
            cypherTextCreate += "CREATE (n)-[r:MPEPS_SMIndex]->(m)"
            graph.run(cypherTextCreate)
    
cypherTextFind = ''
cypherTextFind += "MATCH (n:MPEPSection)-[r:MPEPS_SMIndex]->(m:MPEPSMIndexItem) "
cypherTextFind += "RETURN n.name, m.name"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/MPEPAppIndex/createRels_MPEPS_SMIndex.csv', index = False, header=True)
