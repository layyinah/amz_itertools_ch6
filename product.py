import sys


def product(p1,p2):
    if p1 ==0 or p2 == 0:
        return 0
    else:
        return p1+product(p1,p2-1)
print("product of  two numbers :")
print(product(5,6))

# print(product(sys.argv[1],sys.argv[2]))