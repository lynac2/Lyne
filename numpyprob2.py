#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:59:51 2023

@author: Lynenaccache
"""
#exo1
#Write a NumPy program to create a vector with values from 0 to 20 and change 
#the sign of the numbers in the range from 9 to 15.
import numpy as np
import math as mp


for i in range (0,21):
    d=np.arange(21) #vecteur 
    if i>=9 and i<=15:
        d[i]=-d[i]
    print(d[i])
#exo2    
#Write a NumPy program to create a vector with values ranging 
#from 15 to 55 and print all values except the first and last.
e=np.arange(15,56)    
print(e[1:-1]) 

#exo3
#Write a NumPy program to create a 3X4 array and iterate over it.

h=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(h)
for i in h:
    for j in i:
        print(j)
        
#Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.

d=np.linspace(5,50,10)
print(d)

#Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
d=np.random.randint(0,11,5)
print(d)

#Write a NumPy program to multiply the values of two given vectors.

d=np.array([2,5,7])
h=np.array([9,10,3])
print(d*h)

#Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.


h=np.random.randint(10,22,size=(3,4))    
print(h)   
#Write a NumPy program to find the number of rows and columns in a given matrix.

h=np.array([[10,11,12,13],[14,15,16,17],[18,19,10,21]])
f=0
n=0
for i in  h:
    for j in i:
        n=n+1
    f=f+1
r=n/f    
print(h)
print("The colomn of the matrix is {}".format(r))
print("The row of the matrix is {}".format(f))

#or 

h=np.array([[10,11,12,13],[14,15,16,17],[18,19,10,21]])
f = len(h)
r = len(h[0])
print(h)
print("The colomn of the matrix is {}".format(r))
print("The row of the matrix is {}".format(f))


#Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.

m = np.zeros((4, 4))   # Create a 4x4 matrix with zeros 
for i in  range(4):
    for j in range(4):
        if (i+j)%2==0 :
            m[i,j]=0
        else:
            m[i,j]=1
print(m)


#Write a NumPy program to find common values between two arrays.
#Expected Output:
#Array1: [ 0 10 20 40 60]
#Array2: [10, 30, 40]
#Common values between two arrays:
#[10 40]

h=np.array([0,10, 20, 40, 60])
d=np.array([10, 30, 40])
list=[]
for i in h:
    for j in d:
        if i==j:
            list.append(i) #pour ajouter un élément à la fin d'une liste
print("Les éléments en commun avec les deux listes sont ",list)            


#or

h=np.array([0,10, 20, 40, 60])
d=np.array([10, 30, 40])
list=[]
for i in range(len(h)):
    for j in range(len(d)):
        if h[i]==d[j]:
            list.append(h[i]) #pour ajouter un élément à la fin d'une liste
print("Les éléments en commun avec les deux listes sont ",list)    


   

h=np.array([10, 10, 20, 20, 30 ,30])
f=np.array([[1 ,1],[2 ,3]])

list=[]
for i in range (len(h)-1):
        if h[i]==h[i+1]:
            list.append(h[i])
        
print(list)            

#Write a NumPy program to compute the cross product of two given vectors.



v = np.array([1, 2, 3])
h = np.array([4, 5, 6])


c= [v[1]*h[2]-h[1]*v[2],v[2]*h[0]-v[0]*h[2],v[0]*h[1]-v[1]*h[0]]


print("Cross product of the two vectors:", c)

#Write a NumPy program to convert cartesian coordinates to polar coordinates of a 
#random 10x2 matrix representing cartesian coordinates.
#Expected Output:
#[ 0.89225122 0.68774813 0.20392039 1.22093243 1.24435921 1.00358852
#0.37378547 0.8534585 0.31999648 0.567451 ]
#[ 1.02751197 1.26964967 0.02567519 0.85386412 0.73152767 0.45822494
#1.5063455 1.47389983 0.80818521 0.33001182]


c = np.random.rand(10, 2)
r = np.sqrt(c[:, 0] ** 2 + c[:, 1] ** 2)
theta = np.arctan(c[:, 1], c[:, 0])
print(c)
print(r)
print(theta)

