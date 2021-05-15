from mpmath import *
from sympy import *

import sympy
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
def func2(*param):
    param=list(param)
    param[0]=param[0].translate({ord(c): "**" for c in "^"})
    Function = parse_expr( param[0],  local_dict={"log": lambda x: sympy.log(x, 10)}, transformations=(standard_transformations + (implicit_multiplication_application,)))
    e = symbols('e')
    Function = Function.subs(e, exp(1))
    symbol_vals = {}
    all_symbols = [str(x) for x in Function.atoms(Symbol)]
    if (len(all_symbols) != 2):
        print("Error, more than two variable detected!")
        exit(0)
    for i, item in enumerate(all_symbols):
        key = all_symbols[i]
        if(key=='x'):
            value =  param[1]
        else:
            value = param[2]
        symbol_vals[key] = value
    Function = Function.subs(symbol_vals)
    return Function.evalf()