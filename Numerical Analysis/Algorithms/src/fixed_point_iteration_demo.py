import math

def fixed_point_1():
    eps : float = 0.001
    #initial guess
    x=0

    for i in range(20):
        x=math.sqrt(x+1)

        print(f"{i}). {x}")

def fixed_point_2():
    eps : float = 0.001
    #initial guess
    x=1

    for i in range(20):
        x=1+1/x

        print(f"{i}). {x}")

def fixed_point_3():
    eps : float = 0.001
    #initial guess
    x=0

    for i in range(20):
        x=(x**3 -2*x**2 +2)/4

        print(f"{i}). {x}")


def example_1():

    #initial guess
    x=1

    for i in range(20):
        x=1/2 * math.sqrt((10-x*x*x))

        print(f"{i}). {x}")

def main():

    
    #fixed_point_1()
    #fixed_point_2()
    fixed_point_3()
    #example_1()

    


if __name__=="__main__":
    main()