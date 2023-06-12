import networkx as nx
import urllib.request
import gzip

# Fetch the Facebook Social Circles dataset
# url = "https://snap.stanford.edu/data/facebook_combined.txt.gz"
file_path = "facebook_combined.txt.gz"
# urllib.request.urlretrieve(url, file_path)

# Create an empty graph
G = nx.Graph()

# Read the dataset and add edges to the graph
# with gzip.open(file_path, 'rt') as file:
#     for line in file:
#         # Each line contains an edge represented by two node IDs separated by a space
#         node1, node2 = line.strip().split(' ')
#         G.add_edge(node1, node2)

with open("data.txt","r") as f:
    for i in range(10000):
        data = f.readline()
        node1,node2 = data.strip().split(' ')
        G.add_edge(node1,node2)



# Compute centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# Print centrality measures for a few nodes
nodes = ['0', '1', '2']  # Example nodes

max_degree_centrality = max(degree_centrality,key=degree_centrality.get)
max_betweenness_centrality = max(betweenness_centrality,key=betweenness_centrality.get)
max_closeness_centrality = max(closeness_centrality,key=closeness_centrality.get)
max_eigenvector_centrality = max(eigenvector_centrality,key=eigenvector_centrality.get)


# for node in nodes:
#     print(f"Node {node}:")
print("Degree Centrality:", max_degree_centrality,degree_centrality[max_degree_centrality])
print("Betweenness Centrality:", max_betweenness_centrality,betweenness_centrality[max_betweenness_centrality])
print("Closeness Centrality:", max_closeness_centrality,closeness_centrality[max_closeness_centrality])
print("Eigenvector Centrality:", max_eigenvector_centrality,eigenvector_centrality[max_eigenvector_centrality])
#     print()

# Visualize the graph (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, with_labels=False, node_size=10, node_color='blue', alpha=0.6)
plt.title("Facebook Social Circles Graph")
plt.axis("off")
plt.show()
