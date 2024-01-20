
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import matplotlib.pyplot as plt
import math

def sumSquared(n):
    k=0
    
    while n>0:
        k += (n % 10)*(n % 10)
        n = int(n/10)

    return(k)


def happyNumber(n):
    setN  = set()
    
    while n>1 and n not in setN:
        setN.add(n)
        n = sumSquared(n)
    
    #print(setN)
    
    return n==1, len(setN)
    


def procuraHappy(N):
    lstHappy =[]
    lstLength =[]
    lstLenHappy=[]
    for i in range(1,N):
        isHappy, lenN = happyNumber(i)
        
        lstLength.append(lenN)
        
        if isHappy:
            lstHappy.append(i)
            lstLenHappy.append(lenN)
        
    #print(lstLength)
    print(lstHappy)    
    
    #Plota tamanhos do ciclo apenas do happy
    plt.figure(figsize=(15,10))
    plt.scatter(lstHappy, lstLenHappy,color='goldenrod',marker='.')
    plt.title("Tamanhos do ciclo - apenas Números Felizes")
    plt.savefig("ApenasHappyCartesian.png")
    
    #Plota tamanhos do ciclo totais
    plt.figure(figsize=(15,10))
    x = range(1,N)    
    plt.scatter(x, lstLength,color='darkgreen',marker='.')
    plt.title("Tamanhos do ciclo - Todos os números")
    plt.savefig("TodosCartesian.png")
    
    #Transformando o eixo x numa escala polar
    #a cada ciclo de 100, dá uma volta completa
    xr =[]
    lstHappyPolar =[]
    for k in x:
        xr.append(2*math.pi*k/100)

    for k in lstHappy:
        lstHappyPolar.append(2*math.pi*k/100)
    

    #Plota tamanhos do ciclo apenas do happy
    plt.figure(figsize=(15,10))
    plt.polar(lstHappyPolar, lstLenHappy,color='goldenrod',marker='.',linestyle='none')
    plt.title("Tamanhos do ciclo - apenas Números Felizes")
    plt.savefig("apenasHappyPolar.png")
    
    #Plota tamanhos do ciclo todos
    plt.figure(figsize=(15,10))
    plt.polar(xr, lstLength,color='darkgreen',marker='.',linestyle='none')
    plt.title("Tamanhos do ciclo - Todos os números")
    plt.savefig("TodosPolar.png")
    
if __name__ == '__main__':
    procuraHappy(10000)
    
      