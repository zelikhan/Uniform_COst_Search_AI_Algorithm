mygraph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '4': ['7', '8'],
    '7': ['11', '12'],
    '6': ['10'],
    '3': ['6'],
    '5': ['9'],
    '9': ['13'],
    '11': [],
    '12': [],
    '8': [],
    '13': [],
    '10': []
}

visited = []
queue = []
starting_node = input("Please Enter Starting Node : ")
goal_state = input("Enter Goal State : ")


def mybfs(mygraph, visited, starting_node):
    visited.append(starting_node)
    queue.append(starting_node)
    while queue:
        a = queue.pop(0)
        print(a, end=" ")
        for neighbour in mygraph[a]:
            if neighbour not in visited:
                if goal_state == neighbour:
                    break
                else:
                    visited.append(neighbour)
                    queue.append(neighbour)


print("Bredth First Search Traversal : ")
mybfs(mygraph, visited, starting_node)
