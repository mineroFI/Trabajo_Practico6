import math

def redondear(x):
    if x > 3.50:
        return math.ceil(x)
    else:
        return math.floor(x)