class Grafo:
    def __init__(self, oriented = False):
        self.oriented = oriented
        self.nodos = []
        self.grafo = {}