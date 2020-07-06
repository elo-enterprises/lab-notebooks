from py2neo import Graph, Node, Relationship
import pandas as pd
import numpy as np
# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

cypherTextDelete = ''
cypherTextDelete += "MATCH (n:Year) "
cypherTextDelete += "DETACH DELETE n"
graph.run(cypherTextDelete)

    
    
    