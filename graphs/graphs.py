class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adj_Mat = [[0 for i in range(vertices)] for j in range(vertices)]

    def printMatrix(self):
         for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.adj_Mat[i][j],end=" ")
            print("")

    def add_Node(self,u,v):
        self.adj_Mat[u][v] = 1
        self.adj_Mat[v][u] = 1


g1 = Graph(4)
g1.printMatrix()
g1.add_Node(1,2)
g1.add_Node(2,3)
g1.printMatrix()