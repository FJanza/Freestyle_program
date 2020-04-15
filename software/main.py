import math
x = float(input('indique el valor de x: '))
y = float(input('indique el valor de y: '))

print('selecciona la operacion que desees realizar')

print('1 sumar')
print('2 restar')
print('3 multiplicar')
print('4 dividir')
print('5 potencia')

n = int(input('cual opcion se solicita: '))

if n==1:
    resultado=x+y
    print(resultado)

if n==2:
    resultado = x - y
    print(resultado)

if n==3:
    resultado= x * y
    print(resultado)

if n==4 and y>0:
    resultado= x / y
    print(resultado)

if n==5:
    resultado=x**y
    print(resultado)

