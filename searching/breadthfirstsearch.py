class Graph:
    def __init__(self, edges, no_vertices):
        self.graph = [[] for _ in range(no_vertices)]

        for (source, destination) in edges:
            self.graph[source].append(destination)
            self.graph[destination].append(source)

    def bfs(self, source_vertex):
        '''Perform breadth-first search from a specified vertex.'''

        discovered = [False] * len(self.graph)

        queue = []
        queue.append(source_vertex)
        # Mark source vertex as discovered, because we begin the search there.
        discovered[source_vertex] = True
        while queue:
            # Get vertex added to queue least recently.
            s = queue.pop(0)

            # Examine all vertices adjacent to vertex s.
            for adjacent_vertex in self.graph[s]:
                # If it hasn't been discovered, add it to the queue and mark it
                # as discovered.
                if discovered[adjacent_vertex] is False:
                    queue.append(adjacent_vertex)
                    discovered[adjacent_vertex] = True

        return discovered


if __name__ == '__main__':
    # Test
    my_graph = Graph(edges=[(1, 2), (2, 3)], no_vertices=4)
    discovered = my_graph.bfs(2)
    print(discovered)
