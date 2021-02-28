from sympy import S, Symbol
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations + (implicit_multiplication_application,))
print(type(parse_expr("2x", transformations=transformations)))
y = parse_expr("2x", transformations=transformations)
load the string as an expression

expression = S('cos(x) + tan (x)')

symbol_vals = {}
all_symbols = [str(x) for x in expression.atoms(Symbol)]
for i, item in enumerate(all_symbols):
   key = all_symbols[i]
   value = float(input("Enter value for " + all_symbols[i] + ":"))
   symbol_vals[key]=value
result = expression.subs(symbol_vals)
print(result)
##################################################################

from sympy.parsing.sympy_parser import (parse_expr, _token_splittable, standard_transformations, implicit_multiplication, split_symbols_custom)
def can_split(symbol):
    if symbol not in ('list', 'of', 'unsplittable', 'names'):
                return _token_splittable(symbol)
        return False
    transformation = split_symbols_custom(can_split)
    parse_expr('unsplittable', transformations=standard_transformations + (transformation, implicit_multiplication))
#############################################################################################
    # sympy.S is a shortcut to sympify
    from sympy import S, Symbol
    from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)
    expression = parse_expr(input("Your custom expression here:"),
                            transformations=(standard_transformations + (implicit_multiplication_application,)))

    # load the string as an expression
    # expression = S('cos(x) + tan(x)')

    # get the symbols from the expression and convert to a list
    # all_symbols = ['avar', 'anothervar', 'athirdvar']
    symbol_vals = {}
    all_symbols = [str(x) for x in expression.atoms(Symbol)]
    for i, item in enumerate(all_symbols):
        key = all_symbols[i]
        value = float(input("Enter value for " + all_symbols[i] + ":"))
        symbol_vals[key] = value
    result = expression.subs(symbol_vals)
    print(result)

    # result = expression.subs(all_symbols)
    # print(result)

######################################################################################################################
from mpmath import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

x = symbols("x")

_fOfX = "e**x + x + 1"

if __name__== "__main__":
    #Function to sympy expression
    _sympyFunction = sympify(_fOfX)
    #Calcolo la derivata prima
    _dPrima = diff(_sympyFunction,x,1)
    _dPrima = _dPrima.subs(x,5)
    #Replace e with exp(1)
    e = symbols('e')
    _dPrima = _dPrima.subs(e, exp(1))

    print(_dPrima.evalf())
    #####################################################################################################
    # sympy.S is a shortcut to sympify
    from sympy.abc import *
    from sympy import S, Symbol
    import sympy as sy
    from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)

    expression = parse_expr(input("Your custom expression here:"),
                            transformations=(standard_transformations + (implicit_multiplication_application,)))

    # load the string as an expression
    # expression = S(input("Your custom expression here:"))

    # get the symbols from the expression and convert to a list
    # all_symbols = ['avar', 'anothervar', 'athirdvar']
    symbol_vals = {}
    all_symbols = [str(x) for x in expression.atoms(Symbol)]
    for i, item in enumerate(all_symbols):
        key = all_symbols[i]
        value = float(input("Enter value for " + all_symbols[i] + ":"))
        symbol_vals[key] = value

    result = expression.subs(symbol_vals)
    print(result)
    print(sy.pi)

    # result = expression.subs(all_symbols)
    # print(result)


