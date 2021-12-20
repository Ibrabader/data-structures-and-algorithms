class Vertex:
  def __init__(self, value):
    self.value = value

class Edge:

  def __init__(self,vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:

  def __init__(self):
    self.__adj_list = {}
    

  def add_node(self, value):
    node = Vertex(value)
    self.__adj_list[node] = []
    return node

  def add_edge(self, start_vertex, end_vertex, weight=0):
    if start_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    if end_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    edge = Edge(end_vertex, weight)
    self.__adj_list[start_vertex].append(edge)
    

  def neighbors(self, vertex):
    return self.__adj_list.get(vertex, [])
  

  def get_nodes(self):
    return self._adj_list.keys()


  def size(self):
    return len(self.__adj_list)

  def print_graph(self):
    print(self.__adj_list)

  def breath_first_search(self,start_vertex):

    queue=Queue()
    checked=set()
    output=[]
    queue.enqueue(start_vertex)
    checked.add(start_vertex)
    output.append(start_vertex.value)
    if start_vertex==None:
        return "empty graph"
    while len(queue):
        current_vertex = queue.dequeue()
        _neighbors = self.neighbors(current_vertex)

        for edge in _neighbors:
            neighbor = add_edge.vertex

            if neighbor not in checked:
                queue.enqueue(neighbor)
                checked.add_node(neighbor)
                output.append(neighbor.value)

        return output









# class Graph:
#     def __init__(self,edges):
#         self.edges = edges
#         self.graph_dectionary= {}
#     for start, end in self.edges :
#         if start in self.graph_dectionary:
#             self.graph_dectionary[start].append(end) 
#         else:
#             self.graph_dectionary[start]=[end]
        




# if __name__ == '__main__':

#     routes = [
#         ("Mumbai","Pune"),
#         ("Mumbai", "Surat"),
#         ("Surat", "Bangaluru"),
#         ("Pune","Hyderabad"),
#         ("Pune","Mysuru"),
#         ("Hyderabad","Bangaluru"),
#         ("Hyderabad", "Chennai"),
#         ("Mysuru", "Bangaluru"),
#         ("Chennai", "Bangaluru")
#     ]

#     rout_graph=Graph(routes)

    ## code challenge 36

    