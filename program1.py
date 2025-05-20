# -*- coding: utf-8 -*-
"""
Created on Tue May 20 11:30:37 2025

@author: user
"""

class Cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def multi(self):
        return self.a*self.b
    def div(self):
        if self.b!=0:
            return self.a/self.b
        else:
            print("error")
            
a=float(input("enter a number"))
b=float(input("enter another number"))
operator=input("choose-> add,sub,multi,div :    ")

calculator = Cal(a,b)
if operator=="add":
    print("answer",calculator.add())
elif operator=="sub":
    print("answer",calculator.sub())
elif operator=="multi":
        print("answer",calculator.multi())
elif operator=="div":
            print("answer",calculator.div())
            
else: print("error")

