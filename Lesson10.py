#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:36:02 2023

@author: Lynenaccache
"""
import math 
import numpy as np  #for numerical analysis and diff from a list
#numpy store  a data in 32 data and list binary w size, ref count,object value, object size 
#numpy is faster ti read bc of his faster memory 

n=np.arange(6)



#basic

a=np.array([1,2,3],dtype='int32')
print(a)

b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

#get dimension show row :
a.ndim

#size show size :

a.itmesize

#tout les bytes: for all the element 
a.nbytes

#get row and colum :
b.shape

#what kind of data is there :
a.dtype    

#get number of element:
a.size
    


c=np.array([[9.0,'c',7.0],[6.0,5.0,4.0]])
print(b)
c.shape
c.dtype   

d=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(d)

#get a specific element:
d[1,5] #fist row ad 5 colomn on commence a zero

#d[ligne,colonne]

#get a specific row 
d[0,:]

#get a specific column
d[:,2]

d[-1,:] #derniere ligne

d[0,1:-1:2]   #premier row, 2e element in a row (index one), 3e stop index, 4e step size

d[0,::2] #les impaire de la premieres ligne 
d[1,::2] #les paires de la deuxieme 


#matrice de zero
np.zeros((4,3,2)) #1: dimensions ou le nb de matrice,2:lignes,3:colonne
#matrice    vec le meme nombre
np.full((2,2),99)


#des nombres au hasard decimal 
np.random.rand(4,2)

#matrice identite 
np.identity(4) #dim 4

#repeat array
s=np.array([[1,2,3]]) #repete la ligne dans une autre colonne
r1=np.repeat(s,3,axis=0)
print(r1)

#exo
l=np.array([[1,0,1]])
r2=np.repeat(l,3,axis=0)
r2[1,1]=2
print(r2)

f=np.ones((5,5))
z=np.zeros((3,3))
z[1,1]=9
f[1:4,1:4]=z #leslignes de 1 à 4 et les colonnes de 1 à 4 de F dans z
print(f)


#ajddition

a=np.array([1,2,3,4])
b=np.array([1,0,1,0])
print(a+b)

#mutiplication de deux matrices avec matmul
import math 
import numpy as np 
#faire une matrice hasard 
d=np.random.rand(2,3)
print(d)

e=np.random.randint(-5,5,size=(3,2)) #hasar de -5 à 5
print(e)

print(np.matmul(e,d))


#determinant 

d=np.random.randint(-10,10,size=(4,4))
print(d)

e=np.random.randint(-4,10,size=(3,3)) #hasar de -5 à 5
print(e)
print(np.linalg.det(d))
print(np.linalg.det(e))

#minimum

s=np.array([[1,2,3],[4,-2,6]])
print(np.min(s))
print(np.max(s,axis=1))#ala colonne la plus grande
print(np.max(s,axis=0)) #la ligne la plus grand een comparant toute la matrice
print(np.min(s,axis=0)) #axis =1 colonne et 0 est ligne

#somme
print(np.sum(s)) #la somme de toute la matrice 
print(np.sum(s,axis=0)) #somme par colonne

arr=np.array([[1,2,3]])
r=np.repeat(arr,3,axis=1) #repete le nombre dans la mm ligne
print(r)

#de -2 en 2 list de 21 nombre entre -2 et 2 decimal
import numpy
npoint=21
values=numpy.linspace(-2.0,2.0,npoint)
print(values)

import numpy 
vect=numpy.arange(9)
print(vect)