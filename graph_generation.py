# Générer un graph
# Paramètre de la fonction : orienté, pondéré, taille (nb de sommets), vertices (nombre d'arrêtes)
import random


list_adj = [[]]
list_w = []



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
                
                
                

        return list_adj



