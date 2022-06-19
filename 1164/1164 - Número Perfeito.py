for i in range(int(input())):
    x,s = int(input()),0
    for i in range(1,x):
        if x%i == 0: s+=i
    if s == x: print(x,'eh perfeito')
    else: print(x,'nao eh perfeito')
