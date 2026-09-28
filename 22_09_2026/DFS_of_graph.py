graph = {
    0: [1,2,3],
    1: [0,3],
    2: [0,4],
    3: [0,1,4],
    4: [2,3,5],
    5: [4]
    }
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
dfs(graph, 0)