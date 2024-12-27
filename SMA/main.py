class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

class SMAStarNode(Node):
    def __init__(self, state, parent=None, cost=0, f=0, g=0):
        super().__init__(state, parent, cost)
        self.f = f  # Total cost (g + h)
        self.g = g  # Cost from start to this node

def heuristic(state, goal):
    return abs(goal - state)

def successors_revised(state):
    return [(state + 1, 1), (state + 2, 2), (state * 2, 3)]

def sma_star_simple(start, goal, successors, max_nodes):
    open_list = [SMAStarNode(start, g=0, f=0)]
    forgotten = {}

    while open_list:
        current = open_list.pop(0)
        print(f"Processing node: {current.state}, f-value: {current.f}")

        if current.state == goal:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]

        for succ_state, succ_cost in successors(current.state):
            g = current.g + succ_cost
            h = heuristic(succ_state, goal)
            f = g + h
            child = SMAStarNode(succ_state, current, g=g, f=f)
            print(f"Generated child node: {child.state}, g: {g}, h: {h}, f: {f}")

            if child.state in forgotten and forgotten[child.state].f <= f:
                print(f"Child node {child.state} is in forgotten list with lower f-value; skipping.")
                continue

            existing = next((n for n in open_list if n.state == child.state), None)
            if existing and existing.f > f:
                print(f"Updating node {existing.state} in open list with lower f-value.")
                open_list.remove(existing)
            elif existing:
                print(f"Child node {child.state} already in open list with lower f-value; skipping.")
                continue

            open_list.append(child)

        open_list.sort(key=lambda n: n.f)
        if len(open_list) > max_nodes:
            forgotten_node = open_list.pop(-1)
            forgotten[forgotten_node.state] = forgotten_node
            print(f"Memory limit reached. Forgetting node: {forgotten_node.state}")

    print("No path found. Goal not reached.")
    return None

def main():
    start_state = 0
    goal_state = 10
    max_nodes_limit = 5

    path = sma_star_simple(start_state, goal_state, successors_revised, max_nodes_limit)
    if path:
        print("Found path:", path)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
