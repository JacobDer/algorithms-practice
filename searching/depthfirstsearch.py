class Graph:
    def __init__(self, edges, no_vertices):
        self.graph = [[] for _ in range(no_vertices)]

        for (source, destination) in edges:
            self.graph[source].append(destination)
            self.graph[destination].append(source)

    def dfs(self, source_vertex):
        '''Perform depth-first search from a specified vertex.'''

        discovered = [False] * len(self.graph)

        stack = []
        stack.append(source_vertex)

        while stack:
            current_vertex = stack.pop()
            # Mark current vertex as discovered.
            discovered[current_vertex] = True
            for adjacent_vertex in self.graph[current_vertex]:
                # Add all undiscovered vertices to the stack.
                if discovered[adjacent_vertex] is False:
                    stack.append(adjacent_vertex)

        return discovered


if __name__ == '__main__':
    my_graph = Graph(edges=[(1, 2), (1, 3)], no_vertices=4)
    print(my_graph.dfs(1))
