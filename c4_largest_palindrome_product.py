# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:32:45 2022

@author: Omprakash Majoju
"""
"""
A palindromic number reads the same both ways. The largest palindrome made
 from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        return True
    else:
        return False

def main():
    palindrome_list = []
    for i in range(101, 1000):
        for j in range(101,1000):
            product = i * j
            output = is_palindrome(product)
            if output == True:
                palindrome_list.append(product)
    max_palindrome = max(palindrome_list)
    print(max_palindrome)      

main()      