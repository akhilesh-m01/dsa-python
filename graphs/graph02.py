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



g1 = Graph()
g1.addNode(1,2)
g1.addNode(2,3)
g1.addNode(3,4)
g1.addNode(4,5)
g1.addNode(5,1)
g1.printList()
print("bfs implementation")
g1.bfs(1)


