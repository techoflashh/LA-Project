#include <stdio.h>

void computeDegreeCentrality(int adjMatrix[][5], int numNodes) {
    float degreeCentrality[numNodes];
    int i, j;
    
    // Compute row sums of the adjacency matrix
    for (i = 0; i < numNodes; i++) {
        degreeCentrality[i] = 0;
        for (j = 0; j < numNodes; j++) {
            degreeCentrality[i] += adjMatrix[i][j];
        }
    }
    
    // Normalize degree centrality
    float normalizationFactor = (float)(numNodes - 1);
    for (i = 0; i < numNodes; i++) {
        degreeCentrality[i] /= normalizationFactor;
    }
    
    // Print degree centrality values
    printf("Degree Centrality:\n");
    for (i = 0; i < numNodes; i++) {
        printf("Node %d: %f\n", i, degreeCentrality[i]);
    }
}

int main() {
    int adjMatrix[][5] = {
        {0, 1, 1, 1, 0},
        {1, 0, 1, 0, 0},
        {1, 1, 0, 0, 1},
        {1, 0, 0, 0, 0},
        {0, 0, 1, 0, 0}
    };
    int numNodes = 5;
    
    computeDegreeCentrality(adjMatrix, numNodes);
    
    return 0;
}
