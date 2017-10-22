>>> from heapq import heappop, heappush
>>> def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

        
>>> class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso 
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def shortest(self, v): # 
        q = [(0, v, ())] 
        dist = dict() 
        visited = set() 
        while len(q) > 0: 
            (l, u, p) = heappop(q)
            if u not in visited: 
                visited.add(u) 
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	
            p = (u, p) 
            for n in self.vecinos[u]: 
                if n not in visited: 
                    el = self.E[(u,n)] 
                    heappush(q, (l + el, n, p)) 
        return dist

>>> g = Grafo()#Para grafo de 5 nodos y 10 aristas
>>> g.conecta('a', 'b', 2)
>>> g.conecta('a', 'c', 1)
>>> g.conecta('a', 'd', 4)
>>> g.conecta('a', 'e', 6)
>>> g.conecta('b', 'c', 6)
>>> g.conecta('b', 'd', 3)
>>> g.conecta('b', 'e', 7)
>>> g.conecta('c', 'd', 7)
>>> g.conecta('c', 'e', 5)
>>> g.conecta('d', 'e', 8)
>>> print(g.shortest('e'))
>>> print(g.shortest('a'))

>>> g2 = Grafo() #Para grafo de 10 nodos y 20 aristas
>>> g2.conecta('a','b', 1)
>>> g2.conecta('a','c', 4)
>>> g2.conecta('a','d', 2)
>>> g2.conecta('b','c', 2)
>>> g2.conecta('b','e', 4)
>>> g2.conecta('b','f', 7)
>>> g2.conecta('c','d', 3)
>>> g2.conecta('c','f', 4)
>>> g2.conecta('c','h', 5)
>>> g2.conecta('d','h', 9)
>>> g2.conecta('e','f', 5)
>>> g2.conecta('e','i', 8)
>>> g2.conecta('f','g', 6)
>>> g2.conecta('f','i', 2)
>>> g2.conecta('f','j', 3)
>>> g2.conecta('g','h', 7)
>>> g2.conecta('g','j', 2)
>>> g2.conecta('i','j', 9)
>>> g2.conecta('h','j', 10)
>>> print(g2.shortest('a'))

>>> g3 = Grafo() #Para grafo de 15 nodos y 30 aristas
>>> g3.conecta('a', 'b', 1)
>>> g3.conecta('a', 'f', 5)
>>> g3.conecta('b', 'f', 3)
>>> g3.conecta('b', 'c', 2)
>>> g3.conecta('c', 'd', 3)
>>> g3.conecta('c', 'h', 4)
>>> g3.conecta('d', 'e', 4)
>>> g3.conecta('e', 'h', 8)
>>> g3.conecta('e', 'j', 10)
>>> g3.conecta('f', 'h', 9)
>>> g3.conecta('f', 'g', 6)
>>> g3.conecta('f', 'k', 9)
>>> g3.conecta('g', 'h', 7)
>>> g3.conecta('g', 'i', 8)
>>> g3.conecta('g', 'l', 7)
>>> g3.conecta('g', 'k', 10)
>>> g3.conecta('h', 'i', 2)
>>> g3.conecta('h', 'j', 7)
>>> g3.conecta('i', 'j', 8)
>>> g3.conecta('i', 'l', 5)
>>> g3.conecta('i', 'n', 6)
>>> g3.conecta('j', 'n', 2)
>>> g3.conecta('k', 'l', 3)
>>> g3.conecta('k', 'o', 9)
>>> g3.conecta('l', 'm', 6)
>>> g3.conecta('l', 'o', 4)
>>> g3.conecta('m', 'n', 8)
>>> g3.conecta('m', 'o', 4)
>>> g3.conecta('n', 'o', 3)
>>> print(g3.shortest('a'))
