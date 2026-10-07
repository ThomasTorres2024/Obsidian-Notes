"""
Basic implementation for newton's method 
10/6/26
"""

import math

def ex_1():

    #initial guess 
    x_0 = math.pi/4


    #compute deriv approx 
    x_0,x_1=0,1
    
    #y=mx+b

    m=  (math.cos(x_1) - x_1 -math.cos(x_0) + x_0)/(x_1 - x_0)
    b= math.cos(x_0) -x_0

    #0 = mx+b -> -b = mx -> -b/m = x 
    x_0=x_1
    x_1=-b/m



    #just fixed point from here 
    print(f"0: {x_1}")
    
    for i in range(100):
        x_initial =  x_1 - ((math.cos(x_1)-x_1)*(x_1 - x_0)) / ( math.cos(x_1) -x_1 -math.cos(x_0) + x_0  )
        x_0=x_1
        x_1=x_initial
        if((i+1)%10==0 ):
            print(f"{i+1}: {x_1}")
    
    print("-"*50)
    print(f"Final: {x_1}")

def main():
    ex_1() 

if __name__ == "__main__":
    main()