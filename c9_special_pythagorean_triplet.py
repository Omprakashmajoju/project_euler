# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 22:54:24 2022

@author: ompra
"""

def main():
    for i in range(1,1000):
        for j in range(1,1000):
            for k in range(1,1000):
                if((i**2)+(j**2)==(k**2))&(i+j+k==1000):
                #if((i**2)+(j**2)==(k**2)):
                    print(i,j,k)
                    print(i*j*k)
main()