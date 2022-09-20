# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:41:08 2022

@author: michel
"""

from random import randint

class Graph:
    def __init__(self, order, weights = None,  directed = False, adjlists = []):
        self.order = order
        self.directed = directed
        if adjlists == []:
            for i in range (order):
                adjlists.append([])
        self.adjlists = adjlists
        if not weights:
            self.weights = weights
        else:
            weights = []
            for i in range (order):
                weights.append(0)
            self.weights = weights
    
    def addedge(self, a, b):
        if not b in self.adjlists[a]:
            self.adjlists[a].append(b)
            if not self.directed:
                self.adjlists[b].append(a)
            return a
        else:
            return 0
'''randint(0,5)*(diff*10+1)'''
def generateRandomGraph(diff):
    G = Graph(10, randint(0,2), randint(0,2))
    for i in range(G.order + randint(0,3)*G.order):
        chosen = G.addedge(randint(0,G.order-1), randint(0,G.order-1))
        if chosen and G.weights:
            G.weights[chosen] = randint(0,15)
    return G

'''G = generateRandomGraph(1)
print(G.adjlists)
if G.weights:
    print(G.weights)'''
    
    
def trie(G):
    L=[]
    for i in range(len(G)):
        L.append((i,len(G[i])))
    for j in range(len(L)-1):
        for w in range(j,len(L)):
             if(L[j][1]<L[w][1]):
                 L[j],L[w]=L[w],L[j]
    
    return L

def _setdom(G,n,i):
    for j in range(i):
        print("n :", n, " et j : ",j)
        print(G[n][j])### set de départ supérieur à 8 ( G[n][j] = 8 or la len(G[n]) = 5)
        print(G[G[n][j]])###
        if G[G[n][j]][-1]!='/':
            print("J'ai marqué" , j)
            G[G[n][j]].append('/')
            print("G : ",G)
    

def setdom(G,L):
    dom=[]
    for i in range(len(L)):
        if G[L[i][0]][-1]!= '/':
            print("J'ai sélectionné" , L[i][0])
            dom.append(L[i][0])
            G = _setdom(G,L[i][0],len(G[L[i][0]])) 
            print("J'ai marqué" , L[i][0]) ##
            print("L : " , L)##
            print("G[L[i][0]] : ", G[L[i][0]])##
            G[L[i][0]].append('/') #TypeError: 'NoneType' object is not subscriptable (Hypothèse : L étant un Tuple, peut-etre que L[i][0] ne peut pas être lu - Réponse : changé le type des éléments i dans L )
    print(G)
    return dom        
M=[[6, 9], [5], [6, 3], [2, 4, 7], [3, 6, 8], [1], [0, 2, 4], [3], [4], [0]]    #[[1,3,4,5],[8,74,9,0,3],[0,2,9,7,35],[1,25,63,83],[2,3,1]] #changer la liste avec une normale

print(setdom(M,trie(M)))