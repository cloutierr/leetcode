"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def visit(self, node: Optional['Node'], visited: dict[Node: Node]):
        if node is None:  # base case
            return None
        if node in visited:
            return visited[node]  # return already created clone
        
        clone = Node(node.val, None)  # initialize untraversed clone
        visited[node] = clone  # map original node to clone for other clones to access on their visits to node

        for n in node.neighbors:
            clone.neighbors.append(self.visit(n, visited))  # recurse to update clone's neighbors

        return clone

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Alright, this one seems simple enough. We need to keep a set of visited nodes so that we don't visit any node more than once.
        Beyond that, we can use a recursive visit() function to explore all the neighbors and their neighbors--cloning the graph and adding visited nodes to the visited array as we go.
        '''
        visited = dict()   # map original node to its clone so we can access the clone
        return self.visit(node, visited)
