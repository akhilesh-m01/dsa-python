# no of provinces
from collections import defaultdict
class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def addNode(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def printList(self):
        for k,val in self.adjList.items():
            print(f"{k}:{val}")
    
    def dfs(self,start,vis):
        vis.append(start)

        for n in self.adjList[start]:
            if n not in vis:
                self.dfs(n,vis)

    def checkProvinces(self,start,nodes):
        vis = []
        c=0
        for n in range(1,nodes):
            if n not in vis:
                c+=1
                self.dfs(n,vis)
        print(c)

g1 = Graph()
g1.addNode(1,2)
g1.addNode(2,3)

g1.addNode(4,5)
g1.addNode(5,6)

g1.addNode(7,8)

g1.printList()

g1.checkProvinces(1,8)




