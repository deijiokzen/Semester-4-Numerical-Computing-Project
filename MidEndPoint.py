from decimal import *

def enter_points():

    while(1):
        num = int(input("\nEnter number of point (minimum 3): "))
        if num < 3:
            print("Error! Minimum number is 3. Try again.")
        else:
            break
    
    while(1):
        points = []
        for i in range(num):
            points.append(Decimal(input("Enter x" + str(i) + ": ")))

        diff = points[1] - points[0]
        diff_flag = False
        for i in range(2, num):
            if (points[i] - points[i-1]) != diff:
                print("These methods require equal spacing. Enter points again.")
                diff_flag = True
                break

        if not diff_flag:
            break

    functionVals = []
    for i in range(num):
        functionVals.append(Decimal(input("Enter f(x" + str(i) + "): ")))

    while(1):
        x = Decimal(input("\nEnter the point at which you want the derivative: x = "))

        correct_x_flag = False
        for i in range(num):
            if x == points[i]:
                correct_x_flag = True
                x = i
                break
        
        if not correct_x_flag:
            print("Invalid value. Try again.")
            continue
        break

    while(1):
        choice = int(input("\nChoose formula:\n1. Three-point Midpoint\n2. Three-point Endpoint\n3. Five-point Midpoint\n4. Five-point Endpoint\n"))
        h = Decimal(input("\nEnter valid value of h = "))

        if h % diff == 0 and h != 0:
            h = int(h / diff)
        else:
            print("Invalid value of h. Try again.")
            continue

        try:
            if choice == 1 and h != 0:
                result = three_mid_point(points, functionVals, x, diff, h)
                break
            elif choice == 2 and h != 0:
                result = three_end_point(points, functionVals, x, diff, h)
                break
            elif choice == 3 and h != 0:
                result = five_mid_point(points, functionVals, x, diff, h)
                break
            elif choice == 4 and h != 0:
                result = five_end_point(points, functionVals, x, diff, h)
                break
            else:
                print("Invalid input(s)! Try again.")

        except IndexError:
            print("The value of x is out of bounds for the selected method. Select a different method and/or value of h.")

    print("\nf'(" + str(x) + "): " + str(result))

def three_mid_point(points, f, x, h, h_multiple):
        return (1/(2*h*h_multiple))*(f[x+h_multiple] - f[x-h_multiple])

def three_end_point(points, f, x, h, h_multiple):
        return (1/(2*h*h_multiple))*(-3*f[x] + 4*f[x+h_multiple] - f[x+2*h_multiple])

def five_mid_point(points, f, x, h, h_multiple):
        return (1/(12*h*h_multiple))*(f[x-2*h_multiple] - 8*f[x-h_multiple] + 8*f[x+h_multiple] - f[x+2*h_multiple])

def five_end_point(points, f, x, h, h_multiple):
        return (1/(12*h*h_multiple))*(-25*f[x] + 48*f[x+h_multiple] - 36*f[x+2*h_multiple] + 16*f[x+3*h_multiple] - 3*f[x+h_multiple])


if __name__== "__main__":
    getcontext().prec = 9
    enter_points()