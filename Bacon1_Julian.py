import numpy as np
import sys

# Werte aus Boyles Experiment
#x = np.array([1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0])
#y = np.array([29.750, 19.125, 14.375, 9.5, 7.125, 5.625, 4.875, 4.250, 3.750, 3.375, 3.0, 2.625, 2.250, 2.0, 1.875, 1.750, 1.5, 1.375, 1.250])

# Werte aus Keplers Experiment
x = np.array([1.0, 4.0, 9.0]) #Distance (D)
y = np.array([1.0, 8.0, 27.0]) #Period(P)

# andere synthetische Werte (für x / y ↑ 3 = c)
#x = np.array([1, 8, 64])
#y = np.array([1, 2, 4])

#zufälliger Fehler
relative_error = 0.01
random_index = np.random.randint(0, len(y))
random_error = np.random.normal(loc=0, scale=relative_error * y[random_index])
y[random_index] += random_error

averagex = np.mean(x)
averagey = np.mean(y)
maxerlabweichung = 30 # Maximal zugelassene Abweichung in %
a = 1 #Exponent für x für print
b = 1 #Exponent für y für print
c = 1 #counter
d = 1 #für while

#Funktion zur Berechnung von Durchschnitt, Min, Max und Abweichung
def min_max_abw():
    # Berechnung von Durchschnitt, Maximal- und Minimalwert
    average = np.mean(xy)
    maxxy = np.max(xy)
    minxy = np.min(xy)

    # Maximalen Abweichung vom Durchschnitt
    abweichungnumb = np.abs([maxxy - average, minxy - average])
    maxabweichungnumb = np.max(abweichungnumb)

    #Abweichung in %
    abweichung = (maxabweichungnumb / average) * 100

    return average, maxxy, minxy, maxabweichungnumb, abweichung

# im Falle eines antiproportinalen Zusammenhangs
def antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung):
    # Überprüfung der Abweichung
    if abweichung < maxerlabweichung:
        print("\n\n\n")
        # Ergebnisse ausgeben
        print(" - x entspricht D (Distance); y entspricht P (Period) - ")
        print("Durchschnitt von (x ↑",a,"* y ↑",b,"):", average)
        print("Maximaler Wert:", maxxy)
        print("Minimaler Wert:", minxy)
        print("\nMaximale Abweichung vom Durchschnitt (Absolute Zahl):", maxabweichungnumb)
        print("Maximale Abweichung vom Durchschnitt (%):", abweichung, "%")
        print("Maximal zugelassene Abweichung:", maxerlabweichung, "%")
        print("\nErgebnis:")
        
        print("(x ↑",a,"* y ↑",b,") = konstant (antiproportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung nicht)")
        sys.exit()
    else:
        print("(x ↑",a,"* y ↑",b,") ist nicht konstant (nicht antiproportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung)")
        

# im Falle eines proportionalen Zusammenhangs
def proportional(average, maxxy, minxy, maxabweichungnumb, abweichung):
    # Überprüfung der Abweichung
    if abweichung < maxerlabweichung:
        print("\n\n\n")
        # Ergebnisse ausgeben
        print(" - x entspricht D (Distance); y entspricht P (Period) - ")
        print("Durchschnitt von (x ↑",a,"/ y ↑",b,"):", average)
        print("Maximaler Wert:", maxxy)
        print("Minimaler Wert:", minxy)
        print("\nMaximale Abweichung vom Durchschnitt (Absolute Zahl):", maxabweichungnumb)
        print("Maximale Abweichung vom Durchschnitt (%):", abweichung, "%")
        print("Maximal zugelassene Abweichung:", maxerlabweichung, "%")
        print("\nErgebnis:")
        
        print("(x ↑",a,"/ y ↑",b,") = konstant (proportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung nicht)")
        sys.exit()
    else:
        print("(x ↑",a,"/ y ↑",b,") ist nicht konstant (nicht proportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung)")

try:
    #Antiproportionaler Zusammenhang
    if (x[1] > x[-1] and y[1] < y[-1]) or (x[1] < x[-1] and y[1] > y[-1]):
        print("Antiproportionaler Zusammenhang 1")
        xy = x * y
        average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
        antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

        #Was soll passieren, wenn xy nicht konstantt ist (nicht antiproportional)?
        while d == 1: 
            if (xy[1] > xy[-1] and x[1] < x[-1]) or (xy[1] < xy[-1] and x[1] > x[-1]): #Antiproportional
                c = c + 1
                print("Zusammenhang", c )
                a = a + 1 #Exponent von x erhöhen
                xy = xy * x
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung)
        
            else: #Proportional
                c = c + 1
                print("Zusammenhang", c )
                b = b + 1 #Exponent von y erhöhen
                xy = xy / y
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

    #Proportionaler Zusammenhang
    else:
        print("Proportionaler Zusammenhang")
        xy = x / y
        average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
        proportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

        #Was soll passieren, wenn x/y nicht konstantt ist (nicht proportional) und xy nicht konstant ist (nicht antiproportional)?
        while d == 1:
            if (xy[1] > xy[-1] and x[1] > x[-1]) or (xy[1] < xy[-1] and x[1] < x[-1]): #Proportional
                c = c + 1
                print("Zusammenhang", c )
                b = b + 1 #Exponent von y erhöhen
                xy = xy / y
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                proportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

            else: #Antiproportional
                c = c + 1
                print("Zusammenhang", c )
                a = a + 1 #Exponent von x erhöhen
                xy = xy * x
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                proportional(average, maxxy, minxy, maxabweichungnumb, abweichung)


except SystemExit: #Dient dem Verhindern einer Errormessage bei Verwendung von sys.exit() Fehlerbehandlung:
    pass # Keine Fehlermeldung anzeigen, wenn das Programm gestoppt wurde
