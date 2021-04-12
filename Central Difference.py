import math

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
    return temp + temp2

def stirling_table(n):
    xtable=[]
    table=[[]]
    for i in range(0, n, 1):
        print("\nEnter value for x",i,":")
        xtable.append(float(input()))
    x=float(input("\nEnter value for x on which you would like to work on"))

    h=xtable[1]-xtable[0]
    p=xtable[math.ceil(len(xtable)/2)]-x/h
    for i in range(0, n, 1):
        print("\nEnter value for f(x",i,"):")
        table[0].append(float(input()))

    for i in range(1, n, 1):
        table.append([])
        for j in range(0, len(table[i-1])-1, 1):
            table[i].append(table[i-1][j]-table[i-1][j+1])





stirling_table(3)

print(1.49182 + stirling([0.27042,0.33030,0.05988], 0, 0.15) + stirling([0.01086,0.01324,0.00238], 1, 0.15)   )