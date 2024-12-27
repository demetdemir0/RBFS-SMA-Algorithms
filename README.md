# Simplified Memory-Bounded A* (SMA*) Algorithm  

This repository contains a Python implementation of the Simplified Memory-Bounded A* (SMA*) algorithm, a memory-efficient heuristic search algorithm for finding optimal paths in state spaces.  

---

## Features  

- **Memory-Bounded Search:**  
  - The algorithm uses a limited memory space (`max_nodes`) to store nodes in the search tree.  
  - Nodes with the least promising `f`-value are "forgotten" when memory is full.  

- **Heuristic Function:**  
  - A simple heuristic function is used: the absolute difference between the current state and the goal state.  

- **Successor Function:**  
  - Generates successors by applying specific operations (e.g., `+1`, `+2`, `*2`) to the current state.  

- **Path Reconstruction:**  
  - Once the goal is reached, the path from the start state to the goal state is reconstructed and returned.  

---

## How It Works  

1. **Initialization:**  
   - The algorithm starts with an open list containing the initial state.  
   - A dictionary (`forgotten`) stores nodes that have been removed due to memory constraints.  

2. **Node Expansion:**  
   - Nodes are expanded based on their `f`-values (sum of `g` and `h`).  
   - Successors are generated using the custom `successors_revised` function.  

3. **Memory Management:**  
   - If the number of nodes exceeds the `max_nodes` limit, the least promising node (with the highest `f`-value) is removed and stored in the `forgotten` dictionary.  

4. **Goal Check:**  
   - If the current node matches the goal state, the algorithm reconstructs the path and terminates.  

