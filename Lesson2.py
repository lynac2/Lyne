# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 10:57:40 2023

@author: lynen
"""

name ='lyne' 
name ='lyne' #on ne met pas de chiffre avant une variable * et trop long
Name = 'Lyne'

#exercice de physique

R = 0.008206
n=0.5
T=298.15
V=2.5
P=n*R*T/V
print("At temperature {} K thepressure is {} atm {}".format(T,P,R)) 
# .format(R,T) avec {} pour completer un print 

#On utilise '='  declarer une variable et '==' pour comparer deux variables
n = int(21)
n=n/12
print(n)

#on ecris les complexs:
a=5
v=2
b=complex(a,v) #premier reel deuxieme imaginaire
print(b)

#cette opeation "//" fait une division en nombre naturel pas de decimal
# cette operation ' %' donne la reste de la division euclidienne, le modulo

#exercice operation0
a=5
b=3
c=2.5
d=(2*a+b**2)/c
print(d)

#si on veut demander qlq chose a l'utilisateur on utilise input
#v=input("enter your name")
print(v)

#+ le mettre en float
#n=float(input('enter a number'))

#exercice phyisque
import math 
r=12
h=5
v=(1/3)*h*math.pi*r**2
print(v)

#import math pour des operaions 
num=float(input('enter a numero:'))
num2=float(input('enter an anoher numero:'))
sum=num+num2
product=num*num2
print('the sum of {} and {} is'.format(num,num2))
print('the product of {} and {} is'.format(num,num2))

celsius = float(input("enter the temperature in celsius"))
print("temperature in kelvin is "+celsius+273.15)

length=float(input('enter the length'))
length=1.5
a=length*length*6
v=length*length*length
print('the area of the cube is: {} and the volume is: {} for the length: {}'.format(a,v,length))

#exercice 

money10 = input('how much do you have bills of 10 euros')

money20 = input('how much do you have bills of 20 euros')

money50 = input('how much do you have bills of 50 euros')

bank=10*money10+20*money20+50*money50
print('you have {} bills of 10, {} bills of 20 and {} bills of 50 and you have {} in your bank account'.format(money10,money20,money50,bank))

#exercice math 

import math as m
r=float(input('write the radius of the circle in cm'))
a=2*m.pi*r
v=m.pi*r**2
print("l'air du cercle est {} et le volume {} pour un radius de {}".format(a,v,r))

#puissance r**6 and r.math.exp(6)

