from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))
df = pd.read_csv('data/external/Actions/Actions.csv')

for index, row in df.iterrows():
    pCategory = str(row['Action Categories']).strip()
    pTitle = str(row['Action Title']).strip()
    pPrecedingTitle = str(row['Preceding \nAction Titles']).strip()
    pActingAgent = str(row['Acting \nAgent']).strip()
    pReceivingAgent = str(row['Receiving \nAgent']).strip()
    pUSPTOFormCode = str(row['USPTO \nForm Code']).strip()
    pUSPTOFormTitle = str(row['USPTO \nForm Title']).strip()
    pSubmittalOptions = str(row['Submittal \nOptions']).strip()
    pFee = str(row['Fee']).strip()
    pFeeSE = str(row['Fee \nSmallEntity?']).strip()
    pDueDate = str(row['Due Date']).strip()
    pDueDateExt = str(row['Due Date \nExtendable?']).strip()
    pWhoCanSign = str(row['Who Can \nSign']).strip()
    pSignCOR = str(row['Certified Owner \nRequired?']).strip()
    pSMIItem = str(row['SMIndex \nItem Name']).strip()
    newNode = Node("Action", category=pCategory, name=pTitle, precedingName=pPrecedingTitle, 
        aAgent=pActingAgent, rAgent=pReceivingAgent, 
        usptoFormCode=pUSPTOFormCode, usptoFormTitle=pUSPTOFormTitle, 
        submittalOptions=pSubmittalOptions, 
        fee=pFee, feeSE=pFeeSE, 
        dueDate=pDueDate, dueDateExt=pDueDateExt, 
        whoCanSign=pWhoCanSign, signCOR=pSignCOR, 
        smiItem=pSMIItem)
    graph.create(newNode)

cypherTextFind = ''
cypherTextFind += "MATCH (n:Action) "
cypherTextFind += "RETURN n.name, n.precedingName, n.aAgent, n.rAgent"
df = pd.DataFrame(graph.run(cypherTextFind))

df.to_csv (r'data/processed/Actions/createNodes_Actions.csv', index = False, header=True)
