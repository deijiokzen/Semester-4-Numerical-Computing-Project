from main import *
from newtonDDT import *


def ProjectMenu():
    def project_print_menu():
        os.system("cls")
        print(30 * "-", "Chapter Selection", 30 * "-")
        print("1. Chapter#2-Solutions of Equations in One Variable")
        print("2. Chapter#3-Interpolation and Polynomial Approximation")
        print("3. Chapter#4-Numerical Differentiation and Integration")
        print("4. Chapter#5-Initial-Value Problems for Ordinary Differential Equations")
        print("5. Exit")


    choice = int(input("Enter your choice 1-5"))
    while True:
        if choice==1 :
            menu_chapter2()
        elif choice==2:
            print(30 * "-", "Chapter#3-Interpolation and Polynomial Approximation", 30 * "-")
            choice_2=int(input("1. Lagrange\n2. Divided Differences"))
            if choice_2==1:
                lagrange()
            elif choice_2==2:
                Diff()


