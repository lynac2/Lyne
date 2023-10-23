# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 23:52:58 2023

@author: lynen
"""

#how much caracter in a word a use 'len'

message='Good morning'
print(len(message))

#choisir ce qu'on print sur le message pour une lettre, on compte on utilise un index 
print(message[8])

#pour print un mot du message 

print(message[0:4]) #the ending point is excluded so we nedd to add one more to make a word
#ou
print(message[:4]) #on commence debut du mot

print(message[8:11])
#ou
print(message[8:]) #jusqu'a la fin du mot

print(message[-1]) #on aura le dernier index du mot

print(message[0:-1]) #on a tout le mot sauf la derniere lettre

#mettre en majuscule
print(message.upper())
#mettre en minuscule
print(message.lower())

#donner le nombre de fois ou la lettre apparait
print(message.count('g'))

#trouves la position de la premiere apparation de la lettre rechercher
print(message.find('d'))

message2= message.replace('morning','afternoon')
print(message2)

print(message.count('ing'))

#ce quon peut utiliser avec les strings
print(dir(str))

#Pour les conditions on utilise if_____:
    
num=input('Enter an interger:') #input pour dmda l'utilisateur
num=int(num)
if num<5:
    print('Its less than five')
else:
    print('Its greater than or equal to five')  

#even or odd exerice pair ou impair
num=int(input("enter the number:"))
if num%2==0:
    print("the number {} is an even number".format(num))
else:
    print(f"the number {num} is an odd number") #une synthaxe pour un string pareil qu'au dessus
    
#si on a plus d'une condition on utilise elif
#if____: elif___________: else______: (a la fin)

#exercice sur les grades

num= float(input("note of the student:"))

if num<5:
    print('Suspended')
elif num>=5 and num<7:
        print('Approved')
elif num>=7 and num<9:
    print("Great")
else:
    print('Very great')
    
#Ecerice BMI

w=float(input("Enter your weight"))
h=float(input("Enter your height"))
height= float(h[-2:])
unit=h[-2:]
if unit =='cm':
    height=height/100
bmi=w/(h**2)
if bmi<18.5:
    print("Your bmi is {} and you are underweight".format(bmi))
elif bmi>=18.5 and bmi<25:
    print("Your bmi is {} and you are normal weigth".format(bmi))
elif bmi>=25 and bmi<30:
    print('Your bmi is {} and you are overweight'.format(bmi))
else:
    print('Your bmi is {} and you are in obesity'.format(bmi))
    
#exercice 
n1= int(input("Enter a natural number:"))
n2= int(input("Enter an other natural number:"))
n=n1/n2
r=n1%n2
if r==0:
    print("The number (} is divisible by (} and the quotient is (J".format (n1, n2,n))
else:
    print("The number (} is not divisible by (f but the remainder is ( ".format (n1, n2, r))

#exercice minimum

n1= int(input("Enter a natural number:"))
n2= int(input("Enter an other natural number:"))
if n1<n2:
    print("{} est plus grand que {}".format(n2,n1))
elif n1==n2:
    print("{} est egal à {}".format(n1,n2))
else:
    print("{} est plus grand que {}".format(n1,n2))
    
#exercice bill 
unit=int(input('Enter the number of unit:'))
if unit<=100:
    charge=0
elif  unit>100 and unit<=200:
    charge=5*(unit-100)
else:
     charge=10*(unit-200)+100*5
     

print ("Your bill is {}".format(charge))   
    