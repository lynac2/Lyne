#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:55:23 2023

@author: Lynenaccache
"""

def evenodd():
    num=int(input("Enter a number:"))

    if(num%2)==0:
        print("{0} is even".format(num))  #paire
    else:
        print("{0} is odd".format(num)) #impaire
  ####On utlise try pour dire à l'utilisateur qu'il y a une erreur    
try:
    evenodd()
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")    
finally:
    print("Finished")    
    

def bigger_num (a,b) :
  if a > b :
    return a
  elif a < b :
    return b
  else :
    return a

list = []
for i in range(0,5):
  x = int(input("Enter number : "))
  list.append(x)
print("List created :",list)

for i in range (0,4):
  big = bigger_num(list[i],list[i+1])

print("The biggest number is :",big)






try :
  num = int(input("Enter a number: "))
except ValueError as e :
  print(e)
else:
  if (num%2)==0:
    print("even")
  else:
    print("odd")
#finally:
  #num = int(input("Enter a number: "))







while True:
  try:
    num = int(input("Enter a number: "))
    if (num%2)==0:
      print("even")
    else:
      print("odd")
    break
  except ValueError as e:
    print(e)
  #else: