# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:06:36 2023

@author: Ricardo Ismael Gomez Sanchez
"""

class Grafo:
    def __init__(self, vertices):
        self.V = vertices 
        self.grafo = []
        
    def agregar_arista(self, u, v, w):
        self.grafo.append([u, v, w])
        #Busca el padre del nodo y realiza la compresión de caminos
    def buscar_padre(self, padre, i):
        if padre[i] == i:
            return i
        return self.buscar_padre(padre, padre[i])
    # Une los subconjuntos de los nodos
    def union(self, padre, rango, x, y):
        raiz_x = self.buscar_padre(padre, x)
        raiz_y = self.buscar_padre(padre, y)
        
        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1
        
    def kruskal(self):
        resultado = [] #Aquí se almacenarán las aristas que forman el arbol
        i = 0 #Indice de la siguiente arista a considerar en el grafo ordenado
        e = 0 #Indice del resultado
        # Ordenamos las aristas por su peso de menor a mayor
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        
        padre = []
        rango = []
        # Inicializamos cada elemento en un conjunto separado
        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)
            
        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i += 1
            x = self.buscar_padre(padre, u)
            y = self.buscar_padre(padre, v)
# Si unir estos dos vértices no crea un ciclo, se unen y añaden al arbol
            if x != y:
                e += 1
                resultado.append([u, v, w])
                self.union(padre, rango, x, y)
            print('Expansión del árbol')
            print(resultado)
        
        print("Arbol de expansión mínima:")
        for u, v, peso in resultado:
            print("%d - %d: %d" % (u, v, peso))
            
#
g = Grafo(5)
g.agregar_arista(0, 1, 1)
g.agregar_arista(0, 2, 3)
g.agregar_arista(0, 3, 2)
g.agregar_arista(0, 4, 4)
g.agregar_arista(1, 2, 2)
g.agregar_arista(2, 3, 1)
g.agregar_arista(3, 4, 1)

g.kruskal()
