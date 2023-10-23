# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#cours 7
#ex1 variable length list of numeric values
value=input("enter a numeric value ")
list_a=[]
sum=0
while value!="" :
    list_a.append(value)
    value=float(value)
    sum=sum+value
    value=input("Enter a numeric value:")
average=sum/len(list_a)
print("The arithmetic mean is {}".format(average))

#ex2 greeting code , ask name of people
phrase=input("Enter a name:")
nb_people=0
list_phrase=phrase.split()
for i in list_phrase:#plus pratique pour passer dans la list for
    print('Hi', i)
    nb_people+=1

print("welcome all {}".format(nb_people))

#ex3 molecular mass based on the nb on atom of each type
List_atom=["H","C","N","O","S","Cl"]
list_massatom=[1.008,12.011,14.007,15.999,32.065,35.453]
tot=0
for i in range(len(List_atom)):
    n=int(input("Nombre de {}".format(List_atom[i])))
    tot=n*list_massatom[i]+tot
print(tot)

#ex4 des polynomes (demander a l'utilisateur le deg max , donner les num devant chaque x et ensuite donner un x pour ensuite le calculer)

list_pol=[]
degree=int(input("Enter the max degree of your polynomial"))
for i in range(degree):
    nb=float(input("Enter the value of x in order 0 to n:"))
    list_pol.append(nb)
print(list_pol)

x=float(input("Enter x:"))
som=0
for i in range (degree):
    som=som+(x**i)*list_pol[i]
print("The equation for x={} is {}".format(x,som))

#les fonctions
#exemple
def hf():
    print("Hello world")
hf()

def add(x,y):
    c=x+y
    print(c) #or return c
add(5,4)
#or it's the same thing
def add(x,y):
    c=x+y
    return c 
print(add(5,4))

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
print(add(5,4))

def hf():
    return "hw"
print(hf())

def hello_f():
    return "hellocollege"
print(hello_f().upper())

def hello(wish):
    return 'is {}'.format(wish)
print(hello("mrect"))

def wish(name,msg):
    print("Hello",name+' '+msg)
wish("Mrcet",'Goodmorning!')

def func(a,b=5,c=10):
    print("a is ",a,"and b is ",b,"and c is ",c)
func(3,7)
func(25,c=24)
func(c=50,a=100)
