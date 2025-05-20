# -*- coding: utf-8 -*-
"""
Created on Tue May 20 12:11:02 2025

@author: user
"""



class Num:
    def __init__(self,numbers):
        self.numbers=numbers
        
    def count_num(self):
        result={}
        
        for i in range(1,10):
            count=0
            for num in self.numbers:
                if num%i==0:
                    count+=1
                    result[i]=count
            return result
        
list=[1,2,8,9,12,46,76,82,15,20,30]
counter=Num(list)
output=counter.count_num()
print("result:  ", output)
            