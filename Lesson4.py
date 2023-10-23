# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:30:08 2023

@author: lynen
"""

#while synthaxe

num =int(input("enter an integer value:"))
ndiv=0
while num>0:
    res=num//3
    print("the integer division of {} by 3 gives:{}".format(num,res))
    ndiv=ndiv+1
    print("Number of division so far:{}".format(ndiv))
print("We are done")    





num =int(input("enter an integer value:"))
ndiv=1

while ndiv<num:
    res=num//ndiv
    print("The integer division of {} by {} gives:{}".format(num,ndiv,res))
    ndiv=ndiv+1
    
print("We are done")
print("The total num of the division :{}".format(ndiv))    

#write a code to print sum of the first matural number

num=1
sum=0

while num<=10:
    sum=sum+num
    num=num+1
print(f"the sum of the first 10 natural number is :{sum}")    


#write a code using loop and print their average value on the screen
sum=0
i=10
while i>0:
    num=int(input(print("Enter a number:")))
    sum=sum+num
    i=i-1
print('the average is',sum/10.0)    

#exercice triangle etoile

i=1
num=int(input(print("Enter a number:")))
while i<=num:
    print("*"*i)
    i=i+1

#exercice finding the factorial of a givin number using loop
num=int(input(print("Enter a number:")))
i=num
f=1
while i>0:
    
    f=f*i
    i=i-1
print("The factoriel of {} is {}".format(num,f))
