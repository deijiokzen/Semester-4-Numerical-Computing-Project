from main import func

def enter_data():
    integrate = input("Integrate function: ")

    bound1 = float(input("From a = "))
    bound2 = float(input("To b = "))

    while(1):
        num = int(input("Enter n = "))
        if num < 2:
            print("\nError! At least n=2 necessary for Simpson's Method. Try again.\n")
            continue
        break
    spacing = (bound2-bound1)/num

    points = list()
    for i in range(num+1):
        points.append(bound1 + (i*spacing))

    # if num%2 == 0:
    #     result = simpson_one_third(integrate, num, spacing, points)
    # else:
    #     result = simpson_three_eights(integrate, num, spacing, points)

    while(1):
        choice = int(input("\nSelect:\n1. Simpson's 1/3rd\n2. Simpson's 3/8th\n"))
        if choice == 1:
            result = simpson_one_third(integrate, num, spacing, points)
            break
        if choice == 2:
            result = simpson_three_eights(integrate, num, spacing, points)
            break
        else:
            print("Invalid input! Try again.")

    print("\nIntegration of " + integrate + " from " + str(points[0]) + " to " + str(points[num]) + " = " + str(result))


def simpson_one_third(function, n, h, points):

    answer = func(function, points[0]) + func(function, points[n])

    for i in range(1, n, 2):
        answer += 4*func(function, points[i])

    for i in range(2, n-1, 2):
        answer += 2*func(function, points[i])

    answer *= h/3

    return answer

def simpson_three_eights(function, n, h, points):

    answer = func(function, points[0]) + func(function, points[n])

    for i in range(1, n):
        if i%3==0:
            continue
        answer += 3*func(function, points[i])

    for i in range(3, n, 3):
        answer += 2*func(function, points[i])

    answer *= (3*h)/8

    return answer

if __name__== "__main__":
    print("SIMPSON'S RULE FOR INTEGRATION:\n")
    enter_data()