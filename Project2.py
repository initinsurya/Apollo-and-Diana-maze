
import sys
sys.setrecursionlimit(10**4)

# Open the input file
with open(sys.argv[1], 'r') as f:
    contents = f.readlines()

# Split the file contents with \n
input = "".join(contents).strip().split("\n")

# Storing rows and columns from the first line of the file
rows = int(input[0].split(" ")[0])
cols = int(input[0].split(" ")[1])
length = rows*cols

# Creating a dictionary where each direction has some value.
# This helps to find the all other connected nodes of a particular nodes dynamically
direction_values = {
    'N': -cols,
    'S': cols,
    'E': 1,
    'W': -1,
    'NE': 1-cols,
    'NW': -1-cols,
    'SE': 1+cols,
    'SW': -1+cols
}

# Storing the indexes of the nodes in an array
maze = []
for i in range(1, rows+1):
    maze.append(input[i])

# Creating a dictionary to store the colors and directions of the nodes
maze_nodes = {
    "color": [],
    "direction": [],
}

# Storing the colors and directions of the nodes in respective indexes
for x in maze:
    for y in x.split(" "):
        if(y != ""):
            # Storing the last node i.e 'O' color and direction as Bulls_Eye
            if(y == "O"):
                maze_nodes["color"].append("Bulls_Eye")
                maze_nodes["direction"].append("Bulls_Eye")

            else:
                maze_nodes["color"].append(y.split("-")[0])
                maze_nodes["direction"].append(y.split("-")[1])


# Initializing a empty graph
graph = {}
for i in range(length):
    graph[i] = []


# Generating the graph based on nodes we have created
# This graph consists of indexes of nodes of same direction and different color
# i.e If we take a node R-S, this node has the connected nodes which are in south
# to that node and different color i.e B
# -------- Example ---------------
# R-S(0)   R-W(1)     B-SE(2)
# R-SE(3)  B-NW(4)    B-W(5)
# B-SE(6)  B-W(7)     B-SE(8)
# customized_graph={
#     0: [6],
#     1: [],
#     2: [],
#     3: [7],
#     4: [0],
#     5: [3],
#     6: [],
#     7: [],
#     8: []
#   }
for i in range(length):
    # Storing the index of BullsEye
    if(maze_nodes["direction"][i] == 'Bulls_Eye'):
        graph[i] = [i]
    # If index of next node is <0 or >rows*cols-1 then dont store the index
    elif(i + direction_values[maze_nodes["direction"][i]] < 0 or i + direction_values[maze_nodes["direction"][i]] > length-1):
        continue

    else:
        connected_node = i + direction_values[maze_nodes["direction"][i]]
        exit_loop = False
        # Loop to store the indexes of connected nodes in same direction and differet color

        while(connected_node >= 0 and connected_node < length and
                connected_node != 'Bulls_Eye' and exit_loop == False):
            if(((maze_nodes["direction"][i] in ['E', 'NE', 'SE'] and i % cols == cols-1)
                    or (maze_nodes["direction"][i] in ['W', 'NW', 'SW'] and i % cols == 0))):
                break
            if (((maze_nodes["direction"][i] in ['E', 'NE', 'SE'] and connected_node % cols == cols-1)
                 or (maze_nodes["direction"][i] in ['W', 'NW', 'SW'] and connected_node % cols == 0))):
                exit_loop = True
            if(maze_nodes["color"][i] != maze_nodes["color"][connected_node]):
                graph[i].append(connected_node)
            connected_node += direction_values[maze_nodes["direction"][i]]


visited = set()
path = []

# Traversal alogorithm to find the BullsEye


def depth_first_traversal(node, visited, path):
    path.append(node)
    visited.add(node)
    if maze_nodes["direction"][node] == 'Bulls_Eye':
        result = ""
        for i in range(len(path)-1):
            a = path[i]
            b = path[i+1]
            c = int(
                abs((b-a))/abs(direction_values[maze_nodes["direction"][a]]))

            # Calculating the final output
            result += str(c) + maze_nodes["direction"][a]+" "

        f = open("soln_path_list.txt", "w")
        # Writing the final output in a file
        f.write(result)
    else:
        for n in graph[node]:
            if n not in visited:
                depth_first_traversal(n, visited, path)
    path.pop()


# Calling the function
visited = depth_first_traversal(0,  visited, path)
