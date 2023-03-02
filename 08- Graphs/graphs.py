class Graph:
    def __init__(self):
        """Graph constructor"""
        self.adj_list ={}

    def print_graph(self):
        """Method to print items on graph"""
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])


    def add_vertex(self, vertex):
        """Method to add a vertex if is not already on the adjacent list"""
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return  True
        return False

    def add_edge(self, v1, v2):
        """Method to add an edge """
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return  True
        return False

    def remove_edge(self, v1, v2):
        """Method to remove an edge"""
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self,vertex):
        """Method to remove a vertex"""
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return  False


# testing methods
my_graph = Graph()

my_graph.add_vertex("a")
my_graph.add_vertex("b")
my_graph.add_vertex("c")
my_graph.add_vertex("d")

my_graph.add_edge("a", "b")
my_graph.add_edge("a", "c")
my_graph.add_edge("a", "d")
my_graph.add_edge("b", "d")
my_graph.add_edge("c", "d")

my_graph.print_graph()

print("After change")
my_graph.remove_vertex("d")
my_graph.print_graph()