### 1. Graph Creation
```python
G = nx.Graph()  # Undirected graph
G.add_nodes_from(buildings)  # Add nodes
G.add_edge(node1, node2, weight=time)  # Add weighted edges
```

### 2. Shortest Path Finding
```python
# Find the fastest route
path = nx.shortest_path(G, start, end, weight='weight')
distance = nx.shortest_path_length(G, start, end, weight='weight')
```

### 3. Network Analysis
```python
# Centrality: which building is most "central"?
betweenness = nx.betweenness_centrality(G, weight='weight')

# Degree: how many connections does each node have?
degree = G.degree(node)

# Average path length: average walking time between any two buildings
avg = nx.average_shortest_path_length(G, weight='weight')
```

### 4. Visualization
```python
pos = nx.spring_layout(G)  # Position nodes
nx.draw_networkx_nodes(G, pos)  # Draw nodes
nx.draw_networkx_edges(G, pos)  # Draw edges
nx.draw_networkx_labels(G, pos)  # Add labels
```

### Run the Complete Analysis
```bash
python cmu_campus_network.py
```
