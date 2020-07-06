from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

#countRelsMPEPS_USCS = len(graph.match(("MPEPSection", "USCSection"), "MPEPS_USCS"))
#    "MATCH (n)-[r:MPEPS_USCS]->(m) WHERE ID(a)=" + str(a.identity) + " RETURN count(r)"

df = pd.DataFrame(
    {
        "c1": ['-'],
        "c2": ['-'],
        "c3": ['-']
    }
)
#cypherCountNodesMPEPS = "MATCH (n:MPEPSection) "
#cypherCountNodesMPEPS += "RETURN count(n) as count"
#countNodesMPEPS = graph.run(cypherCountNodesMPEPS).evaluate()
countNodesMPEPS = len(graph.nodes.match("MPEPSection"))
dfMPEP = pd.DataFrame(
    {
        "c1": ['MPEP Sections'],
        "c2": ['-'],
        "c3": [countNodesMPEPS]
    }
)
df = pd.concat([df, dfMPEP], ignore_index=True)
countRelsMPEPS_USCS = graph.run("MATCH (n)-[r:MPEPS_USCS]->(m) RETURN count(r)").evaluate()
dfMPEP_USCS = pd.DataFrame(
    {
        "c1": ['-'],
        "c2": ['MPEPS_USCS'],
        "c3": [countRelsMPEPS_USCS]
    }
)
df = pd.concat([df, dfMPEP_USCS], ignore_index=True)
countRelsMPEPS_CFRS = graph.run("MATCH (n)-[r:MPEPS_CFRS]->(m) RETURN count(r)").evaluate()
dfMPEP = pd.DataFrame(
    {
        "c1": ['-'],
        "c2": ['MPEPS_CFRS'],
        "c3": [countRelsMPEPS_CFRS]
    }
)
df = pd.concat([df, dfMPEP], ignore_index=True)
countRelsMPEPS_CaseActions = graph.run("MATCH (n)-[r:MPEPS_CaseAction]->(m) RETURN count(r)").evaluate()
dfMPEP_CaseAction = pd.DataFrame(
    {
        "c1": ['-'],
        "c2": ['MPEPS_CaseAction'],
        "c3": [countRelsMPEPS_CaseActions]
    }
)
df = pd.concat([df, dfMPEP_CaseAction], ignore_index=True)
countRelsMPEPS_SMIndex = graph.run("MATCH (n)-[r:MPEPS_SMIndex]->(m) RETURN count(r)").evaluate()
dfMPEP_SMIndex = pd.DataFrame(
    {
        "c1": ['-','-'],
        "c2": ['MPEPS_SMIndex','-'],
        "c3": [countRelsMPEPS_SMIndex,'-']
    }
)
df = pd.concat([df, dfMPEP_SMIndex], ignore_index=True)

##------------------------------------------------------------------------------

countNodesUSCS = len(graph.nodes.match("USCSection"))
dfUSCS = pd.DataFrame(
    {
        "c1": ['35 USC Sections','-'],
        "c2": ['-','-'],
        "c3": [countNodesUSCS,'-']
    }
)
df = pd.concat([df, dfUSCS], ignore_index=True)

##------------------------------------------------------------------------------

countNodesCFRS = len(graph.nodes.match("CFRSection"))
dfCFRS = pd.DataFrame(
    {
        "c1": ['37 CFR Sections','-'],
        "c2": ['-','-'],
        "c3": [countNodesCFRS,'-']
    }
)
df = pd.concat([df, dfCFRS], ignore_index=True)

##------------------------------------------------------------------------------

countNodesCaseActions = len(graph.nodes.match("CaseAction"))
dfCaseActions = pd.DataFrame(
    {
        "c1": ['Case Actions','-'],
        "c2": ['-','-'],
        "c3": [countNodesCaseActions,'-']
    }
)
df = pd.concat([df, dfCaseActions], ignore_index=True)

##------------------------------------------------------------------------------

countNodesSMIndex = len(graph.nodes.match("MPEPSMIndexItem"))
dfSMIndex = pd.DataFrame(
    {
        "c1": ['MPEP Subject Matter Index Items','-'],
        "c2": ['-','-'],
        "c3": [countNodesSMIndex,'-']
    }
)
df = pd.concat([df, dfSMIndex], ignore_index=True)

##------------------------------------------------------------------------------

countNodesPBTQ = len(graph.nodes.match("PatentBarTestQuestion"))
dfPBTQ = pd.DataFrame(
    {
        "c1": ['Patent Bar Test Questions'],
        "c2": ['-'],
        "c3": [countNodesPBTQ]
    }
)
df = pd.concat([df, dfPBTQ], ignore_index=True)
countRelsPBTQ_MPEPS = graph.run("MATCH (n)-[r:PBTQ_MPEPS]->(m) RETURN count(r)").evaluate()
dfPBTQ_MPEPS = pd.DataFrame(
    {
        "c1": ['-'],
        "c2": ['PBTQ_MPEPS'],
        "c3": [countRelsPBTQ_MPEPS]
    }
)
df = pd.concat([df, dfPBTQ_MPEPS], ignore_index=True)
countRelsPBTQ_USCS = graph.run("MATCH (n)-[r:PBTQ_USCS]->(m) RETURN count(r)").evaluate()
dfPBTQ_USCS = pd.DataFrame(
    {
        "c1": ['-'],
        "c2": ['PBTQ_USCS'],
        "c3": [countRelsPBTQ_USCS]
    }
)
df = pd.concat([df, dfPBTQ_USCS], ignore_index=True)
countRelsPBTQ_CFRS = graph.run("MATCH (n)-[r:PBTQ_CFRS]->(m) RETURN count(r)").evaluate()
dfPBTQ_CFRS = pd.DataFrame(
    {
        "c1": ['-'],
        "c2": ['PBTQ_CFRS'],
        "c3": [countRelsPBTQ_CFRS]
    }
)
df = pd.concat([df, dfPBTQ_CFRS], ignore_index=True)
countRelsPBTQ_CaseActions = graph.run("MATCH (n)-[r:PBTQ_CaseAction]->(m) RETURN count(r)").evaluate()
dfPBTQ_CaseActions = pd.DataFrame(
    {
        "c1": ['-','-'],
        "c2": ['PBTQ_CaseAction','-'],
        "c3": [countRelsPBTQ_CaseActions,'-']
    }
)
df = pd.concat([df, dfPBTQ_CaseActions], ignore_index=True)

##------------------------------------------------------------------------------

countNodesUSPTOForms = len(graph.nodes.match("USPTOForm"))
dfPBTQ_CaseActions = pd.DataFrame(
    {
        "c1": ['USPTO Forms','-'],
        "c2": ['-','-'],
        "c3": [countNodesUSPTOForms,'-']
    }
)
df = pd.concat([df, dfPBTQ_CaseActions], ignore_index=True)

df.to_csv (r'data/processed/display_DBSummary.csv', index = False, header=True)