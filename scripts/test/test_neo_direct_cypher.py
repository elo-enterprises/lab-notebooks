from py2neo import Graph

graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

graph.run("CREATE (n:Person {name:'Bob'})")
result = graph.run("MATCH (n:Person) RETURN n")
for record in result:
    print(record)