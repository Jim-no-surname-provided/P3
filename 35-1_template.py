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

Aufgabe 35.1 der Aufgabensammlung
Bitte suchen Sie aus der Sympy-Dokumentation die nötigen Befehle.
Es würde bestimmt auch andere Lösungswege geben, aber die Übung dient dazu,
dass Sie sich mit solchen Dokumentationen vertraut machen.
"""
import sympy as sp
from sympy.abc import c,d,t
x = sp.Function('x')(t)

# Wahl geeignete Masse und Startpunkt
m = 10e-3
x0 = 5e-5

# Definition der DGL und seiner Lösung
f = TODO #DGL
x = TODO # Lösung - Hinweis: dsolve

print("Differentialgleichung:")
sp.pprint(f)

#Liste mit den Gleichungen des GLS
eq = [sp.Eq(x.subs(t, 0),x0),
      sp.Eq(x.diff(t, 1).subs(t, 0), 0)]


#Berechnung der Startbedingungen
C1, C2 = list(sp.linsolve(TODO))[0]
x = TODO

# 3 Beispiele mit verschiedenen Werten für c und d
x1 = x.subs(c,0.36).subs(d,0.02) 
x2 = x.subs(c,0.01).subs(d,0.021)
x3 = x.subs(c,0.21).subs(d,0.02)


# Lösungsplots für t=0..5
p = sp.plot(TODO)
p[0].line_color = "orange"
p[1].line_color = 'green'
p.show()