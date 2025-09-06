import threading
import time

class PathfindingThread(threading.Thread):
    def __init__(self, player, graph, algo_id):
        super().__init__()
        self.player = player
        self.graph = graph
        self.algo_id = algo_id
        self.path = None
        self.cost = None
        self.time = None

    def run(self):        
        if self.algo_id == 1:
            visited = set()
            path_dfs = []
            self.path, self.cost, self.time = self.graph.procuraDFS(self.player, path_dfs, visited)
        elif self.algo_id == 2:
            self.path, self.cost, self.time = self.graph.procuraBFS(self.player)
        elif self.algo_id == 3:
            self.path, self.cost, self.time = self.graph.aStar(self.player)
        elif self.algo_id == 4:
            vis = []
            path_greedy = []
            self.path, self.cost, self.time = self.graph.GreedyAlgorithm(self.player, vis, path_greedy)
        