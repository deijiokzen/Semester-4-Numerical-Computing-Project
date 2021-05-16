from Functions import func
from sympy import *

def Midpoint(*param):
    list(param)
    if(len(param)==4):
        expression=param[0]
        a=param[1]
        b=param[2]
        h=(param[2]-param[1])/(param[3]+2)
        n=param[3]+2
    else:
        print("More variables passed in Midpoint Integral Function than allowed!")
        return
    for j in range(0, n/2):
        sum+=func(expression, a+(j+1)*h)
    final_calc=2*h*sum
    print("Your MidPoint Integral Result Is: ", final_calc)

    return
def MidpointValues():
    Exp=input("Enter The Expression you want To Evaluate with Midpoint Integration:")
    L_x = int(sympify(input("Enter value for lower Limit:").translate({ord(c): "**" for c in "^"})).evalf())
    L_y = int(sympify(input("Enter value for Upper Limit:").translate({ord(c): "**" for c in "^"})).evalf())
    n=int(sympify(input("Enter value n:").translate({ord(c): "**" for c in "^"})).evalf())
    Midpoint(Exp,L_x,L_y,n)






