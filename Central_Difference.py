import math
import numpy as np

# if (iterative_value == 0):
#     return values
# else:
#     if(iterative_value == 1):
#         return p*(values[0]+values[1])/2
#     elif(iterative_value == 2):
#         return ((p**2)/2)*values
#     else:
#         if(iterative_value%2!=0):
#             temp = p
#             for x in range(1, iterative_value, 1):
def factorial(n):
    fact = 1
    if n==0:
        return 1
    for i in range(1,n+1):
        fact = fact * i
    return fact


def stirling(values, iterative_value, p):
    temp=p
    temp2=p**2
    for x in range(1, iterative_value+1, 1):
        temp *= (p**2-x**x)
        temp2 *= (p**2-x**x)

    temp/=factorial(2*(iterative_value+1)-1)
    temp2/=factorial(2*(iterative_value+1))
    temp*=(values[0] + values[1])/2
    temp2*=values[2]
    print(" + "+str(temp), "+", temp2, end='')
    return temp + temp2

def stirling_table(n,round_off):
    if (n % 2 == 0):
        print("To acquire function’s values near the middle of a table where central difference interpolation\n"
              "formulas are applicable in which our new method is very suitable. This method employs\n"
              "differences lying as nearly as possible on a horizontal line through y0 in a diagonal difference\n"
              "table. The values you input MUST be odd in number for the center difference to work.\n")
        return 0

    # x=1.5
    # xtable = [1,1.3,1.6,1.9,2.1]
    # table=[[0.7651977,0.6200860,0.4554022,0.2818186,0.1103623]]
    # x = 0.5437
    # xtable = [0.51,0.52,0.53,0.54,0.55,0.56,0.57]
    # table=[[0.5292437, 0.5378987, 0.5464641, 0.5549392, 0.563323, 0.5716157, 0.57981]]
    # x=28
    # xtable=[20,25,30,35,40]
    # table=[[49225,48316,47236,45926,44306]]

    #------------Comment this part below and uncomment one of the above for experiment----------#
    xtable = []
    table = [[]]
    for i in range(0, n, 1):
        print("\nEnter value for x" + str(i) + ":")
        xtable.append(float(input()))
    x = float(input("\nEnter value for x on which you would like to work on:"))
    #------------Comment this part above and uncomment one of the above for experiment----------#

    for i in range(0, n, 1):
        print("\nEnter value for f(x" + str(i) + "):")
        table[0].append(float(input()))

    h = xtable[1] - xtable[0]
    p = (x - xtable[math.floor(len(xtable) / 2)]) / h
    for i in range(1, n, 1):
        table.append([])
        for j in range(0, len(table[i-1])-1, 1):
            table[i].append(round(table[i-1][j+1]-table[i-1][j],round_off))

    def superscript(n):
        return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c) - ord('0')] for c in str(n)])

    header=["x", "y"]
    for i in range(0, len(xtable)-1, 1):
        if i==0:
            header.append("Δy")
        else:
            header.append("Δ" + superscript(i+1) + "y")


    frmt = "{:>25}" * len(header)
    print(frmt.format(*header))
    for i in range(0, len(table), 1):
        if i==0:
            lst=[item[0] for item in table]
        else:
            lst = [item[i] for item in table[:-i]]
        lst.insert(0,xtable[i])
        frmt="{:>25}" * len(lst)
        print(frmt.format(*lst))






    matrix=[]
    final_stir= table[0][math.floor(len(xtable)/2)]
    print("\n\n\n\n\n"+ str(final_stir), end='')
    i=1
    j=0
    for i in range(1, n-1, 2):
        matrix.append([round(table[i][len(table[i])//2-1],round_off),round(table[i][len(table[i])//2],round_off), round(table[i+1][math.floor(len(table[i])//2)-1],round_off)])
        final_stir+=stirling([round(table[i][len(table[i])//2-1],round_off),round(table[i][len(table[i])//2],round_off), round(table[i+1][math.floor(len(table[i])//2)-1],round_off)], j, p)
        j+=1
        matrix=[]

    return round(final_stir, round_off)

# b=int(input("Enter Range For Central Difference:"))
# c=int(input("Round-off to how many digits ? :"))
# print("\nYour answer for stirling is :",stirling_table(b,c))

