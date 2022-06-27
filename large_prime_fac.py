# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 00:28:41 2022

@author: ompra
"""
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def lpf(x):
    factor_list = []
    for i in range(1,x):
        if(x%i==0):
            factor_list.append(i)
    return factor_list

def is_prime(num):
    flag= False
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                flag = True
                break
    return flag

def main():
    x=int(input("Enter the number : "))
    result_factor = lpf(x)
    output_list = []
    for k in result_factor:
        flag_result = is_prime(k)
        if flag_result == False:
            output_list.append(k)
    print(output_list)
    print(max(output_list))
        
main()
        
