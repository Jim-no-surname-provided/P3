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

A36.2 - Mehrdimensionale Integralrechnung

Bitte suchen Sie aus der Sympy-Dokumentation die nötigen Befehle.
Es würde bestimmt auch andere Lösungswege geben, aber die Übung dient dazu,
dass Sie sich mit solchen Dokumentationen vertraut machen.
"""
import sympy as sp

var = [r, theta, phi] = sp.symbols("r, θ, φ")
R = 4

# Geben Sie die Angabe in einer sp Matrix ein
x = sp.Matrix([
    (R + r * sp.cos(theta)) * sp.cos(phi),
    (R + r * sp.cos(theta)) * sp.sin(phi),
    r * sp.sin(theta)
])

# a) Erstellen eines 3 dimensionalen Plots
x1 = x.subs(r, 1)
p = sp.plotting.plot3d_parametric_surface(
    x1[0],
    x1[1],
    x1[2],
    (theta, 0, 2 * sp.pi),
    (phi, 0, 2 * sp.pi))

# b) Oberflächenberechnung
# Bestimmen Sie das Kreuzprodukt (ggf. mit zwischenvariablen)
x_theta = sp.Derivative(x1, theta, evaluate=True)
x_phi = sp.Derivative(x1, phi, evaluate=True)

crossp = x_theta.cross(x_phi).simplify()

crossp_mag = sp.sqrt(crossp.dot(crossp).simplify())

print("\nDie Oberfläche des Torus beträgt: ")
# Implementieren sie hier die Berechnung der Oberfläche
O = sp.integrate(crossp_mag,
                 (phi, 2 * sp.pi, 0),
                 (theta, 2 * sp.pi, 0)
                 )
sp.pprint(O)

# c) Volumensberechnung
y = sp.Matrix(var)
# Bestimmen Sie die Jacobi-Determinante
j_det = sp.det(x.jacobian(y)).simplify()

print("\nDas Volumen des Torus beträgt: ")
# Implementieren sie hier die Berechnung des Volumens
V = sp.integrate(j_det,
                 (phi,  2 * sp.pi, 0,),
                 (theta, 2 * sp.pi, 0),
                 (r, 1, 0)
                 )
sp.pprint(V)
