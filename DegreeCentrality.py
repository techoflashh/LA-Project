import numpy as np

def compute_degree_centrality(adj_matrix):
    num_nodes = adj_matrix.shape[0]
    
    # Compute row sums of the adjacency matrix
    degree_centrality = np.sum(adj_matrix, axis=1)
    type(degree_centrality);
    
    # Normalize degree centrality
    normalization_factor = float(num_nodes - 1)
    degree_centrality /= normalization_factor
    
    # Print degree centrality values
    print("Degree Centrality:")
    for node, centrality in enumerate(degree_centrality):
        print(f"Node {node}: {centrality}")
        
# Example adjacency matrix
adj_matrix = np.array([
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
])

compute_degree_centrality(adj_matrix)
