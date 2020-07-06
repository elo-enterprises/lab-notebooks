from py2neo import Graph, Node, Relationship
import pandas as pd

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

#chapterNumbers = np.arange(1, 30, 1).tolist()
#chapterNumbers = [19, 20, 22, 23, 24, 25, 26, 27, 28, 29]
chapterNumbers = [21]
for chapterNumber in chapterNumbers:
    chapterText = ('0'+str(chapterNumber*100))[-4:]
    df = pd.read_csv('data/interim/MPEP/MPEPChapter' + chapterText + 'Sections.csv')

    for index, row in df.iterrows():
        pSection = str(row['Section'])
        if pSection != 'nan':
            pParg = str(row['Paragraph'])
            if pParg == 'nan':
                mpepsName = pSection
            else:
                mpepsName = pSection + ' - ' + pParg
            stringLinks = str(row['Links to 35USC']).replace('35 U.S.C. ','')
            i = -2
            while stringLinks.find(';',i+2) != -1: 
                prevI = int(i+2)
                i = stringLinks.find(';',prevI)
                uscsName = stringLinks[prevI:i]
                cypherTextCreate = ''
                cypherTextCreate += "MATCH (n:MPEPSection { name: '" + mpepsName + "' }),"
                cypherTextCreate += "(m:USCSection { name: '" + uscsName + "' }) "
                cypherTextCreate += "CREATE (n)-[r:MPEPS_USCS]->(m)"
                graph.run(cypherTextCreate)

cypherTextFind = ''
cypherTextFind += "MATCH (n:MPEPSection)-[r:MPEPS_USCS]->(m:USCSection) "
cypherTextFind += "RETURN n.name, m.name"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/MPEPAppIndex/createRels_MPEPS_USCS.csv', index = False, header=True)
