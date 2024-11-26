//Breadth First Search
#include<stdio.h>

int visited[10] = {0};       // Visited array initialized to 0 for all nodes
int adj[10][10];             // Adjacency matrix
int queue[10];
int front = -1, rear = -1;   // Queue pointers

// Function to insert into the queue
void insert(int item) {
    if (rear == 9) {
        printf("Queue is full\n");
    } else {
        if (front == -1) front = 0;
        queue[++rear] = item;
    }
}

// Function to delete from the queue
int delete() {
    if (front == -1 || front > rear) {
        return -1;
    } else {
        return queue[front++];
    }
}

// BFS traversal function
void bfs(int start, int n) {
    int i, p;
    insert(start);
    visited[start] = 1;
    
    while (front <= rear) {
        p = delete();
        if (p == -1) break;  // End if queue is empty
        
        printf("%d ", p);   // Print the current node
        
        // Check all nodes for adjacency
        for (i = 0; i < n; i++) {
            if (adj[p][i] == 1 && visited[i] == 0) {
                insert(i);
                visited[i] = 1;
            }
        }
    }
}

int main() {
    int i, j, v, s;
    
    printf("Enter the number of vertices: ");
    scanf("%d", &v);
    
    printf("Enter the adjacency matrix:\n");
    for (i = 0; i < v; i++) {
        for (j = 0; j < v; j++) {
            scanf("%d", &adj[i][j]);
        }
    }
    
    printf("Enter the starting vertex: ");
    scanf("%d", &s);
    
    printf("BFS traversal starting from vertex %d:\n", s);
    bfs(s, v);
    return 0;
}

