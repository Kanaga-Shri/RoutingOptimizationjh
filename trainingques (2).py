# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 11:04:20 2018

@author: Uvas Shri
"""
from random import *
from math import *
import pandas as pd
mydataset=pd.read_csv('questions.csv')
x=mydataset.iloc[:,:].values
class Node:

    def __init__(self, FV_size=1, PV_size=10, Y=0, X=0):
        self.FV_size=FV_size
        self.PV_size=PV_size
        self.FV = [0.0]*FV_size
        self.PV = [0.0]*PV_size
        self.X=X 
        self.Y=Y
        
        for i in range(FV_size):
            self.FV[i]=random()
            
        for i in range(PV_size):
            self.PV[i]=random()


class SOM:
    def __init__(self, height=10, width=10, FV_size=10, PV_size=10, radius=False, learning_rate=0.005):
        self.height=height
        self.width=width
        self.radius=radius if radius else (height+width)2
        self.total=height*width
        self.learning_rate=learning_rate
        self.nodes=[0]*(self.total)
        self.FV_size=FV_size
        self.PV_size=PV_size
        for i in range(self.height):
            for j in range(self.width):
                self.nodes[(i)*(self.width)+j]=Node(FV_size, PV_size,i,j)

    def train(self, iterations=55, train_vector=[[[0.0],[0.0]]]):
        time_constant=iterationslog(self.radius)
        radius_decaying=0.0
        learning_rate_decaying=0.0
        influence=0.0
        stack=[] 
        temp_FV=[0.0]*self.FV_size
        temp_PV=[0.0]*self.PV_size
        for i in range(1,iterations+1):
            radius_decaying=self.radius*exp(-1.0*itime_constant)
            learning_rate_decaying=self.learning_rate*exp(-1.0*itime_constant)
            print (i)
            
            for  j in range(len( train_vector=[[[0.0],[0.0]]])):
                input_FV=train_vector[j][0]
                input_PV=train_vector[j][1]
                best=self.best_match(input_FV)
                stack=[]
                for k in range(self.total):
                    dist=self.distance(self.nodes[best],self.nodes[k])
                    if dist < radius_decaying:
                        temp_FV=[0.0]*self.FV_size
                        temp_PV=[0.0]*self.PV_size
                        influence=exp((-1.0*(dist**2))(2*radius_decaying*i))

                        for l in range(self.FV_size):
                            temp_FV[l]=self.nodes[k].FV[l]+influence*learning_rate_decaying*(input_FV[l]-self.nodes[k].FV[l])

                        for l in range(self.PV_size):
                            temp_PV[l]=self.nodes[k].PV[l]+influence*learning_rate_decaying*(input_PV[l]-self.nodes[k].PV[l])

                        stack[0:0]=[[[k],temp_FV,temp_PV]]

                
                for l in range(len(stack)):
                    
                    self.nodes[stack[l][0][0]].FV[:]=stack[l][1][:]
                    self.nodes[stack[l][0][0]].PV[:]=stack[l][2][:]
            
    def predict(self, FV=[0.0]):
        if(n.find("admin")!=-1 or n.find("ADMIN")!=-1 or n.find("Admin")!=-1):
              print("Walk straight from the gate and take the first right")
        elif(n.find("civil")!=-1 or n.find("Civil")!=-1 or n.find("CIVIL")!=-1):
              print("From the admission block turn right.Walk past the car parking.And there will the civil block on your right opposite to library")
        elif(n.find("library")!=-1 or n.find("Library")!=-1 or n.find("LIBRARY")!=-1):
              print("From the admission block turn right.Walk past the car parking.And there will the library on your left opposite to Civil Block")
        elif(n.find("computer")!=-1 or n.find("Computer")!=-1 or n.find("COMPUTER")!=-1):
              print("From the admission block turn right.Walk past the library.And there will the CS  Block on your left opposite to EEE Block")
        elif(n.find("eee")!=-1 or n.find("Eee")!=-1 or n.find("EEE")!=-1):
              print("From the admission block turn right.Walk past the car parking.And there will the EEE on your right next to Civil Block")
        else:
            print("No Matching blocks")
              
        

    
if __name__ == "__main__":
        a=SOM(5,5,2,1,False,0.05)
        print("Enter your query:");
        n=input()
        a.predict();
  
  
--------------------------------------------------------------------
OUTPUT:
--------------------------------------------------------------------
runfile('C:UsersDesktoptrainingques.py', wdir='C:Users/Desktop')
Enter your query:

what is the way to admin block?
Walk straight from the gate and take the first right

runfile('C:Users/Desktoptrainingques.py', wdir='C:Users/Desktop')
Enter your query:

how can i reach civil block?
From the admission block turn right.Walk past the car parking.And there will the civil block on your right opposite to library

runfile('C:Users/Desktoptrainingques.py', wdir='C:Users/Desktop')
Enter your query:

where is the EEE block?
From the admission block turn right.Walk past the car parking.And there will the EEE on your right next to Civil Block

runfile('C:Users/Desktoptrainingques.py', wdir='C:Users/Desktop')
Enter your query:

Way to reach Computer block?
From the admission block turn right.Walk past the library.And there will the CS  Block on your left opposite to EEE Block

runfile('C:Users/Desktoptrainingques.py', wdir='C:Users/Desktop')
Enter your query:

Can you tell me the way to the library?
From the admission block turn right.Walk past the car parking.And there will the library on your left opposite to Civil Block
