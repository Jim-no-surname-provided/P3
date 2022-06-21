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

A36.2 - Mehrdimensionale Integralrechnung

Bitte suchen Sie aus der Sympy-Dokumentation die nötigen Befehle.
Es würde bestimmt auch andere Lösungswege geben, aber die Übung dient dazu,
dass Sie sich mit solchen Dokumentationen vertraut machen.
"""

import sympy as sp

var = [r, theta, phi] = sp.symbols("r, theta, phi")
R = 4

#Geben Sie die Angabe in einer sp Matrix ein
x = TODO

#a) Erstellen eines 3 dimensionalen Plots
x1 = x.subs(r,1)
p = sp.plotting.plot3d_parametric_surface(TODO)

#b) Oberflächenberechnung
# Bestimmen Sie das Kreuzprodukt (ggf. mit zwischenvariablen)
crossp = TODO

print("\nDie Oberfläche des Torus beträgt: ")
# Implementieren sie hier die Berechnung der Oberfläche
O = TODO.doit()
sp.pprint(O)

#c) Volumensberechnung
y = sp.Matrix(var)
j_det =  TODO #Bestimmen Sie die Jacobi-Determinante

print("\nDas Volumen des Torus beträgt: ")
# Implementieren sie hier die Berechnung des Volumens
V = TODO.doit())
sp.pprint(V)

