from mpmath import *
from sympy import *
import sympy, numpy as np, math
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)

def func_bisector(expression, limit_val):
    expression = expression.translate({ord(c): "**" for c in "^"})
    Function = parse_expr(expression, local_dict={"log": lambda x: sympy.log(x, 10)}, transformations=(standard_transformations + (implicit_multiplication_application,)))
    e = symbols('e')
    Function = Function.subs(e, exp(1))
    symbol_vals = {}
    all_symbols = [str(x) for x in Function.atoms(Symbol)]
    for i, item in enumerate(all_symbols):
        key = all_symbols[i]
        value = limit_val
        symbol_vals[key] = value
    Function = Function.subs(symbol_vals)
    return Function.evalf()

def func_newton(expression, limit_val):
    expression = expression.translate({ord(c): "**" for c in "^"})
    Function = parse_expr(expression, local_dict={"log": lambda x: sympy.log(x, 10),
                                                  "cos": lambda x: sympy.cos(sympy.deg(x)),
                                                  "sin": lambda x: sympy.sin(sympy.deg(x)),
                                                  "tan": lambda x: sympy.tan(sympy.deg(x))

                                                  },
                          transformations=(standard_transformations + (implicit_multiplication_application,)))
    e = symbols('e')
    x = symbols('x')
    Function = Function.subs(e, exp(1))
    symbol_vals = {}
    all_symbols = [str(x) for x in Function.atoms(Symbol)]
    key = all_symbols[0]
    symbol_vals[key] = x
    Function = Function.subs(symbol_vals)
    Function=diff(Function,x)

    key = x
    value = limit_val
    symbol_vals[key] = value
    Function = Function.subs(symbol_vals)
    return Function.evalf()

def newton(Expression, L_x, L_y, Eps):
    IVR = abs(func_bisector(Expression, L_x) * func_bisector(Expression, L_y))
    a = 0
    header = ["P", "F(P)", "ERROR"]
    matrix = []
    P0 = (L_x + L_y) / 2

    while (1):

        # print(c,"-",a)
        # matrix.append([P0, func_bisector(Expression, P0), abs(P0 - a)])
        print([P0, func_bisector(Expression, P0), abs(P0 - a)])

        if abs(P0 - a) < Eps or IVR == 0:
            break

        a = P0
        P0 = P0-func_bisector(Expression,P0)/func_newton(Expression,P0)


    row_format = "{:>20}" * (len(header) + 1)
    print(row_format.format("", *header))
    for team, row in zip(header, matrix):
        print(row_format.format("", *row))
    print("Your final value of P is: ", P0)



def bisection(Expression, L_x, L_y, Eps):
    IVR = abs(func_bisector(Expression, L_x) * func_bisector(Expression, L_y))
    a = 0
    header=["A", "B", "C=(A-B)/2", "F(C)", "ERROR"]
    matrix=[]
    while(1):

        c = (L_x + L_y) / 2
        # print(c,"-",a)
        # matrix.extend([[L_x, L_y, c, func_bisector(Expression,c), abs(c-a)]])
        print([L_x, L_y, c, func_bisector(Expression,c), abs(c-a)])
        if abs(c-a) < Eps or IVR == 0:
            if abs(c - a) < Eps:
                print("The error value has reached!\n")
            else:
                print("IVR has reached!\n")
            break
        elif func_bisector(Expression,c) < 0:
            if(func_bisector(Expression,L_x) < 0):
                L_x=c
            else:
                L_y=c

        elif func_bisector(Expression,c) > 0:
            if (func_bisector(Expression, L_x) > 0):
                L_x = c
            else:
                L_y = c
        a = c

    row_format ="{:>20}" * (len(header) + 1)
    print(row_format.format("", *header))
    for team, row in zip(header, matrix):
        print(row_format.format("", *row))
    print("Your final value of c is: ", c)

def regular_falsi(Expression, L_x, L_y, Eps):
    IVR = abs(func_bisector(Expression, L_x) * func_bisector(Expression, L_y))
    a = 0
    header = ["A", "B", "C=[A(F(B)-B(F(A))]/[F(B)-F(A)]", "F(C)", "ERROR"]
    matrix = []
    while (1):

        c = (L_x * func_bisector(Expression,L_y) - L_y * func_bisector(Expression,(L_x))) / (func_bisector(Expression,L_y)-func_bisector(Expression,L_x))
        # print(c,"-",a)
        matrix.append([L_x, L_y, c, func_bisector(Expression, c), abs(c - a)])

        if abs(c - a) < Eps or IVR == 0:
            break
        elif func_bisector(Expression, c) < 0:
            if (func_bisector(Expression, L_x) < 0):
                L_x = c
            else:
                L_y = c

        elif func_bisector(Expression, c) > 0:
            if (func_bisector(Expression, L_x) > 0):
                L_x = c
            else:
                L_y = c
        a = c

    row_format = "{:>40}" * (len(header) + 1)
    print(row_format.format("", *header))
    for team, row in zip(header, matrix):
        print(row_format.format("", *row))
    print("Your final value of c is: ", c)

def secant(Expression, L_x, L_y, Eps):
    while (1):
        c = L_y - ((func_bisector(Expression, L_y)*(L_y-L_x))/(func_bisector(Expression, L_y)-func_bisector(Expression, L_x)))
        print([L_x, L_y, c, abs(c - L_y)])
        if abs(c - L_y) < Eps:
            break
        L_x=L_y
        L_y=c




def func_convergence(expression, val):

    a=val
    while(1):
     a=func_bisector(expression, a)
     print("Error = ", a-func_bisector(expression, a))
     print(a)
     input()


# Expression = input("Enter the Function on Which Bisection will be Applied:")
# L_x = float(input("Enter value for Lower Limit:"))
# L_y = float(sympify(input("Enter value for Upper Limit:").translate({ord(c): "**" for c in "^"})).evalf())
# Eps = float(sympify(input("Input tolerance value:").translate({ord(c): "**" for c in "^"})).evalf())
#
# bisection(Expression,L_x,L_y,Eps)
# regular_falsi(Expression,L_x,L_y,Eps)
# newton("3x - e^(x)",1,2,10**-5)
secant("2x + 3cos x - e^x", 0,1,10**-5)
# func_convergence("3/(x(x^(2)-3))", 1)
# func_convergence("(1/2)(x+3/x)", 1.5)