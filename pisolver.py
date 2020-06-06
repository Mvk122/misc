"""
Solves for pi given random numbers between 0 and 1 
"""
from random import random 
def dist_from_origin(x,y):
    return (x**2 + y**2)**0.5
in_circle = 0
outside_circle = 0 
step = 100000
for i in range(step):
    x = random()
    y = random()
    if dist_from_origin(x,y) >= 1:
        outside_circle += 1
    else:
        in_circle += 1 
    
print(4 * in_circle/(outside_circle +in_circle))