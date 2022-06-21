"""
@ authors: 
    
Autor:
Matr.Nr.:

Autor:
Matr.Nr.:

Autor:
Matr.Nr.:

Autor:
Matr.Nr.:

Aufgabe 35.2 der Aufgabensammlung
Bitte suchen Sie aus der Sympy-Dokumentation die nötigen Befehle.
Es würde bestimmt auch andere Lösungswege geben, aber die Übung dient dazu,
dass Sie sich mit solchen Dokumentationen vertraut machen.
"""

import sympy as sp
t, a, b  = sp.symbols( TODO ) #Hinweis: Erstellen sie rein reelle Symbole

#Richtungsvektor
x = TODO #Hinweis: erstellen sie eine Matrix

#Geschwindigkeitsvektor
v = TODO

#Bahngeschwindigkeit
s = TODO 

#Beschleunigung
a = TODO

#Tangenteneinheitsvektor
T = TODO

#Für den Hauptnormaleneinheitsvektor udn die Krümmung wäre es sinnvoll einen zwischenvariable auszurechnen
# Hauptnormaleneinheitsvektor
N = TODO

#Krümmung
k = TODO

print("Bahngeschwindigkeit s:")
sp.pprint(s)

print("\n\nBeschleunigung a:")
sp.pprint(a)

print("\n\nTangenteneinheitsvektor T:")
sp.pprint(T)

print("\n\nHauptnormaleneinheitsvektor N:")
sp.pprint(TODO) #Geben Sie den Hauptnormaleneinheitsvektor vereinfacht aus

print("\n\nKrümmung k:")
sp.pprint(k) #Geben Sie die Krümmung vereinfacht aus

