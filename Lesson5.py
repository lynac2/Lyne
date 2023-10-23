# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:20:42 2023

@author: lynen
"""

#range  : loop
# range(X) de 0 a X
n=int(input("Enter the value of n:"))
for i in range(1,n+1): #first,end
    q=i**2
    print(q)

n=int(input("Enter the value of n:"))
for i in range(1,n+1,2): #first,end,le pas
    q=i**2
    print(q)
    
#exemple somme jusqu'à 6

sum=0
for i in range(6):
    sum=sum+i
    print(f"The value if the sum is in each iteration:{sum}")
print("The sum is valid {}".format(sum))    

#deux loop

for i in range(4):
    for j in range(3):
        print("i={},j={}".format(i,j))
        
#exercice somme des i

n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print(i)
print('la somme des {} premiers nombres est {}'.format(n,sum))    

#exo sum of another serie
n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n+1):
    f=(i+1)/i**2
    sum=sum+f
    print(i)
print("For n ={} the sum is {: .2f}".format(n,sum))    
#.2f les deux premieres décimal

#exercice factorial of a positive integer

n=int(input("Enter the value of n="))
prod=1
for i in range(1,n+1):
    prod=prod*i
print("The factorial of {} is {}".format(n,prod))

#donner tous les nombes sauf les nombres finissant par zero et debut par zero


for i in range(1,10):
    for j in range(1,10):
        print("{}{}".format(i,j))


#exercice eviter les répétitions
for i in range(1,10):
    for j in range(1,10):
        if i!=j:
            print("{}{}".format(i,j))
        
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            print("{}{}{}".format(i,j,k),end="  ")

#ecerice somme des trois nombre egal a 22

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if i+j+k == 22:
              print("{}{}{}".format(i,j,k),end="  ")
              
  ###Exerice   

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if (i**3)+(j**3)+(k**3) == i*100+j*10+k:
              print("{}{}{}".format(i,j,k),end="  ")          
        
        
        ##Exercice divisor of a positif integer 
        
n=int(input("enter a number n:"))     
i=1
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")
        i=i+1
        
#exerice

n=int(input("Enter a number n:"))
sum=0
for i in range(0,n):
    q=2*i+1
    sum=sum+q
    print(q)
print("The some of the odd number is {}".format(sum))

#verify if its a prime number

n=int(input("Enter a number n:"))
b=True
for i in range(2,n):
    if n%i==0:
        b=False
   
if b==True:
    print("{} is a prime number".format(n)) 
else:
       print("{} is not a prime number".format(n))
       
   #FIBONACCI
n=int(input("Enter a number n:"))
f=0
u1=1
u0=0
for i in range(0,n):
     f=u0+u1
     u0=u1
     u1=f
print(f)     