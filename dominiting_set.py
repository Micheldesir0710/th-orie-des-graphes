# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:41:08 2022

@author: michel
"""

from graph import graph


#La fonction trie prend en paramètre un graph et retourne une liste composé de 
#couple trié en ordre décroissant de la position dans la liste d'adjacence du graphe et sa longueur    
    
def trie(G):
    L=[]
    for i in range(len(G)):
        L.append((i,len(G[i])))
    for j in range(len(L)-1):
        for w in range(j,len(L)):
             if(L[j][1]<L[w][1]):
                 L[j],L[w]=L[w],L[j]
    
    return L
#La fonction _setdom permet de marqué les élément se trouvant à l'intérieur d'une liste d'adjacence
def _setdom(G,n,i):
    for j in range(i):
        if G[G[n][j]][-1]!='/':
            print("J'ai marqué" , j)
            G[G[n][j]].append('/')
    return G
    
#la fonction setdom créer un fichier retournant un graphe, sa liste d'adjacence et son dominiting set 
def setdom(G,L):
    dom=[]
    fichier = open("set.txt","w")
    fichier.write("Le graphe G est : [")
    for i in range(len(G)-1):
        fichier.write("" + str(i) + ", ")
    fichier.write("" + str(len(G)) + "]\n")
    fichier.write("\nLa liste d'adjacence du graphe G est : [")
    for i in range(len(G)):
        fichier.write("[")
        for j in range(len(G[i])-1):
            fichier.write("" + str(G[i][j]) + ", ")
        if(i+1==len(G)):
            fichier.write("" + str(G[i][-1]) + "] ")
        else:
            fichier.write("" + str(G[i][-1]) + "], ")
    fichier.write("]\n")
    
    for i in range(len(L)):
        if G[L[i][0]][-1]!= '/':
            print("J'ai sélectionné" , L[i][0])
            dom.append(L[i][0])
            G = _setdom(G,L[i][0],len(G[L[i][0]])) 
            print("J'ai marqué" , L[i][0]) ##
            G[L[i][0]].append('/')
    fichier.write("\nLe dominiting set du graphe G est: [")
    for i in range(len(dom)-1):
        fichier.write("" + str(dom[i]) + ", ")
    fichier.write("" + str(dom[-1]) + "] ")    
    fichier.close()
    return dom 

       
M=graph([[]],1000,False,False,15000)   

print(setdom(M,trie(M)))