import copy
import sys
def peep(x):
    it=copy.copy(x)
    return next(x),it

itr=iter(range(10))
y,it=peep(itr)
print(y,list(it))
