import useful
import networkx as nx

G = nx.Graph()
G.add_edges_from(line.split('-') for line in useful.get_lines('23'))

print(','.join(sorted(nx.max_weight_clique(G, weight=None)[0])))

        