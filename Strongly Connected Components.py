#Daniel Eke
#CS566 Analysis and Algorithms
#5/3/2019
#Program Assignment 3


import sys
from collections import defaultdict

#This class creates a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = defaultdict(list)

    #function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    #A function used by DFS
    def DFSVisit(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        #print("DFSVisit v") #was used to see what DFS was printing
        print(v)


        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSVisit(i, visited)

    def fill(self, v, visited, stack):
        #Mark the current node as visited
        visited[v] = True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] is False:
                self.fill(i, visited, stack)

        stack.append(v)

    #Returns the transpose of this graph
    def getTranspose(self):
        g = Graph(self.V)

        #Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    #The function that finds and prints all strongly connected components
    def findSCCs(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * self.V
        #print(visited)
        #print(self.V)

        #Adds the vertices to the stack according to their finishing times
        for i in range(self.V):
            if visited[i] is False:
                self.fill(i, visited, stack)
            #print(visited[i])

        #Create a reversed graph
        gr = self.getTranspose()

        #Labels all the vertices as not visited (For second DFS)
        visited = [False] * self.V

        #Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] is False:
                gr.DFSVisit(i, visited)

                print() #adds space to separate the strongly connected components


def main():
    #load the text file into an array

    input1 = sys.argv[1]
    file = open(input1)  #here is where you input the text file
    outfile = open("p3_out.txt", "w+")
    values = []
    g = Graph(7) #define number of vertices

    print('Edges and Vertices (u,v) from text file')
    for line in file:
        line = line.replace(':', ' ').replace(',', ' ') #replaces ':' and ',' with a space so file can be read easily
        adj = list(map(int, line.strip().split()))

        values.append(adj)
        u = adj[0]

        for v in adj[1:]:
            g.addEdge(int(u), int(v))

            print(u,v) #print (u,v) to verify the addEdge function is working correctly
    output = str(g.findSCCs())
    outfile.write('Values from text file \n')
    outfile.write(str(values))
    outfile.write('\n')
    outfile.write('Following are strongly connected components \n')
    outfile.write(output)
    print('Values from text file')
    print(values) #print to verify the values from text file are being loaded correctly
    print('Following are strongly connected components')
    g.findSCCs()
    file.close()




if __name__ == '__main__':
        main()