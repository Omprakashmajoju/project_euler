# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:50:46 2022

@author: Omprakash Majoju
"""
"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""
#Sum Square Differance
def main():
    sum_of_sq=0
    sum=0
    for i in range(1,101):
        j=i*i
        sum_of_sq=sum_of_sq+j
        sum=sum+i
    sqs=sum**2
    print(sum_of_sq)
    print(sqs)
    print("Difference is ",sqs-sum_of_sq,"Sum is ",sqs+sum_of_sq)
    
main()