from Functions import *

def enterdata():
    Expression = input(
        "Enter the Function to Integrate using Modified Euler Method : ")
    h = float(input("Enter h : "))
    n = bound1 = float(input("From a = "))
    bound2 = float(input("To b = "))
    y0 = float(input("Enter y("+str(bound1)+") : "))
    fix = int(input("Enter the rounding point digits : "))

    choice = int(input("Which methods do you want to use for Integrating : \n1. Euler.\n2. Modified Euler.\n3. Huen Method.\n4. RK4 Method\n Choice : "))
    if choice == 1:
        Euler(Expression, h, n, bound1, bound2, y0, fix)
    elif choice == 2:
        ModifiedEuler(Expression, h, n, bound1, bound2, y0, fix)
    elif choice == 3:
        Huen(Expression, h, n, bound1, bound2, y0, fix)
    elif choice == 4:
        Rk4(Expression, h, n, bound1, bound2, y0, fix)
    else:
        print("no choice allocated to this number.")

def ModifiedEuler(Expression, h, n, bound1, bound2, y0, fix):
    # Expression = input(
    #     "Enter the Function to Integrate using Modified Euler Method : ")
    # h = float(input("Enter h : "))
    # n = bound1 = float(input("From a = "))
    # bound2 = float(input("To b = "))
    # y0 = float(input("Enter y("+str(bound1)+") : "))
    # fix = int(input("Enter the rounding point digits : "))

    matrix = []
    while (n <= bound2):
        list = [n, y0]
        n += h
        matrix.append(list)

    n = bound1+h
    i = int(0)
    while (n <= bound2):
        k1 = round((h * func2(Expression, matrix[i][0], matrix[i][1])), fix)
        k2 = round(
            (h * func2(Expression, matrix[i+1][0], (k1 + (matrix[i][1])))), fix)

        matrix[i+1][1] = round((matrix[i][1] + 0.5*(k1 + k2)), fix)

        i += 1
        n += h

    header = ["x", "y"]
    row_format = "{:>15}" * (len(header) + 1)
    print(row_format.format("", *header))
    for row in matrix:
        print(row_format.format("", *row))


def Huen(Expression, h, n, bound1, bound2, y0, fix):
    # Expression = input(
    #     "Enter the Function to Integrate using Huen Method : ")
    # h = float(input("Enter h : "))
    # n = bound1 = float(input("From a = "))
    # bound2 = float(input("To b = "))
    # y0 = float(input("Enter y("+str(bound1)+") : "))
    # fix = int(input("Enter the rounding point digits : "))

    matrix = []
    while (n <= bound2):
        list = [n, y0]
        n += h
        matrix.append(list)

    n = bound1+h
    i = int(0)
    while (n <= bound2):
        k1 = round((func2(Expression, matrix[i][0], matrix[i][1])), fix)
        k2 = round(
            (func2(Expression, ((h/3)+matrix[i][0]), (((k1*h)/3) + (matrix[i][1])))), fix)
        k3 = round(func2(
            Expression, (((2*h)/3)+matrix[i][0]), (((2*k2*h)/3) + (matrix[i][1]))), fix)

        matrix[i+1][1] = round((matrix[i][1] + (1/4)*(k1 + (3*k3))*h), fix)

        i += 1
        n += h

    header = ["x", "y"]
    row_format = "{:>15}" * (len(header) + 1)
    print(row_format.format("", *header))
    for row in matrix:
        print(row_format.format("", *row))


def Euler(Expression, h, n, bound1, bound2, y0, fix):
    # Expression = input("Enter the Function to Integrate using Huen Method : ")
    # h = float(input("Enter h : "))
    # n = bound1 = float(input("From a = "))
    # bound2 = float(input("To b = "))
    # y0 = float(input("Enter y("+str(bound1)+") : "))
    # fix = int(input("Enter the rounding point digits : "))

    matrix = []
    while (n <= bound2):
        list = [n, y0]
        n += h
        matrix.append(list)

    n = bound1+h
    i = int(0)
    while (n <= bound2):
        k1 = func2(Expression, matrix[i][0], matrix[i][1])
        
        matrix[i+1][1] = round((matrix[i][1] + (h*k1)), fix)

        i += 1
        n += h

    header = ["x", "y"]
    row_format = "{:>15}" * (len(header) + 1)
    print(row_format.format("", *header))
    for row in matrix:
        print(row_format.format("", *row))        


def Rk4(Expression, h, n, bound1, bound2, y0, fix):
    # Expression = input(
    #     "Enter the Function to Integrate using Huen Method : ")
    # h = float(input("Enter h : "))
    # n = bound1 = float(input("From a = "))
    # bound2 = float(input("To b = "))
    # y0 = float(input("Enter y("+str(bound1)+") : "))
    # fix = int(input("Enter the rounding point digits : "))

    matrix = []
    while (n <= bound2):
        list = [n, y0]
        n += h
        matrix.append(list)

    n = bound1+h
    i = int(0)
    while (n <= bound2):
        k1 = round((h * func2(Expression, matrix[i][0], matrix[i][1])), fix)
        k2 = round((h * func2(Expression, ((h/2)+matrix[i][0]), ((k1/2) + (matrix[i][1])))), fix)
        k3 = round((h * func2(Expression, ((h/2)+matrix[i][0]), ((k2/2) + (matrix[i][1])))), fix)
        k4 = round((h * func2(Expression, matrix[i+1][0], (k3 + (matrix[i][1])))), fix)


        matrix[i+1][1] = round((matrix[i][1] + (1/6)*(k1 + 2*(k2+k3) + k4)), fix)

        i += 1
        n += h

    header = ["x", "y"]
    row_format = "{:>15}" * (len(header) + 1)
    print(row_format.format("", *header))
    for row in matrix:
        print(row_format.format("", *row))


# ModifiedEuler()
# Huen()
# Euler()
enterdata()