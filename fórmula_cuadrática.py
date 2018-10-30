#Santiago Gabriel Vallejo García A01631816
#Daniel Efren Velázquez Lara A01636246  hi
from math import sqrt
a=int(input("Escribe el coeficiente de x^2 de tu función cuadrática. "))
b=int(input("Escribe el coeficiente de x de tu función cuadrática. "))
c=int(input("Escribe el término independiente de tu función cuadrática. "))
if (a==0):
    if (b==0):
        print("Esto no es una ecuación.")
    else:
        x=-c/b
        print(x)
else:
    if (b**2-4*a*c<0):
        print("Tenemos una solución imaginaria!!")
        x1=complex(-b/(2*a),(sqrt(abs(b**2-4*a*c))/(2*a)))
        x2=complex(-b/(2*a),-(sqrt(abs(b**2-4*a*c))/(2*a)))
        print (x1,x2)
    elif (b**2-4*a*c>0):
        x1=(-b+sqrt(b**2-4*a*c))/(2*a)
        x2 =(-b-sqrt(b**2-4*a*c))/(2*a)
        print(x1, x2)
    else:
        x1 = (-b/(2 * a))
        x2 = (-b/(2 * a))
        print(x1, x2)
