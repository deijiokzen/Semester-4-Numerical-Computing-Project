from sympy.parsing.sympy_parser import standard_transformations,\
    implicit_multiplication_application
from sympy import *
from mpmath import *

prog_quit = 0
prog_exit = 0

function = input('Enter the function : ')
L = float(input("Enter the first interval a : "))
R = float(input("Enter the second interval b : "))
Tolerance = float(sympify(input("Input tolerance value:").translate({ord(c): "**" for c in "^"})).evalf()) #Saud reminder : understood the working, dk the logic behind translate

transformations = (standard_transformations +
                   (implicit_multiplication_application,))

function = parse_expr(function, transformations=transformations)
x, e = symbols('x e')

function = function.subs(e, exp(1)) #e scenez
func_a = float(function.subs(x, L))
func_b = float(function.subs(x, R))

if (func_a > 0 and func_b < 0):     #it will understand which value to change if the resulted value is positive or negative
    value_replacer = 1
elif (func_a < 0 and func_b > 0):
    value_replacer = 2
else:
    print("Solution does not exist")
    prog_exit = 1

iteration = 0
c = float(0)
c_prev = float(0)
while (prog_quit == 0) and (prog_exit == 0):    #if the solution exists and solution not found, RUN BARRY RUN
    iteration += 1

    if(iteration > 1):      #store the previous value for checking the stopping criteria shit
        c_prev = c

    c = (L+R)/2
    func_C = float(function.subs(x, c))
    if (func_C > 0) and (value_replacer == 1):      #code to where to put the values after each iterations
        L = c
    elif (func_C > 0) and (value_replacer == 2):
        R = c
    elif (func_C < 0) and (value_replacer == 1):
        R = c
    elif (func_C < 0) and (value_replacer == 2):
        L = c

    if func_C == 0:         #All four stopping criteria
        solution = c
        prog_quit = 1
        break
    elif abs(func_C) < Tolerance:
        solution = c
        prog_quit = 1
        break
    elif abs(c - c_prev) < Tolerance:
        prog_quit = 1
        solution = c
        break
    elif abs((c-c_prev)/c) < Tolerance:
        solution = c
        prog_quit = 1
        break

if prog_quit == 1:
    print("The answer is : ", solution)
    print("At iteration : ", iteration)