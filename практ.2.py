class Vertex:
    def __init__(self, data):
        self.data = data
        self.adjacent = []


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertex_data):
        vertex = Vertex(vertex_data)
        self.vertices.append(vertex)
        return vertex

    def find_vertex(self, vertex_data):
        for vertex in self.vertices:
            if vertex.data == vertex_data:
                return vertex
        return None

    def add_edge(self, src, dest):
        src_vertex = self.find_vertex(src)
        dest_vertex = self.find_vertex(dest)
        if src_vertex and dest_vertex:
            src_vertex.adjacent.append(dest_vertex)

    def topological_sort(self):
        indegrees = {vertex: 0 for vertex in self.vertices}

        for vertex in self.vertices:
            for neighbor in vertex.adjacent:
                indegrees[neighbor] += 1

        sorted_vertices = []
        zero_indegree_queue = [
            vertex for vertex in self.vertices if indegrees[vertex] == 0]

        while zero_indegree_queue:
            current_vertex = zero_indegree_queue.pop(0)
            sorted_vertices.append(current_vertex)

            for neighbor in current_vertex.adjacent:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    zero_indegree_queue.append(neighbor)

        return sorted_vertices

    def find_path(self, start, end):
        visited = set()
        path = []

        def dfs(vertex):
            visited.add(vertex)
            path.append(vertex.data)
            if vertex.data == end:
                return True

            for neighbor in vertex.adjacent:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            path.pop()
            return False

        start_vertex = self.find_vertex(start)
        end_vertex = self.find_vertex(end)

        if start_vertex and end_vertex:
            dfs(start_vertex)
            return path if end_vertex.data in path else None
        return None


g = Vertex()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2)
g.add_edge(2, 3)

topo_sorted = g.topological_sort()
print("Топологическая сортировка:", [v.data for v in topo_sorted])

path = g.find_path(1, 3)
print("Путь от 1 до 3:", path)
