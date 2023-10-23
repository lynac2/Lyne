#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:37:02 2023

@author: Lynenaccache
"""

var=open("name.txt")
for names in var:
    names = names.strip() #enelever les espaces entre deux variables
    print("hello {}".format(names))

var=open("name.txt")
for names in var:
    if "anna" in names:
        names = names.strip() #enelever les espaces entre deux variables
        print("hello {}".format(names))

n=open("name.txt","r") #read file
for name in n:
        print(name)
        
with open("name.txt","r") as f:#second way of reading a file
    pass

#small file below

        
with open("name.txt","r") as f:
    z=f.read()
    print(z)
    
#big file

        
with open("name.txt","r") as f:
    z=f.readlines() #read each line as a list
    print(z)    
    
#read the file with extra line
        
with open("name.txt","r") as f:
    z=f.readline() #READLINE SANS S !!!!!! ligne par ligne
    print(z)
    z=f.readline()
    print(z)
    z=f.readline()
    print(z)
    z=f.readline()
    print(z)
    z=f.readline()
    print(z)
    z=f.readline()
    print(z)

with open("name.txt","r") as f: #enleves les sauts entre les lignes
    z=f.readline() 
    print(z,end='')
    z=f.readline()
    print(z,end='')    

#the error

with open("name.txt","r") as f: 
    f.write("Test")
    
    
n=open("name.txt","w") #writing
#n=open("name.txt","a") #appedning
#n=open("name.txt","r+") #reading and writing
print(n.mode)



#writing starts:
with open("test4. txt", "w") as f:
    f.write("Test")
    f.seek (0)#come back to index f.write("Test")
    f.seek("R")
with open("test2. txt", "w") as f:
    val1='10' 
    val2="nhzag" 
    f.write(val1+val2)
    f.seek (0)
    f.write("Test")
    f.seek(6)
    f.write("z")
    
#copying files:
with open("test.txt", "r") as rf:
    with open("test_copy-txt", "w") as wf:
        for line in rf:
            wf.write(line)
            
#copying your image
with open("python.jpg", "rb") as rf:
    with open("python_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)