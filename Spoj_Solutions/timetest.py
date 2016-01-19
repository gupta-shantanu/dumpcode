import timeit
t=timeit.default_timer

t1=t()
import numpy
t2=t()
print(t2-t1)

t1=t()
import django
t2=t()
print(t2-t1)

t1=t()
import random
t2=t()
print(t2-t1)
