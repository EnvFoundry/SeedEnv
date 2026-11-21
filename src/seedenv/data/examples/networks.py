"""Analyze a small weighted graph without dropping node identities."""
import json
import networkx as nx

graph=nx.Graph()
graph.add_weighted_edges_from([("a","b",2),("b","c",1),("a","c",5)])
print(json.dumps({"path":nx.shortest_path(graph,"a","c",weight="weight"),
                  "distance":nx.shortest_path_length(graph,"a","c",weight="weight")}))
