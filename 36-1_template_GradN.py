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

A36.1 - Taylorpolynom

Bitte suchen Sie aus der Sympy-Dokumentation die nötigen Befehle raus.
Es würde bestimmt auch andere Lösungswege geben, aber die Übung dient dazu,
dass Sie sich mit solchen Dokumentationen vertraut machen.
"""

# %% Version 2 - Beschleunigte Berechnung des Taylorpolynoms n-ten Grades unter Ausnutzung
# %% des Satz von Schwartz und der Binomialkoeffizienten (Pascalsches Dreieck)
import sympy as sp
from sympy.abc import x, y
from sympy.ntheory import binomial_coefficients_list as bcl  # für Pascalsches Dreieck
"""
Geht man davon aus, dass eine Funktion f(x,y) von 2 Variablen abhängt,
muss man diese für das Taylorpolynom auch nach beiden Variablen ableiten.
Wäre die Funktion von 3 Variablen (x,y,z) abhängig muss man immer nach allen 3 Variablen ableiten.

Für diese Aufgabe reicht es uns, dass das Program nur für 2 unabhängige Variablen ausgelegt wird.

Weiters steigt die Komplexität eines mehrdimensionales Taylerpolynoms mit Erhöhung des
Näherungsgrades rasch an. Wird der Näherungsgrad um eins erhöht, so wird die mehrdimensionale Matrix 
mit den Ableitungen doppelt so groß:
    
len(f) = 1
len(grad) = 2
len(hess) = 4
len(derivate(hess, [x,y])) = 8
usw...

Das heißt für ein Taylorpolynom 10. Grades müssen in Summe i ∈ [0,10]: sum(2^i) = 2047 Ableitungen 
berechnet werden. Bei einem Taylorpolynom 40. Grades würde das 2^41-1 Ableitungen bedeuten.
Mit einem Programm dauert das Ableiten einer Funktion zwar nicht lange, aber es summiert sich.

Wir wissen, dass für Funktionen, die die Vorausstetzungen für den Satz von Schwartz erfüllen, 
einige Ableitungen zum gleichen Termausdruck führen, zB :

d²f/(dxdy) =d²f(dydx)

Dies bedeutet insbesondere, dass für geeignete Funktionen 
die Hessematrix mit 4 Einträgen nur 3 unterschiedliche Termausdrücke zu finden sind
auf der nächsten Stufe mit 8 Einträgen gibt es 4 unterschiedliche Termausdrücke,
bei 16 gibt es 5
bei 32 gibt es 6
bei 64 gibt es 7 usw.

Wir bemerken auch, dass die Häufigkeit der verschiedenen Termausdrücke mit dem Pascalschen Dreieck
zusammenhängt:

    0. Grad: 1*f
    1. Grad: 1*df/dx, 1*df/dy
    2. Grad: 1*d²f/dx², 2*d²f/dxdy, 1*d²f/dy²
    3. Grad: 1*d3f/dx3, 3*d³f/dx²dy, 3*d³f/dxdy², 1*d³f/dy³
    ...
    
    also [1], [1,1], [1,2,1], [1,3,3,1], ... bcl(k)
    
Weiters ist noch der Richtungsvektor v=(v_x,v_y) zu berücksichtigen: 
    
Wurde die Funktion beispielsweise 2 mal nach x und einmal nach y abgeleitet (d³f/dx²dy, d³f/dxdydx, d³f/dydx²), 
so muss dieser Term für das Taylorpolynom auch noch nach mit (v_x)^2 und (v_y)^1 multipliziert werden.

Der zugehörige Summand des 3. Grades würde dann beispielsweise so aussehen (exkl. Faktor 1/deg!):
    binom(3,2) * d³f/dx²dy * (v_x)^2 * (v_y)^1
    
Abschließend werden die Terme aufsummiert und man erhält die Lösung.

Das nachfolgende Programm soll dieser Schritte ausführen. 
"""
# Festleung des Grads des Taylorpolynoms
approx = 2

# funktion
f = x*sp.sin(y) + y*sp.sin(x)  # übertragen Sie die Angabe

# Entwicklungspunkt
x0 = sp.pi / 2  # übertragen Sie die Angabe
y0 = 0          # übertragen Sie die Angabe

print('Angabe: \nf(x,y) = {}'.format(sp.pretty(f)))
print("\nRichtungsvektor: ")
v = sp.Matrix([
    sp.Derivative(f, x).doit(),
    sp.Derivative(f, y).doit(),
])  # Hinweis: Geben sie den Richtungsvektor als Matrix an

sp.pprint(v)

# Lösungsterm initialisieren
solution = 0

# für jeden Grad des Taylerpolynomes wird ein Term addiert
for k in range(approx+1):

  # Berechnung von dem nächsten Näherungsterm mithilfe von dem Pascalschen Dreieck
  # und Ausnutzung von Satz von Schwartz
    i, termsk = 0, 0

    while i <= k:
        partdevf = sp.diff(f, x)  # Ermittlung der partiellen Ableitung
        partdevfAt = partdevf.subs(x, x0).subs(y, y0)  # Einsetzen des Entwicklungspunktes in die Ableitung
        add = bcl(k)[i] * TODO  # Bestimmung des Terms inkl. Häufigkeit
        termsk += add  # Ergänzung zu den Termen der Approximation vom Grad k
        i += 1

    # Addition der normierten Terme der Approximation vom Grad k zum Taylorpolynom vom Grad k-1, Hinweis sp.factorial
    solution += TODO

solution = solution.simplify()

# Rückgabe des Ergebnisses
print("\nTaylorpolynom vom Grad {}: ".format(approx))
sp.pprint(solution)
