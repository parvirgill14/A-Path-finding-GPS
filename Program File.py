import random


map = {'VA': [('WV', 13), ('NV', 15), ('BY', 11), ('RH', 10)],  # Vancouver
       'NV': [('WV', 5), ('VA', 15), ('BY', 16)],  # North Vancouver
       'WV': [('NV', 5), ('VA', 13)],  # West Vancouver
       'BY': [('NV', 16), ('VA', 11), ('RH', 21), ('NW', 10), ('MI', 55)],  # Burnaby
       'RH': [('VA', 10), ('DE', 10), ('BY', 21), ('SY', 29)],  # Richmond
       'SY': [('NW', 7), ('MI', 47), ('LY', 18), ('RH', 29), ('DE', 26)],  # Surrey
       'NW': [('BY', 10), ('SY', 7)],  # New Westminster
       'DE': [('RH', 10), ('SY', 26), ('LY', 30)],  # Delta
       'LY': [('SY', 18), ('DE', 30), ('AF', 33)],  # Langley
       'AF': [('LY', 33), ('MI', 12), ('CW', 33)],  # Abbotsford
       'CW': [('HP', 52), ('AF', 33)],  # Chilliwack
       'HP': [('MI', 83), ('CW', 52)],  # Hope
       'MI': [('HP', 83), ('AF', 12), ('SY', 47), ('BY', 55)]  # Mission
       }


def heuristic(node, goal):
    # Find the coordinates of the nodes in the map
    goal_coords = [c[0] for c in map.keys() if c[0] == goal]

    # Calculate the minimum distance between the two nodes
    min_dist = float('inf')
    for n1, edges in map.items():
        if n1[0] == node:
            for n2, dist in edges:
                if n2[0] == goal:
                    min_dist = min(min_dist, dist)
                elif n2[0] in goal_coords:
                    # If the neighbor is closer to the goal than the current node, use it
                    neighbor_dist = dist + heuristic(n2[0], goal)
                    if neighbor_dist < min_dist:
                        min_dist = neighbor_dist

    # Generate a random number between 5 and 10
    rand_num = random.randint(5, 10)

    # Calculate the heuristic value as the minimum distance minus the random number
    heuristic_val = min_dist - rand_num

    return heuristic_val


def a_star(start, goal):
    # Initialize the fringe with the starting node and its cost
    fringe = [(0, start, [], 0)]

    # Initialize the visited set and the list of paths
    visited = set()
    paths = []

    # Loop until the fringe is empty
    while len(fringe) > 0:
        # Pop the node with the lowest total cost from the fringe
        (f, node, path, distance) = fringe.pop(0)

        # If the node is the goal, append the path and distance to the list of paths
        if node == goal:
            paths.append((path + [node], distance))

        # Add the node to the visited set
        visited.add(node)

        # Loop through the neighbors of the node
        for (neighbor, cost) in map[node]:
            # If the neighbor has not been visited, calculate its cost
            if neighbor not in visited:
                g = f + cost
                h = heuristic(neighbor, goal)
                total_cost = g + h
                # Add the neighbor to the fringe with its total cost
                # and the new path and distance from the start node to the neighbor
                fringe.append(
                    (total_cost, neighbor, path + [node], distance + cost))

    # If there are no paths from the start to the goal, return None
    if len(paths) == 0:
        return None
    
    # Find and Return only the shortest path using the cost
    minDistance = paths[0][1]
    shortestPath = paths[0]

    # Check each path for shortest
    for x in paths:
        if(minDistance > x[1]):
            shortestPath = x
            minDistance = x[1]
            
    return shortestPath


def PathFinder(start, goal, algorithmType):
    if (algorithmType == "a*"):
        return a_star(start, goal)


# Give User imformation on what to type
print("Vancouver = VA, North Vancouver = NV, West Vancouver = WV, Burnaby = BY, Richmond = RH, Surrey = SY, ")
print("New Westminster = NW, Delta = DE, Langley = LY, Abbotsford = AF, Chilliwack = CW, Hope = HP, Mission = MI")
start = input("Enter city code for source: ").upper()  # input source
goal = input("Enter city code for destination: ").upper()  # input destination

# Our A Star Algorithm that find the path also the cost
path = PathFinder(start, goal, "a*")

# Display Path to the User
if path:
    print(
        f"The shortest path from {start} to {goal} is ({'->'.join(path[0])}) with a cost of {path[1]}")
else:
    print(f"There is no path from {start} to {goal}")
