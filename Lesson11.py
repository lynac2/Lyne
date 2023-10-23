#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:13:18 2023

@author: Lynenaccache
"""

import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

#exo d'une fonction 
x=np.linspace (-2,2,101) #starting point,ending point,number of point 
y=x**2
print(x)

plt.plot(x,y) #montrer la fonction
plt.title("Graph of x^2 vs x")
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x=np.linspace (0,3*np.pi,500) #starting point,ending point,number of vector
y=x**2
print(x)

plt.plot(x,np.sin(x**2)) #montrer la fonction
plt.title("A simple chirp")
plt.show()





x=np.linspace (-2,2,101) #starting point,ending point,number of point 
y=x**2
print(x)

plt.plot(y) #montrer la fonction
plt.title("Graph of x^2 vs x")
plt.show()




#exo2
x=np.linspace(-2,2,101)
y=x**2
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-1.5,1.5) #zoom de -1.5 à 1.5
plt.ylim(-0.5,2.5)
plt.title("Chart title")
plt.plot(x,y)
plt.show()


#representer plusieurs fonction sur le meme graphe


x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x,y,'go',label='x^2')  # r et g red for green if you add o after g it maake a point
y2=x**4
plt.plot(x,y2,'r',label='^x4') #label rajoute la legende
plt.legend()
plt.show()


#exo 

n=int(input("Enter the number of point for the function: "))
x=np.linspace(-1,1,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.cos(2*np.pi*x)
plt.plot(x,y,label='Body Function (2pix)')
plt.legend()
plt.show()
plt.savefig("cos2pix.png") #to save the graph



#exo

n=int(input("Enter the number of point for the function: "))
x=np.linspace(-1,1,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.cos(2*np.pi*x)
plt.plot(x,y,label='cos(2pix)')
y2=np.sin(2*np.pi*x)
plt.plot(x,y2,label='sin(2pix)')
plt.legend()
plt.title("cos(2pix) and sin(2pix)")
plt.show()
plt.savefig("trigo.png") #to save the graph



#exo

while True:  #si l'utilisateur s'est trompé
    try:
        n = int(input("Enter the number of points for the function: "))
        break
    except ValueError:
        print("Please enter a valid number.")
x=np.linspace(0,4,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.cos(20*np.pi*x)*np.sin(np.pi*x)*np.exp(-x)
plt.plot(x,y,label='cos(20pix)sin(pix)e^-x')
plt.legend()
plt.show()

#exo

n=int(input("Enter the number of point for the function: "))
T=float(input("Enter the temperature(in Kelvin):"))
R=0.08206
Vm=np.linspace(2,10,n)
plt.xlabel("Molar volume(L/mol)")
plt.ylabel("Pressure(atm)")
plt.title("Isotherm(ideal gas)")
p=R*T/Vm
plt.plot(Vm,p)
plt.show()

#s_10_6
xo=int(input("Enter xo: "))
s=float(input("Enter s: "))
d=int(input("Enter the number of point for the function: "))
f=int(input("Enter the number of point for the function: "))
n=int(input("Enter the number of point for the function: "))
x=np.linspace(d,f,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y=(1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - xo) / s)**2)
plt.plot(x,y)
plt.title("Fonctioin de gauss")
plt.legend()
plt.show()
#s_10_7

n=int(input("Enter the number of point for the function: "))
x=np.linspace(0,3,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y,label='sin(3pix)e^(-x)')
y2=np.exp(-x)
plt.plot(x,y2,label='e^-x')
plt.title("sin(3pix)e-x and e-x")
plt.legend()
plt.show()

#s_10_8
while True:
    try:
        n = int(input("Enter the number of point for the function:"))
        break
    except ValueError:
        print("Try again an correct number of point:")
for i in range (0,n):
    x = np.linspace(-1,1,100)
    s = float(input("s:"))
    x0 = float(input("x0:"))
    y = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*((x-x0)*2)/(s**2))
    a = input("line : ")
    nom = input("name ? ")
    plt.plot(x,y,a,label = nom)
 
plt.title("Gaus")
plt.legend()
plt.show()


