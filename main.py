from mpmath import *
from sympy import *
import sympy, numpy as np, math
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)

def func(expression, limit_val):
    expression = expression.translate({ord(c): "**" for c in "^"})
    Function = parse_expr(expression,  local_dict={"log": lambda x: sympy.log(x, 10)}, transformations=(standard_transformations + (implicit_multiplication_application,)))
    e = symbols('e')
    Function = Function.subs(e, exp(1))
    symbol_vals = {}
    all_symbols = [str(x) for x in Function.atoms(Symbol)]
    if (len(all_symbols) != 1):
        print("Error, more than one variable detected!")
        exit(0)
    for i, item in enumerate(all_symbols):
        key = all_symbols[i]
        value = limit_val
        symbol_vals[key] = value
    Function = Function.subs(symbol_vals)
    return Function.evalf()

def func_differential(expression, limit_val):
    expression = expression.translate({ord(c): "**" for c in "^"})
    Function = parse_expr(expression, local_dict={"log": lambda x: sympy.log(x, 10)},
                          transformations=(standard_transformations + (implicit_multiplication_application,)))
    e = symbols('e')
    x = symbols('x')
    Function = Function.subs(e, exp(1))
    symbol_vals = {}
    all_symbols = [str(x) for x in Function.atoms(Symbol)]
    if (len(all_symbols) != 1):
        print("Error, more than one variable detected!")
        exit(0)
    key = all_symbols[0]
    symbol_vals[key] = x
    Function = Function.subs(symbol_vals)
    Function=diff(Function,x)

    key = x
    value = limit_val
    symbol_vals[key] = value
    Function = Function.subs(symbol_vals)
    return Function.evalf()

def newton(Expression, L_x, L_y, Eps_, Round_Val):
    Eps=10**Eps_
    if Round_Val > 12:
        Round_Val = 12
    IVR = abs(func(Expression, L_x) * func(Expression, L_y))
    a = 0
    header = ["N","P", "F(P)", "|ERROR < 10^"+str(Eps_)+"|"]
    matrix = []
    P0 = (L_x + L_y) / 2
    i=-1
    while (1):
        i+=1
        # print(c,"-",a)
        matrix.append([i,round(P0,Round_Val), round(func(Expression, P0),Round_Val), round(abs(P0 - a),Round_Val)])
        # print([P0, func(Expression, P0), abs(P0 - a)])

        if abs(P0 - a) < Eps or IVR == 0 or i==200:
            break

        a = P0
        P0 = P0-func(Expression,P0)/func_differential(Expression,P0)


    row_format = "{:>25}" * (len(header) + 1)
    print(row_format.format("", *header))
    for row in matrix:
        print(row_format.format("", *row))
    print("Your final value of P is: ", P0, ", While your rounded off value is: ", round(P0,Round_Val))



def bisection(Expression, L_x, L_y, Eps_, Round_Val):
    Eps=10**Eps_
    if Round_Val > 12:
        Round_Val = 12
    IVR = abs(func(Expression, L_x) * func(Expression, L_y))
    a = 0
    header=["N","A", "B", "C=(A-B)/2", "F(C)", "|ERROR < 10^"+str(Eps_)+"|"]
    matrix=[]
    i=-1
    while(1):
        i+=1

        c = (L_x + L_y) / 2
        # print(c,"-",a)
        list =[i,round(L_x,Round_Val), round(L_y,Round_Val), round(c,Round_Val), round(func(Expression,c),Round_Val), round(abs(c-a),Round_Val)]
        matrix.extend([list])
        # print([round(L_x,Round_Val), round(L_y,Round_Val), round(c,Round_Val), round(func_bisector(Expression,c),Round_Val), round(abs(c-a),Round_Val)])
        if abs(c-a) < Eps or IVR == 0 or i==85:
            if abs(c - a) < Eps:
                print("The error value has reached!\n")
            else:
                print("IVR has reached!\n")
            break
        elif func(Expression,c) < 0:
            if(func(Expression,L_x) < 0):
                L_x=c
            else:
                L_y=c

        elif func(Expression,c) > 0:
            if (func(Expression, L_x) > 0):
                L_x = c
            else:
                L_y = c
        a = c

    row_format ="{:>25}" * (len(header) + 1)
    print(row_format.format("", *header))
    for row in matrix:
        print(row_format.format("", *row))
    print("Your final value of c is: ", c, ", While your rounded off value is: ", round(c,Round_Val))

def regular_falsi(Expression, L_x, L_y, Eps_,Round_Val):
    Eps=10**Eps_
    if Round_Val > 12:
        Round_Val = 12
    IVR = abs(func(Expression, L_x) * func(Expression, L_y))
    a = 0
    header = ["N","A", "B", "C=[A(F(B)-B(F(A))]/", "F(C)", "|ERROR < 10^"+str(Eps_)+"|"]
    headerv2 = [" "," "," ","[F(B)-F(A)]","",""]
    matrix = []
    i=-1
    while (1):
        i+=1
        c = (L_x * func(Expression,L_y) - L_y * func(Expression,(L_x))) / (func(Expression,L_y)-func(Expression,L_x))
        # print(c,"-",a)
        list=[round(i,Round_Val),round(L_x,Round_Val), round(L_y,Round_Val), round(c,Round_Val), round(func(Expression, c),Round_Val), round(abs(c - a),Round_Val)]
        matrix.extend([list])


        if abs(c - a) < Eps or IVR == 0:
            break
        elif func(Expression, c) < 0:
            if (func(Expression, L_x) < 0):
                L_x = c
            else:
                L_y = c

        elif func(Expression, c) > 0:
            if (func(Expression, L_x) > 0):
                L_x = c
            else:
                L_y = c
        a = c

    row_format = "{:>25}" * (len(header) + 1)
    print(row_format.format("", *header))
    print(row_format.format("", *headerv2))
    for row in matrix:
        print(row_format.format("", *row))
    print("Your final value of c is: ", c)

def secant(Expression, L_x, L_y, Eps_, Round_Val):
    Eps=10**Eps_
    i=1
    header=["N", "P(N-1)", "P(N-2)", "P(N)", "|ERROR < 10^"+str(Eps_)+"|"]
    matrix=[]
    while (1):
        i+=1

        c = L_y - ((func(Expression, L_y)*(L_y-L_x))/(func(Expression, L_y)-func(Expression, L_x)))
        list=[round(i,Round_Val),round(L_x,Round_Val), round(L_y,Round_Val), round(c,Round_Val), round(abs(c - L_y),Round_Val)]
        matrix.extend([list])
        if abs(c - L_y) < Eps or i==200:
            print("Error Tolerance Reached!")
            break
        L_x=L_y
        L_y=c

    row_format = "{:>25}" * (len(header) + 1)
    print(row_format.format("", *header))
    for row in matrix:
        print(row_format.format("", *row))
    print("Your final value of c is: ", c, ", While your rounded off value is: ", round(c, Round_Val))


def fixedpoint(expression, val):
    a=val
    while(1):
     a=func(expression, a)
     print("Error = ", a-func(expression, a))
     print(a)
     input()


# Expression = input("Enter the Function on Which Bisection will be Applied:")
# L_x = float(input("Enter value for Lower Limit:"))
# L_y = float(sympify(input("Enter value for Upper Limit:").translate({ord(c): "**" for c in "^"})).evalf())
# Eps = float(sympify(input("Input tolerance value:").translate({ord(c): "**" for c in "^"})).evalf())
#
bisection("x * cos(x) - 2x^2 +3x -1",1.2,1.3,-5,6)
regular_falsi("2x*cos(2x)-(x-2)^2",2,3,-5,6)
newton("ln(x-1)+cos(x-1)",1.3,2,-5,6)
secant("ln(x-1)+cos(x-1)", 1.3,2,-5,6)
# func_convergence("3/(x(x^(2)-3))", 1)
# func_convergence("(1/2)(x+3/x)", 1.5)

