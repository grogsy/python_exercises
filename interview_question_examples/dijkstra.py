inf = float('inf')

class Graph(dict):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self['start'] = {}
        self['fin'] = {}
    
    def add_node(self, parent, neighbor=None, cost=inf):
        if neighbor is None or parent not in self:
            self[parent] = {}
        if neighbor:
            self[parent][neighbor] = cost

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.processed = set()
        self.costs = {}
        self.parents = {}
        for node in graph.keys():
            if node in graph['start']:
                self.costs[node] = graph['start'][node]
                self.parents[node] = 'start'
            elif node == 'start':
                continue
            else:
                self.costs[node] = inf
                self.parents[node] = None
    
    def find_lowest_cost(self):
        try:
            return min((cost for cost in self.costs if cost not in self.processed), key=lambda k: self.costs[k])
        except:
            return None
    
    def __call__(self):
        node = self.find_lowest_cost()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.add(node)
            node = self.find_lowest_cost()
            
        output = ['fin']
        while output[-1] != 'start':
            output.append(self.parents[output[-1]])
        
            
        return '->'.join(reversed(output))
    
# https://imgur.com/a/iOEy2LP
g = Graph()
g.add_node('start', 'a', 2)
g.add_node('start', 'b', 5)
g.add_node('a', 'd', 7)
g.add_node('a', 'b', 8)
g.add_node('b', 'd', 2)
g.add_node('b', 'c', 4)
g.add_node('c', 'd', 6)
g.add_node('c', 'fin', 3)
g.add_node('d', 'fin', 1)

d = Dijkstra(g)
d()
# should return 'start->b->d->fin'
