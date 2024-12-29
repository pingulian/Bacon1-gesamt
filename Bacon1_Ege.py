import numpy as np
import sympy
c=False
Daten1=numpy.array([1,4,9])
Daten2=numpy.array([1,8,27])
def prozent(prozent, ganz):
    return (prozent*ganz)/100
def erhöhung(k,l):
    e=None
    for n in range(len(k)):
        if (k[n]>k[n-1]) and (l[n]>l[n-1]):
            e=True
        elif (k[n]>k[n-1]) and (l[n]<l[n-1]) or (k[n]<k[n-1]) and (l[n]>l[n-1]):
            e=False
    return e
def konstant(p):
    mittelwert=numpy.mean(p)
    intervall1=prozent(100-int(abweichung),mittelwert)
    intervall2=prozent(100+int(abweichung),mittelwert)
    for b in range(len(p)):
        if (p[b]>=intervall1) and (p[b]<=intervall2):
            c=True
        else:
            c=False
    return c
term = ""
v1 = "a"
v2 = "b"
termstrings = []
n=0
abweichung=input("Abweichung in Prozent")
while c==False:
    if (erhöhung(Daten1,Daten2)==True):
        Daten3=Daten1/Daten2
        termstrings.append("(" + v1 + "/" + v2+ ")")
    if (erhöhung(Daten1,Daten2)==False):
        Daten3=Daten1*Daten2
        termstrings.append("(" + v1 + "*" + v2+ ")")
    c=konstant(Daten3)
    Daten1 = Daten2
    Daten2 = Daten3
    print(Daten3)
    v1 = v2
    v2 = termstrings[n]
    n+=1
print (termstrings[-1])
sympy.sympify(termstrings[-1])
