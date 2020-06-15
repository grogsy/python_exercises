from collections import deque, namedtuple

inf = float('inf')

Node = namedtuple('Node', ['label', 'num_stops', 'current_cost'])

class Graph(dict):
    def add_node(self, parent, neighbor=None, cost=inf):
        if neighbor is None or parent not in self:
            self[parent] = {}
        if neighbor is not None:
            self[parent][neighbor] = cost

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        min_cost = inf
                    
        # construct the graph
        graph = Graph()
        for this_node, neighbor, cost in flights:
            graph.add_node(this_node, neighbor, cost)
            
        q = deque([Node(src, 0, 0)])

        while q:
            node = q.popleft()
            # if we are dst we check if the cost for this path is less than the current min_cost
            if node.label == dst:
                min_cost = min(min_cost, node.current_cost)
            # if we are at max current stops(K) and not at src OR the current cost exceeds the min cost we do not proceed any further
            elif node.num_stops > K or node.current_cost > min_cost:
                continue
            # track current cost and num of stops of the neighbors
            else:
                neighbors = graph.get(node.label)
                if neighbors is not None:
                    for neighbor in graph[node.label].keys():
                        q.append(Node(neighbor, node.num_stops + 1, node.current_cost + graph[node.label][neighbor]))

        return min_cost if min_cost is not inf else -1
