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

Aufgabe 35.1 der Aufgabensammlung
Bitte suchen Sie aus der Sympy-Dokumentation die nötigen Befehle.
Es würde bestimmt auch andere Lösungswege geben, aber die Übung dient dazu,
dass Sie sich mit solchen Dokumentationen vertraut machen.
"""
import sympy as sp
from sympy.abc import c, d, t
x = sp.Function('x')(t)

# Wahl geeignete Masse und Startpunkt
m = 10e-3
x0 = 5e-5

# Definition der DGL und seiner Lösung
f = m*sp.diff(x, t, 2) + d*sp.diff(x, t) + c*x  # DGL
x = sp.dsolve(f, x).rhs      # Lösung - Hinweis: dsolve

print("Differentialgleichung:")
sp.pprint(f)

#Liste mit den Gleichungen des GLS
eq = [sp.Eq(x.subs(t, 0),x0),
      sp.Eq(sp.diff(x, t, 1).subs(t, 0), 0)]

#Berechnung der Startbedingungen
C1, C2 = list(sp.linsolve(eq, sp.symbols('C1'), sp.symbols('C2')))[0]
x = x.subs(sp.symbols('C1'), C1).subs(sp.symbols('C2'), C2)

# 3 Beispiele mit verschiedenen Werten für c und d
x1 = x.subs(c, 0.36).subs(d, 0.02)
x2 = x.subs(c, 0.01).subs(d, 0.021)
x3 = x.subs(c, 0.21).subs(d, 0.02)


# Lösungsplots für t=0..5
p = sp.plot((x1, (t, 0, 5)), (x2, (t, 0, 5)), (x3, (t, 0, 5)), show=False)
p[0].line_color = "orange"
p[1].line_color = 'green'
p.show()
