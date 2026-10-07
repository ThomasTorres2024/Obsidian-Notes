"""
Basic implementation for newton's method 
10/6/26
"""

import math

def ex_1():

    #initial guess 
    x_0 = math.pi/4
    print(f"0: {x_0}")
    for i in range(100):
        x_0 =  x_0 - (math.cos(x_0) - x_0 )/( -math.sin(x_0) - 1 )

        if((i+1)%10==0 ):
            print(f"{i+1}: {x_0}")
    
    print("-"*50)
    print(f"Final: {x_0}")

def main():
    ex_1() 

if __name__ == "__main__":
    main()