n = int(input())
a = int(input())
b = int(input())

for i in range(1,n+1):
    
    if (i % a == 0) and (i % b == 0):
        print("ITCCC")
    elif (i % a == 0) and (i % b != 0):
        print("IT")
    elif (i % a != 0) and (i % b == 0):
        print("CCC")
    else:
        print(i)
