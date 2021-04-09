from main import *
import os


def lagrange():
    n = int(input("Enter number of points (min = 2): "))
    if n < 2:
        print("Points can not be less than, number of points set to 2")
        n = 2

    choice = str(
        input("Do you want to specify the degree of Lagrange Interpolation [y/n] : "))
    if choice == 'y':
        degree = int(input("Enter degree : "))
        if degree >= n and degree < 1:
            print("degree can not be greater than or equal to the number of points and less than 1, degree set to " + str(n-1))
            degree = n-1
    else:
        degree = n-1

    points = []

    for i in range(0, n):
        points.append(float(input("Enter x" + str(i) + " : ")))
    else:
        points.append(float(input("Enter x : ")))

    start = int(0)
    check = 0
    if choice == 'y':
        # for check in range(check, n-degree+1):
        while check+degree < n:
            if (points[check] < points[n] < points[check+degree]):
                start = check
                end = check+degree
                break
            else:
                check += 1
    else:
        start = 0
        end = start+degree

    Expression = input(
        "Enter the Function to perform the lagrange Interpolation :")

    os.system("cls")

    # make table format here
    print("x\t\tf(x)")
    for j in range(0, n):
        print("x" + str(j) + "\t\t" + str(points[j]))

    value = float(0)
    individual = float(1)

    for k in range(start, end+1):
        for i in range(start, end+1):
            if(i != k):
                individual *= (points[n] - points[i])/(points[k]-points[i])
        value += individual*func(Expression, points[k])
        individual = float(1)

    print("value of f({}) = {}".format(points[n], value))


def NewtonFixedPoint():
    p = float(input("Enter p0 (start value) : "))
    Expression = input(
        "Enter the Function to perform the Newton Fixed Point iteration method :")
    Eps = float(sympify(input("Input tolerance value:").translate({ord(c): "**" for c in "^"})).evalf())
    choice = input("Want to enable Maximum Iterations ? [y/n] ")
    RoundValue = int(input("Enter fixed point : "))
    p = round(p, RoundValue)
    
    if choice == 'y':
        total = int(input("Enter maximum number of iterations you want to perform : "))
    
    iteration, solution = int(0), int(0)
    divergence, i, flucTarget, fluctCount = float(0), float(0), float(0), float(0)
    quit_while, prog_quit, totalflag = int(0), int(0), int(0)
    header=["N", "P", "G(P)", "DIVERGENCE FROM LAST VALUE"]
    matrix = []

    while (quit_while != 1) and (prog_quit != 1) and (totalflag != 1) :
        g = func(Expression, p)
        g = round(g, RoundValue)
        
        if (iteration % 3 == 0) :   # pick every third value and will check the fluctuation with the remaining 2
            flucTarget = g
        elif flucTarget == g :        # One point increase for every fluctuation hit
            fluctCount += 1

        if (abs(g - p)) < Eps :
            solution = g
            quit_while = 1

        if(abs(g - p)) > divergence:
            divergence = round(abs(g - p), RoundValue)
            i += 1
        else:
            i = 0

        if(i == 5):
            print("The function is diverging at iteration {}.".format(iteration))
            prog_quit = 1
        if(fluctCount == 5):
            print("The value are fluctuating from the given function.")
            prog_quit = 1

        if choice == 'y':
            if (iteration+1) >= total:
                totalflag = 1
                prog_quit = 1

        iteration += 1
        list = [iteration, p, g, round(abs(g - p), RoundValue)]
        matrix.extend([list])
        p = g

    if prog_quit != 1 : 
        if (quit_while == 1) or (totalflag == 1) :
            os.system("cls")
            row_format = "{:>30}" * (len(header) + 1)
            print(row_format.format("", *header))
            for row in matrix:
                print(row_format.format("", *row))

            if solution != 0 :
                print("The final solution  : {} at Iteration {}".format(solution, iteration))




# lagrange()
NewtonFixedPoint()