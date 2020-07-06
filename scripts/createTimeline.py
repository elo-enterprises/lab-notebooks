from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

yearNumbers = np.arange(1900, 2021, 1).tolist()
for yearNumber in yearNumbers:
    newNode = Node("Year", name=yearNumber)
    graph.create(newNode)

for yearNumber in yearNumbers:
    if yearNumber != 2020:
        cypherTextCreate = ''
        cypherTextCreate += "MATCH (n:Year { name: " + str(yearNumber) + " }),"
        cypherTextCreate += "(m:Year { name: " + str(yearNumber + 1) + " }) "
        cypherTextCreate += "CREATE (n)-[r:NextYear]->(m)"
        graph.run(cypherTextCreate)

    
    
    