from py2neo import Graph, Node, Relationship
from pandas import DataFrame

# https://py2neo.org/2.0/intro.html#nodes-relationships
# (demo only works behind VPN, using the bitnami neo4j container)
graph = Graph("bolt://neo4j.lab.elo.enterprises:7687", auth=("neo4j", "bitnami"))

alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
alice_knows_bob = Relationship(alice, "KNOWS", bob)
graph.create(alice_knows_bob)

df = DataFrame(graph.run("MATCH (n:Person) RETURN n"))

df.to_csv (r'data/interim/test/test_neo_python_objects.csv', index = False, header=True)



# text_file = open("data/interim/test_neo_matchPerson.txt", "w")
# text_file.write(records)
# text_file.close()