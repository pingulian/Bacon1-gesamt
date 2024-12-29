import numpy as np
import sympy

class panic(Exception):
    def __init__(self, message = "panic", errors = None):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

val1 = np.array([1,4,9,10])
val2 = np.array([1,8,27,31.62])
terme = [np.zeros_like(val1)]



def ratio (val1, val2):
    ratio = (val1/val2)     #/-operator für numpy-arrays implementiert deshalb okay
    return ratio

def product (val1, val2):
    prod = val1*val2
    return prod

def maxerror(values):
    e = max(np.abs((np.average(values)-np.max(values))), np.abs((np.average(values)-np.min(values))))
    return e

term = ""
v1 = "a"
v2 = "b"
termstrings = []
n = 0

while maxerror(val2) > 0.1:

    if np.all(np.diff(val1) > 0):
        if np.all(np.diff(val2) > 0):
            terme[n] = ratio(val1,val2)
            termstrings.append("(" + v1 + "/" + v2+ ")")
        elif np.all(np.diff(val2) < 0):
            terme[n] = product(val1,val2)
            termstrings.append("(" + v1 + "*" + v2+ ")")
        else:
            raise panic(message = "val2 nicht monoton")
    elif np.all(np.diff(val1) < 0):
        if np.all(np.diff(val2) > 0):
            terme[n] = product(val1,val2)
            termstrings.append("(" + v1 + "*" + v2+ ")")
        elif np.all(np.diff(val2) < 0):
            terme[n] = ratio(val1,val2)
            termstrings.append("(" + v1 + "/" + v2+ ")")
        else:
            raise panic(message = "val2 nicht monoton")
    
    else:
        raise panic("val1 nicht monoton")

    
    val1 = val2
    val2 = terme[n]
    terme.append(np.zeros_like(val1))
    v1 = v2
    v2 = termstrings[n]
    n+=1
print (termstrings[-1])
print("c= " + str(val2[-1]))
sympy.sympify(termstrings[-1])



