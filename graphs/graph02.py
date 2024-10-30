from collections import defaultdict,deque
class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)
    
    def printList(self):
        # print(self.adjList)
        for i,val in self.adjList.items():
            print(f"{i}:{val}")
    
    def addNode(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def removeNode(self,u,v):
        self.adjList[u].remove(v)
        self.adjList[v].remove(u)

    def bfs(self,start):
        visited = []
        q1 = deque()
        q1.append(start)
        visited.append(start)

        while q1:
            ele = q1.popleft()
            print(ele,end=" ")

            for i in self.adjList[ele]:
                if i not in visited:
                    q1.append(i)
                    visited.append(i)
    
    def dfs(self,start,vis,res):
        vis.append(start)
        res.append(start)

        for i in self.adjList[start]:
            if i not in vis:
                self.dfs(i,vis,res)

    def printdfs(self,start):
        vis = []   
        self.start = start
        res = []
        self.dfs(start,vis,res) 
        print(res)   




g1 = Graph()
g1.addNode(1,4)
g1.addNode(1,3)
g1.addNode(2,3)
g1.addNode(3,4)
g1.addNode(4,5)
g1.addNode(5,1)
g1.printList()
print("bfs implementation")
g1.bfs(1)
print("\ndfs implementation")
g1.printdfs(3)


