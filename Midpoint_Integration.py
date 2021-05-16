from Functions import *

def Midpoint(*param):
    list(param)
    if(len(param)==4):
        expression=param[0]
        a=param[1]
        b=param[2]
        h=(param[2]-param[1])/(param[3]+2)
        print("Value of h is=",h)
        n=param[3]+2
    else:
        print("More variables passed in Midpoint Integral Function than allowed!")
        return
    sum=0
    for j in range(0, int(n/2),1):
        print("Value of f(x"+str(2*j)+")=", func(expression, a+(2*(j)+1)*h))
        sum+=func(expression, a+(2*(j)+1)*h)
    final_calc=2*h*sum
    print("Your MidPoint Integral Result Is: ", final_calc)

    return
def MidpointValues():
    Exp=input("Enter The Expression you want To Evaluate with Midpoint Integration:")
    L_x = float(sympify(input("Enter value for lower Limit:").translate({ord(c): "**" for c in "^"})).evalf())
    L_y = float(sympify(input("Enter value for Upper Limit:").translate({ord(c): "**" for c in "^"})).evalf())
    n=-1
    while(n<0):
        n=int(sympify(input("Enter value for n(should be greater than 0):").translate({ord(c): "**" for c in "^"})).evalf())

    Midpoint(Exp,L_x,L_y,n)


MidpointValues()



