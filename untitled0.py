# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:41:08 2022

@author: michel
"""

from graph_generation import graph


    
    
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
        if G[G[n][j]][-1]!='/':
            print("J'ai marqué" , j)
            G[G[n][j]].append('/')
    return G
    

def setdom(G,L):
    dom=[]
    for i in range(len(L)):
        if G[L[i][0]][-1]!= '/':
            print("J'ai sélectionné" , L[i][0])
            dom.append(L[i][0])
            G = _setdom(G,L[i][0],len(G[L[i][0]])) 
            print("J'ai marqué" , L[i][0]) ##
            G[L[i][0]].append('/')
            print(len(dom))
    return dom        
M=graph([[]],1000,False,False,15000)   

print(setdom(M,trie(M)))