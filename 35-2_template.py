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
from textwrap import wrap
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
T_diff = sp.diff(T, t)
N = T_diff / sp.sqrt(T_diff.dot(T_diff))

# Krümmung
K = T_diff / s
k = sp.sqrt(K.dot(K))

print("Bahngeschwindigkeit s:")
sp.pprint(s)

print("\n\nBeschleunigung a:")
sp.pprint(a)

print("\n\nTangenteneinheitsvektor T:")
# Inspired in: https://stackoverflow.com/a/39692039/16790196
g = sp.simplify(sp.gcd(tuple(T)))   # Get common factor
T = sp.MatMul(g, (T/g), evaluate=False)
sp.pprint(T)

print("\n\nHauptnormaleneinheitsvektor N:")
N.simplify()
# Inspired in: https://stackoverflow.com/a/39692039/16790196
g = sp.simplify(sp.gcd(tuple(N)))   # Get common factor
N = sp.MatMul(g, (N/g), evaluate=False)
# Geben Sie den Hauptnormaleneinheitsvektor vereinfacht aus
sp.pprint(N, wrap_line=False)


print("\n\nKrümmung k:")
sp.pprint(sp.simplify(k))  # Geben Sie die Krümmung vereinfacht aus
