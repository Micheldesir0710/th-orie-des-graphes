# Générer un graph
# Paramètre de la fonction : orienté, pondéré, taille (nb de sommets), vertices (nombre d'arrêtes)
import random


list_adj = [[]]
list_w = []
#taille = 5
#oriented = False
#weight = True   #True = random de poid entre 1 et 10 ou si False = 1


def graph(list_adj,taille,weight,oriented,vertices):
    count = 0
    if oriented == True:
        x = random.randint(1,taille)
    
        for i in range(taille):
            z=[]
            for j in range(x):
                k = random.randint(0,taille-1)
                if k not in z and k != i: #eviter les doublons (deux arcs vers le même sommet) et les arcs de sommet a vers sommet a (boucle)
                    z.append(k)

            list_adj.append(z)
            
            if weight == True:
                list_w.append(random.randint(1,10))
            else:
                list_w.append(1)

        del list_adj[0]


        '''print("list_adj : ", list_adj)
        print("list_w : ", list_w)
'''
        return list_adj

##non oriented
    if oriented == False:
        list_adj = [ [] for i in range(taille) ]
        
        while count<vertices:
            for i in range(taille):
                k = random.randint(0,taille-1)
                if k != i and k not in list_adj[i] and count<vertices and k not in list_adj[k]:
                    list_adj[i].append(k)
                    list_adj[k].append(i)
                    count +=1      
                
                if weight == True:
                    list_w.append(random.randint(1,10))
                else:
                    list_w.append(1)
                
                
                
        '''print("list_adj_non_o : ",list_adj)
        #print("list_w : ", list_w)
        print("number of vertices : ",count)
'''
        return list_adj


graph(list_adj,1000,False,False,15000)


# à tester avec noeud empty
# list_adj_non_o :  [[9, 1, 2, 6, 7], [0, 5, 7, 6], [0, 6], [5, 4, 6], [3, 7, 9], [3, 1], [9, 0, 2, 3, 1], [4, 1, 0], [], [0, 6, 4]]
# number of vertices :  15