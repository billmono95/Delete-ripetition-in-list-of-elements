# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:54:49 2020

@author: Bill
"""

#example of list

jk = [185,105,2,5,2,15,8,1,7,24,12,7,43,25,12,8,8,5,211]

def remove_ripetition(name):
    

    copy = []

    for i in range(len(name)):
     
    
  
        for j in range(i+1,len(name)):
        
            if (name[i] == name[j]):
             
                copy.append(name[i])
           
    
    print(copy)

    for cancel in copy:
        while cancel in name:
            name.remove(cancel)
    print(name)
            
            
remove_ripetition(jk)            
