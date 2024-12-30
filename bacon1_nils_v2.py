import numpy as np
import sympy

class panic(Exception):
    def __init__(self, message = "panic", errors = None):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

maxabweichungprozent = 5   #maximale Abweichung in Prozent
fehler_prozent = 1   #synthetischer Fehler

val1 = np.array([1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0])
val2 = np.array([29.750, 19.125, 14.375, 9.5, 7.125, 5.625, 4.875, 4.250, 3.750, 3.375, 3.0, 2.625, 2.250, 2.0, 1.875, 1.750, 1.5, 1.375, 1.250])

#val1 = np.array([1.0,4.0,9.0])               #Werte 1  
#val2 = np.array([1.0,8.0,27.0])              #Werte 2

terme = [np.zeros_like(val1)]

def synth_fehler(arr,fehlerprozent):
    index = np.random.randint(0,len(arr))
    arr[index] += arr[index] * (fehlerprozent/100)
    return arr

def ratio (val1, val2):
    ratio = (val1/val2)     #/-operator für numpy-arrays implementiert deshalb okay
    return ratio

def product (val1, val2):
    prod = val1*val2
    return prod

def maxerror(values):   #maximale Abweichung vom Mittelwert 
    e = max(np.abs((np.average(values)-np.max(values))), np.abs((np.average(values)-np.min(values))))
    return e

def nichtkonstant(arr,maxabweichungprozent):          #array konstant mit toleranz
    if maxerror(arr) > (maxabweichungprozent/100):
        return True

def monoton_fallend(arr, error_margin_percent):     #array monotom fallend mit toleranz
    error_margin = error_margin_percent / 100
    m = []
    for i in range(0, len(arr)-1 ):
        m.append((arr[i + 1] * (1 - error_margin) < arr[i]) or (arr[i + 1] < arr[i]))
        #print(arr[i + 1] * (1 - error_margin), arr[i],(arr[i + 1] * (1 - error_margin) < arr[i]),arr[i + 1],arr[i],(arr[i + 1] < arr[i]))
    return np.all(m)

def monoton_steigend(arr, error_margin_percent):    #array monoton steigend mit toleranz
    error_margin = error_margin_percent / 100
    m = []
    for i in range(0, len(arr)-1 ):
        m.append((arr[i + 1] * (1 + error_margin) > arr[i]) or (arr[i + 1] > arr[i]))
    return np.all(m)

val2_new = synth_fehler(val2,fehler_prozent)    #Fehler erzeugen
print(val2_new)
val2 = val2_new


term = ""
v1 = "a"    #spätere variablennamen
v2 = "b"    #spätere variablennamen
termstrings = []
n = 0

while nichtkonstant(val2,maxabweichungprozent):             #nicht konstant

    if monoton_steigend(val1, maxabweichungprozent):        #val1 monoton steigend
        if monoton_steigend(val2, maxabweichungprozent):    #val2 monoton steigend
            terme[n] = ratio(val1,val2)                     #quotient bilden
            termstrings.append("(" + v1 + "/" + v2+ ")")    #neuen term hinzufügen
        elif monoton_fallend(val2, maxabweichungprozent):   #val2 monoton fallend
            terme[n] = product(val1,val2)                   #produkt bilden
            termstrings.append("(" + v1 + "*" + v2+ ")")    #neuen term hinzufügen
        else:
            raise panic(message = "val2 nicht monoton " + str(val2) + " " + str(n))     #val2 nicht monoton --> panic
    elif monoton_fallend(val1, maxabweichungprozent):
        if monoton_steigend(val2, maxabweichungprozent):
            terme[n] = product(val1,val2)
            termstrings.append("(" + v1 + "*" + v2+ ")")
        elif monoton_fallend(val2, maxabweichungprozent):
            terme[n] = ratio(val1,val2)
            termstrings.append("(" + v1 + "/" + v2+ ")")
        else:
            raise panic(message = "val2 nicht monoton " + str(val2) + " " + str(n))
    else:
        raise panic(message = "val1 nicht monoton" + str(val1) + " " + str(n))
    

    val1 = val2
    val2 = terme[n]
    terme.append(np.zeros_like(val1))
    v1 = v2
    v2 = termstrings[n]
    n+=1
print (termstrings[-1])                 #term ausgeben (nicht vereinfacht)
print("c= " + str(np.average(val2)))    #Konstante c ausgeben
sympy.sympify(termstrings[-1])          #term vereinfachen


