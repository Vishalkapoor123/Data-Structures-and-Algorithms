class graph:
    def __init__(self, gdict=None):
        if(gdict is None):
            self.gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def findedges(self):
        edgename=[]
        for vertex in self.gdict:
            for nextvertex in self.gdict[vertex]:
                if {nextvertex, vertex} not in edgename:
                    edgename.append({vertex, nextvertex})
        return edgename

    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
    
    def addEdge(self, edge):
        print("1")
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        print("2")
        if vertex1 in self.gdict:
            print("3")
            self.gdict[vertex1].append(vertex2)
        else:
            print("4")
            self.gdictp[vertex1] = vertex2

    def findEdges(self):
        all_edges=[]
        for i in self.gdict.keys():
            for j in self.gdict[i]:
                all_edges.append({i,j})
        return all_edges


if __name__ == '__main__':
    graphelements = {'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']}
    mygraphobject = graph(graphelements)
    print(mygraphobject.getVertices())
    mygraphobject.addVertex("G")
    print(mygraphobject.getVertices())
    mygraphobject.addEdge({"G","E"})
    print(mygraphobject.findEdges())
    

    
