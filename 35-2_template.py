"""
@ authors: 
    
Autor: Helmut Joaquín Pfeffer
Matr.Nr.: k12105862

Autor: Rainer Grobauer
Matr.Nr.: k1238053

Autor: Hannes Maislinger
Matr.Nr.: k01455994

Autor: Zinedin Puškar
Matr.Nr.: k12043388

Aufgabe 35.2 der Aufgabensammlung

Bitte suchen Sie aus der Sympy-Dokumentation die nötigen Befehle.
Es würde bestimmt auch andere Lösungswege geben, aber die Übung dient dazu,
dass Sie sich mit solchen Dokumentationen vertraut machen.
"""
# %%
import sympy as sp
t, a, b = sp.symbols('t a b')  # Hinweis: Erstellen sie rein reelle Symbole

# Richtungsvektor
x = sp.Matrix([
    a*sp.cos(t),
    b*sp.sin(t)
])  # Hinweis: erstellen sie eine Matrix

# Geschwindigkeitsvektor
v = sp.diff(x, t)

# Bahngeschwindigkeit
s = sp.sqrt(v.dot(v))

# Beschleunigung
a = sp.diff(v, t)

# Tangenteneinheitsvektor
T = v/s

# Für den Hauptnormaleneinheitsvektor und die Krümmung wäre es sinnvoll einen zwischenvariable auszurechnen
# Hauptnormaleneinheitsvektor
N = 

sp.pprint(T)
# %%

# Krümmung
k = TODO

print("Bahngeschwindigkeit s:")
sp.pprint(s)

print("\n\nBeschleunigung a:")
sp.pprint(a)

print("\n\nTangenteneinheitsvektor T:")
sp.pprint(T)

print("\n\nHauptnormaleneinheitsvektor N:")
sp.pprint(TODO)  # Geben Sie den Hauptnormaleneinheitsvektor vereinfacht aus

print("\n\nKrümmung k:")
sp.pprint(k)  # Geben Sie die Krümmung vereinfacht aus
