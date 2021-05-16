from main import *
import os


def Trap():
    Expression = input(
        "Enter the Function to Integrate using Trapezoid method : ")
    bound1 = float(sympify(input("From a = ").translate({ord(c): "**" for c in "^"})).evalf())
    bound2 = float(sympify(input("To b = ").translate({ord(c): "**" for c in "^"})).evalf())
    fix = int(input("Enter the rounding point digits : "))

    while(1):
        num = int(input("Enter n = "))
        if num < 1:
            print("\nError! At least n=1 necessary for Trapezoid's Method. Try again.\n")
            continue
        break
    spacing = (bound2-bound1)/num
    answer = float(0)

    for i in range(1, num):
        answer += round(func(Expression, (bound1 + (i*spacing))), fix)
    else:
        answer *= 2
        answer = round(answer, fix)

    answer += round(func(Expression, bound1) + func(Expression, bound2), fix)
    answer *= (spacing/2)
    answer = round(answer, fix)
    print("The integrated value of the function {} is estimated to be : {}".format(Expression, answer))


if __name__ == "__main__":
    Trap()
