# -*- coding: utf-8 -*-

class UndirectWeigtedGraph:
  """An UndirectedGraph g contains a dictionary (g.neighbor_dict) which
  maps node identifiers (keys) to lists of neighboring nodes (values).
  g.neighbor_dict[node] returns a list [node2, node3, node4] of neighbors.
  Node identifiers can be any non-mutable Python type (e.g., integers,
  tuples, strings, but not lists)."""

  def __init__(self):
    """UndirectedGraph() creates an empty graph g.
    g.neighbor_dict starts as an empty dictionary.  When nodes are
    added, the corresponding values need to be inserted into lists."""
    self.neighbor_dict = {}

  def __getitem__(self, key):
    return self.neighbor_dict[key]

  def __iter__(self):
    return (k for k in self.neighbor_dict)

  def HasNode(self, node):
    """Does not use the dict.keys() method, which would generate a 
    new list of all nodes each time this is called."""
    return node in self.neighbor_dict

  def AddNode(self, node):
    """Uses HasNode(node) to determine if node has already been added."""
    if not self.HasNode(node):
      self.neighbor_dict[node] = []

  def AddEdge(self, node1, node2):
    """
    Add node1 and node2 to network first
    Adds new edge 
    (appends node2 to neighbor_dict[node1] and vice-versa, since it's
    an undirected graph)
    Do so only if old edge does not already exist 
    (node2 not in neighbor_dict[node1])
    """
    self.AddNode(node1)
    self.AddNode(node2)
    if node2 not in self.neighbor_dict[node1]:
      self.neighbor_dict[node1].append(node2)
    if node1 not in self.neighbor_dict[node2]:
      self.neighbor_dict[node2].append(node1)

  def GetNodes(self):
    """g.GetNodes() returns all nodes (keys) in neighbor_dict"""
    return self.neighbor_dict.keys()

  def GetNeighbors(self, node):
    """g.GetNeighbors(node) returns a copy of the list of neighbors of
    the specified node.  A copy is returned (using the [:] operator) so
    that the user does not inadvertently change the neighbor list."""
    return self.neighbor_dict[node][:]


###
# Routines
#

def DjikstraMinPath(graph, from_node, target_node, weight_func):
  links = {n:None for n in graph}
  inf = float('inf')
  edge_weight = lambda n1,n2: 1.*(weight_func(n1)+weight_func(n2))/2
  cumulative_weights = {n:inf for n in graph}
  cumulative_weights[from_node] = 0
  for n in graph[from_node]: cumulative_weights[n] = edge_weight(from_node, n)
  unvisited_nodes = graph.GetNeighbors(from_node)
  while unvisited_nodes:
    n1 = min(unvisited_nodes, key=lambda n: cumulative_weights[n])
    if n1 == target_node:
      break
    unvisited_nodes.remove(n1)
    for n2 in graph[n1]:
      if cumulative_weights[n2] > cumulative_weights[n1] + edge_weight(n1,n2):
        cumulative_weights[n2] = cumulative_weights[n1] + edge_weight(n1,n2)
        links[n2] = n1
        unvisited_nodes.append(n2)
  path = []
  n = target_node
  while n and n != from_node:
    path.insert(0, n)
    n = links[n]
  path.insert(0, from_node)
  return path