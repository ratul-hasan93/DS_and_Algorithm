# BFS Implementation

def BFS(graph, node, visited, queue, level):
    visited.append(node)
    queue.append(node)

    level[node] = 0

    while queue:
        parent = queue.pop(0)

        print(parent, end=' ')

        for child in graph[parent]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
                level[child] = level[parent] + 1


if __name__ == "__main__":

    visited = []
    queue = []
    level = {}

    graph = {
        '1' : ['3', '7', '5'],
        '3' : ['6'],
        '7' : ['8', '10'],
        '5' : ['4'],
        '6' : [],
        '8' : ['2'],
        '10': ['9','50'],
        '4' : [],
        '2' : [],
        '9' : [],
        '50': []
    }

    BFS(graph, '1', visited, queue, level)
    print('\n')
    print("Level:" ,level)
    print()
    print("Queue is Empty:",queue)
    print()