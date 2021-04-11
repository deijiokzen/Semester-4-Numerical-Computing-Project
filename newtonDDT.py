import os
from tabulate import tabulate
from colorama import *

def pos(x, y):
    return ("\033[%d;%dH" % (y, x)) 

def factorial(num):
    if num == 1:
        return 1

    return num*factorial(num-1)

def printDiffTable(points, dds, n):
    os.system("cls")
    print("x\t\tf(x)", end = '')

    for i in range(1, n):
        print('\t\t' + str(i) + "DD", end = '')

    print()
    for i in range(0, n):
        print('\n' + str(points[i]) + '\t\t' + str(dds[0][i]), end = '\t\t')

        for j in range(1, n):
            try:
                print(str(dds[j][i]), end = '\t\t')
            except IndexError:
                print(end = '\t\t')
    
    print()

def Diff():
    while True:
        choice = int(input("\n1. Forward Difference\n2. Backward Difference\n3. Central Difference\n"))
        if choice == 1 or choice == 2:
            divSimpChoice = int(input("\n1. Divided Difference\n2. Simple Difference\n"))

            if divSimpChoice != 1 and divSimpChoice != 2:
                print("Invalid Input, try again!")
                continue

        if choice != 1 and choice != 2 and choice != 3:
            print("Invalid Input, try again!")
            continue

        break

    while True:
        n = int(input("Enter number of points (min = 2): "))
        if choice == 3 and n%2 == 0:
            print("Error, central difference needs odd number of points. Try again!")
        else:
            break

    if n < 2:
        print("Points can not be less than 2, number of points set to 2 (minimum).")
        n = 2

    fix = int(input("\nEnter fix: "))

    points = []
    functionVals = []

    points.append(float(input("Enter x0: ")))
    h = float(input("Enter spacing (rest of the points will be automatically entered using this spacing):\nh = "))

    for i in range(0, n-1):
        points.append(points[i]+h)

    for i in range(0, n):
        functionVals.append(float(input("Enter f(x" + str(i) + "): ")))

    x = round(float(input("\nEnter the value for which you want the approximation: x = ")), fix)

    if choice == 1:
        answer = forward(n, h, x, fix, points, functionVals, divSimpChoice)
    elif choice == 2:
        answer = backward(n, h, x, fix, points, functionVals, divSimpChoice)
    elif choice == 3:
        answer = central(n, h, x, fix, points, functionVals)

    print("\nf(" + str(x) + ") = " + str(round(answer, fix)))

def central(n, h, x, fix, points, functionVals):

    return 1

def forward(n, h, x, fix, points, functionVals, divSimpChoice):
    s = (x - points[0])/h

    aVals = [functionVals[0]]
    dds = []
    ddn = []
    numDD = 0

    dds.append(functionVals)

    for m in range(0, n-1):

        for i in range(0, len(dds[m])-1):
            try:
                temp = dds[m][i+1]-dds[m][i]
                if divSimpChoice == 1:
                    temp /= (points[i+1+numDD]-points[i])

                ddn.append(round(temp, fix))
            except ZeroDivisionError:
                print("\nError! Two points cannot be equal to each other.")
                exit(-1)
        
        dds.append(ddn)
        aVals.append(ddn[0])
        ddn = []
        numDD += 1

    print("\nValues for nDD " + str(dds))
    print("a values: " + str(aVals) + "\n")

    printDiffTable(points, dds, n)

    answer = aVals[0]
    for i in range(1, n):
        mult = 1

        for j in range(0, i):
            mult *= (s-j)
            if divSimpChoice == 1:
                mult *= h

        if divSimpChoice == 2:
            mult /= factorial(i)

        answer += round(aVals[i]*mult, fix)

    return answer

def backward(n, h, x, fix, points, functionVals, divSimpChoice):
    s = (x - points[n-1])/h

    aVals = [functionVals[n-1]]
    dds = []
    ddn = []
    numDD = 0

    dds.append(functionVals)

    for m in range(0, n-1):

        for i in range(0, len(dds[m])-1):
            try:
                temp = (dds[m][i+1]-dds[m][i])
                if divSimpChoice == 1:
                    temp /= (points[i+1+numDD]-points[i])

                ddn.append(round(temp, fix))
            except ZeroDivisionError:
                print("\nError! Two points cannot be equal to each other.")
                exit(-1)
        
        dds.append(ddn)
        aVals.append(ddn[len(ddn)-1])
        ddn = []
        numDD += 1

    print("\nValues for nDD " + str(dds))
    print("a values: " + str(aVals) + "\n")

    printDiffTable(points, dds, n)

    answer = aVals[0]
    for i in range(1, n):
        mult = 1

        for j in range(0, i):
            mult *= (s+j)
            if divSimpChoice == 1:
                mult *= h

        if divSimpChoice == 2:
            mult /= factorial(i)

        answer += round(aVals[i]*mult, fix)

    return answer

def ddt():
    n = int(input("Enter number of points (min = 2): "))
    if n < 2:
        print("Points can not be less than 2, number of points set to 2 (minimum).")
        n = 2

    fix = int(input("\nEnter fix: "))

    points = []
    functionVals = []

    for i in range(0, n):
            points.append(float(input("Enter x" + str(i) + ": ")))
            functionVals.append(round(float(input("Exter f(x" + str(i) + "): ")), fix))

    x = round(float(input("\nEnter the value for which you want the approximation: x = ")), fix)

    aVals = [functionVals[0]]
    dds = []
    ddn = []
    numDD = 0

    dds.append(functionVals)

    for m in range(0, n-1):

        for i in range(0, len(dds[m])-1):
            try:
                ddn.append(round((dds[m][i]-dds[m][i+1])/(points[i]-points[i+1+numDD]), fix))
            except ZeroDivisionError:
                print("\nError! Two points cannot be equal to each other.")
                exit(-1)
        
        dds.append(ddn)
        aVals.append(ddn[0])
        ddn = []
        numDD += 1

    print("\nValues for nDD " + str(dds))
    print("a values: " + str(aVals) + "\n")

    printDiffTable(points, dds, n)


    answer = aVals[0]
    for i in range(1, n):
        mult = 1

        for j in range(0, i):
            mult *= (x-points[j])
        
        answer += round(aVals[i]*mult, fix)

    print("\nf(" + str(x) + ") = " + str(round(answer,fix)))

os.system("cls")
Diff()