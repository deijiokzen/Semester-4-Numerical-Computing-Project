from main import *
import os


def lagrange():
    n = int(input("Enter number of points (min = 2): "))
    if n < 2:
        print("Points can not be less than, number of points set to 2")
        n = 2
    
    choice = str(input("Do you want to specify the degree of Lagrange Interpolation [y/n] : "))
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
                check+=1
    else:
        start = 0
        end = start+degree

    Expression = input("Enter the Function to perform the lagrange Interpolation :")

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


lagrange()
