import random as rd
import numpy as np
import subprocess as sb

yyy = "jjj"
xxx = 6
zzz = 6.3

jjj = rd.randint(0, 100)

print(jjj)

print(type(xxx))
print(type(yyy))
print(type(zzz))

print("Hello")
ggg = ["apple", "banana", "orange", "pear", "plum"]
print(type(ggg))

for i, item in enumerate(ggg):
    print(i)
    print(item)

ggg.append(xxx)
j = xxx / zzz
print(j)

print(ggg)
