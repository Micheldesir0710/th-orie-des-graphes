# Générer un graph
# Paramètre de la fonction : orienté, pondéré, taille (nb de sommets), vertices (nombre d'arrêtes)
import random


list_adj = [[]]
list_w = []



def graph(list_adj,taille,weight,oriented,vertices):
    count = 0
    if oriented == True:
        x = random.randint(1,taille) #choix aléatoire du nombre "supposé" de valeurs par sommet 
    
        for i in range(taille):
            z=[] #initialisation de la liste d'adjacence du sommet i
            for j in range(x):
                k = random.randint(0,taille-1) #choix aléatoire d'une valeur de sommet
                if k not in z and k != i: #eviter les doublons (deux arcs vers le même sommet) et les arcs de sommet a vers sommet a (boucle)
                    z.append(k) #ajout du sommet k à la liste d'adjacence du sommet i

            list_adj.append(z) #à la fin de la boucle, on ajoute la list d'adjacence du sommet j
            
            if weight == True: 
                list_w.append(random.randint(1,10)) #list de poids pour chaque sommet, avec une valeur entre 1 et 10
            else:
                list_w.append(1) #list de poids qui est égale pour tous les sommet (poids pour chaque sommet = 1)

        del list_adj[0] #suppression du premier élément de la liste qui est une liste vide


       
        return list_adj

##non oriented
    if oriented == False:
        list_adj = [ [] for i in range(taille) ]    # initialisation d'une liste avec à l'intérieur un nombre de listes égale à la taille
        
        while count<vertices:   # tant que le nombre d'arrêtes n'est pas atteint, on continue
            for i in range(taille):
                k = random.randint(0,taille-1) #choix aléatoire d'une valeur de sommet
                if k != i and k not in list_adj[i] and count<vertices and k not in list_adj[k]: #eviter les doublons (deux arcs vers le même sommet) et les arcs de sommet a vers sommet a (boucle)
                    list_adj[i].append(k) #ajout d'une arrêtes dans un sens
                    list_adj[k].append(i) #ajout de la même arrête dans l'autre sens
                    count +=1     #incrémente de 1 le nombre d'arrête à chaque passage
                
                if weight == True:
                    list_w.append(random.randint(1,10)) #list de poids pour chaque sommet, avec une valeur entre 1 et 10
                else:
                    list_w.append(1) #list de poids qui est égale pour tous les sommet (poids pour chaque sommet = 1)
                
                
                

        return list_adj #la fonction retourne la list d'adjacence du graph