from main import *
from newtonDDT import *
from simpson import *
from Trapezoid import *
from MidEndPoint import *
from chap5methods import *
def ProjectMenu():
    def project_print_menu():
        os.system("cls")
        print(30 * "-", "Chapter Selection", 30 * "-")
        print("1. Chapter#2-Solutions of Equations in One Variable")
        print("2. Chapter#3-Interpolation and Polynomial Approximation")
        print("3. Chapter#4-Numerical Differentiation and Integration")
        print("4. Chapter#5-Initial-Value Problems for Ordinary Differential Equations")
        print("5. Exit")


    while True:
        project_print_menu()
        choice = int(input("Enter your choice [1-5]:"))
        if choice==1 :
            menu_chapter2()
        elif choice==2:
            while True:
                print(30 * "-", "Chapter#3-Interpolation and Polynomial Approximation", 30 * "-")
                choice_2=int(input("1. Lagrange\n2. Divided Differences\n3. Previous Menu"))
                if choice_2==1:
                    lagrange()
                elif choice_2==2:
                    Diff()
                elif choice_2==3:
                    break
                else:
                    continue
        elif choice==3:
            while True:
                print(30 * "-", "Chapter#4-Numerical Differentiation and Integration", 30 * "-")
                print()
                choice_2=int(input("Numerical Differentiation:\n1. Three-Point / Five-Point Method\nNumerical Integration:\n2. Trapezoid\n3. Simpsons\n4. Previous Menu"))
                if choice_2==1:
                    enter_points()
                elif choice_2==2:
                    Trap()
                elif choice_2==3:
                    enter_data()
                elif choice_2==4:
                    break
                else:
                    continue
        elif choice==4:
            enterdata_()
        elif choice==5:
            break
        else:
            print("Please select correct option!")
            continue




ProjectMenu()