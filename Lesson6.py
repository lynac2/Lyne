# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 21:45:15 2023

@author: lynen
"""

#Créer une liste

a=[1,2,"5","Name"]

#ajouter un élment à une liste

a.append("Lyne")
print(a)

#enlevez un élément d'une liste

a.remove(1)
print(a)

#changer un truc dans une liste

a[1]=7 #a[index]=nouveau élément

print(a)

#tuple (,,) et liste [,,]
#tuple inchageable et liste tu peux ajouter enlever mettre etc

i=[1,2,3,4]
smooth=[3.14,7,-2+3j,'water',False,[1,2]]
long_smooth=len(smooth)
print(long_smooth)
print(smooth)
smooth[2:5] #il prend de l'index 2 à 4
#on commence à 0 avec les index 
smooth[:4] #on commence à 0 jusqu'à 3
smooth[::4]

a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print ("First instruction print: {}".format (c))
b[0] = -1
d = []
for e in a:
    d.append (e+1)
print ("Second instruction print: {}".format(d))
d.append (b[0] + 1)
d.append(b[-1] + 1)
print ("Third instruction print: {}". format (d))
print ("Fourth instruction print: {}".format (d[-2:])) 
print ("Fifth instruction print: {}".format(d[:-1])) 
print ("Sixth instruction print: {}".format(d[1:4]))


#exercice carré des nombres entiers 

n=int(input("Entrer un nombre n:"))
listi=[]
for i in range(1,n+1):
    listi.append(i**2)
print(listi)
    
    



