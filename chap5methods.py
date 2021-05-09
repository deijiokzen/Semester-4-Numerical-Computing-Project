from main import *
from func2 import *
import os


def ModifiedEuler():
    Expression = input(
        "Enter the Function to Integrate using Trapezoid method : ")
    h = float(input("Enter h : "))
    n = bound1 = float(input("From a = "))
    bound2 = float(input("To b = "))
    y0 = float(input("Enter y("+str(bound1)+") : "))
    fix = int(input("Enter the rounding point digits : "))

    matrix = []
    while (n <= bound2):
        list = [n, y0]
        n += h
        matrix.append(list)
        # print(matrix[0][0])

    n = bound1+h
    i = int(0)
    while (n <= bound2):
        # a = matrix[i][0]
        # print (a)
        k1 = round((h * func2(Expression, matrix[i][0], matrix[i][1])), fix)
        k2 = round((h * func2(Expression, matrix[i+1][0], (k1 + (matrix[i][1])))), fix)

        matrix[i+1][1] = round((matrix[i][1] + 0.5*(k1 + k2)), fix)

        i += 1
        n += h

    header = ["x", "y"]
    row_format = "{:>15}" * (len(header) + 1)
    print(row_format.format("", *header))
    for row in matrix:
        print(row_format.format("", *row))


ModifiedEuler()