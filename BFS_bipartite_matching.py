from dataclasses import dataclass, field
from typing import Optional, List
import sys


'''All class definitions'''
# Defining Vertex class to  be used, we need a list of neighbor connections and if it's matched, and predecessor also, (and visited), and group
@dataclass
class Vertex:
    label: None
    group: Optional[str] = None
    neighbors: Optional[List['Vertex']] = field(default_factory=list)
    matched_with: Optional['Vertex'] = None
    predecessor: Optional['Vertex'] = None
    visited: bool = False
    
# An edge has two nodes it's connected to, u and v,  and whether it's matched
@dataclass
class Edge:
    u: Vertex
    v: Vertex
    matched: bool = False

# Storing everything in a class to make things easier, as well as a matching list (to use in the hungarian algorithm)
@dataclass
class Graph:
    vertices: List[Vertex]
    edges: List[Edge] = field(default_factory=list)
    matchings: List[Edge] = field(default_factory=list)

    def add_edge(self, u: Vertex, v: Vertex, matched: bool = False):
        # Add an edge and update neighbors.
        edge = Edge(u, v, matched)
        self.edges.append(edge)
        u.neighbors.append(v)  #store u as neighbor of v and vice versa
        v.neighbors.append(u)
        if matched:
            u.matched_with = v 
            v.matched_with = u
            self.matchings.append(edge) #add to graph matchings list










'''inputting the graph from https://www.gradescope.com/courses/1069836/assignments/6870785/submissions/new into the program'''

X = [Vertex(label) for label in ['u', 'v', 'x', 'y', 'z']] # Top vertices
Y = [Vertex(label) for label in ['1', '2', '3', '4', '5', '6']] # Bottom vertices

for vertex in X:
    vertex.group = "X"
for vertex in Y:
    vertex.group = "Y"

quick_get = {label: i for i, label in enumerate(['u', 'v', 'x', 'y', 'z'])} #letters
numbers = {label: i for i, label in enumerate(['1', '2', '3', '4', '5', '6'])}
quick_get.update(numbers)

def get(index):
    return quick_get[index]
#making a dictionary that looks like {"u": 0, "1":0, "v":1, ...} so i can quickly get vertices by label from U and V
#So i can do U[get["x"]] instead of having to guess where vetex u is with magic numbers


G = Graph(vertices=X + Y)

# Adding Matched edges:
G.add_edge(X[get("y")], Y[get("6")], matched=True)  # y–6
G.add_edge(X[get("u")], Y[get("3")], matched=True)  # u–3
G.add_edge(X[get("z")], Y[get("1")], matched=True)  # z–1
G.add_edge(X[get("x")], Y[get("4")], matched=True)  # x–4

# Adding all other edges:
G.add_edge(X[get("u")], Y[get("5")])  # u-5
G.add_edge(X[get("v")], Y[get("3")])  # you get the gist...
G.add_edge(X[get("x")], Y[get("1")]) 
G.add_edge(X[get("x")], Y[get("2")]) 
G.add_edge(X[get("x")], Y[get("5")]) 
G.add_edge(X[get("y")], Y[get("2")]) 
G.add_edge(X[get("y")], Y[get("4")]) 
G.add_edge(X[get("z")], Y[get("6")]) 






''' BFS logic (aka hungarian algorithm) '''

unmatched_vertices_X = [vertex for vertex in X if vertex.matched_with==None] 
unmatched_vertices_Y = [vertex for vertex in Y if vertex.matched_with==None]

if unmatched_vertices_X is None or unmatched_vertices_Y is None: #We need at least one unmatched PER side
    sys.exit("You need at least one unmatched vertex per side")


vertex_processing_queue = list()
current_vertex = None # type -> Vertex


def explore_neighbors(_vertex: Vertex, should_be_matched):

    for neighbor in _vertex.neighbors:

        neighbor_matched = neighbor.matched_with != None # if it's not matched with anything, then it's unmatched
        edge_in_matching = (_vertex.matched_with == neighbor)

        if (not neighbor.visited) and should_be_matched == edge_in_matching: #not visited, matched based on what we want
            neighbor.predecessor = _vertex #set predecessor for tracking

            if not neighbor_matched: #if it's not matched, then we finally reached the end
                return neighbor
            
            if not neighbor in vertex_processing_queue:
                vertex_processing_queue.append(neighbor)   #add to queue and continue, no repeats          
             
    print([v.label for v in vertex_processing_queue])  #print queue members for each iteration     
    _vertex.visited = True


polarity = False #We want matching, non matching, matching, etc
vertex_processing_queue = unmatched_vertices_Y # initiate with unmatched vertices in y
print([v.label for v in vertex_processing_queue])


# Repeated neighbor explore until finish
while len(vertex_processing_queue) != 0:
    vertex_to_process = vertex_processing_queue.pop(0) # Pop from processing list
    polarity = True if vertex_to_process.group is "X" else False # Matching -> non matching -> matching logic defined by which side it's on
    result = explore_neighbors(vertex_to_process, polarity) 
    if type(result) == Vertex:

        augmented_path = list()
        augmented_path.insert(0, result) # Insert into the beginning of the Augmented Path (since we're backtracking)
        
        x = result.predecessor
        while x:
            augmented_path.insert(0, x)
            x = x.predecessor #Repeated backtracking until vertex with no predecessor   
        
        print(f'Augmented Path Found: {[v.label for v in augmented_path]}')
        break        
