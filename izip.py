import sys


def izip(iter1,iter2):
    for i ,j in zip(iter1,iter2):
        print(i,j)

izip(sys.argv[1],sys.argv[2])