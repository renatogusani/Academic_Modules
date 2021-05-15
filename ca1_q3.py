# date : 31/03/2021
# Author : Renato Gusani
# Student no. : x19411076
# Question - Q3.1 + Q3.2

# * * * * * * * * * * question 3.1) * * * * * * * * * *

# * * This question has been answered on the word document * *





# * * * * * * * * * * question 3.2) * * * * * * * * * *

# The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter
import pprint

graph = {}
values = {}
vertex = int(input("Enter number of vertices (6): "))

print("Enter vertices (Cities) : ")
for i in range(vertex):
    graph.setdefault(input())

edges = {}
for x in graph:
    edges.setdefault(x)

for i in graph:
    graph[i] = edges

print("Enter Edges (**Keep pressing enter after finished entering edges for a particular city**): ")
for i in graph:
    print(i)
    for j in graph[i]:
        var = input()
        graph[i][j] = var

pprint.pprint(graph)
