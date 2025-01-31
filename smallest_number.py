# ""wap to find the largest number among the 4 numbers ""

a = int(input("enter first number  "))
b = int(input("enter second number  "))
c = int(input("enter thid number  "))
d = int(input("enter forth number  "))

if (a < b and a < c and a < d):
    print("the smallest number is a")
elif (b < c and b < d):
    print("the smallest number is b")
elif (c < d):
    print("the smallest number is c")
else:
    print("the smallest number is d")
