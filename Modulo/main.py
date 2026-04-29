from modulo_circulo import *
from modulo_esfera import *
from modulo_cuadrado import *
from modulo_cubo import *

tipo = input('Ingrese la forma a evaluar: (circulo, esfera, cuadrado, cubo): ')
valor = float(input('Ingrese el valor de la forma geometrica: '))

if tipo == 'circulo':
    calculo = input('Que desea calcular, area o perimetro? ')
    if calculo == 'area':
        area = area_circ(valor)
        print('El area del circulo es:', area)
    else:
        perimetro = per_cir(valor)
        print('El perimetro del circulo es:', perimetro)

elif tipo == 'esfera':
    calculo = input('Que desea calcular, area, diametro o circunferencia? ')
    if calculo == 'area':
        area = area_esf(valor)
        print('El area de la esfera es:', area)
    elif calculo == 'diametro':
        diametro = diametro_esf(valor)
        print('El diametro de la esfera es:', diametro)
    elif calculo == 'circunferencia':
        circunferencia = circ_max(valor)
        print('La circunferencia maxima de la esfera es:', circunferencia)

elif tipo == 'cuadrado':
    calculo = input('Que desea calcular, area o perimetro? ')
    if calculo == 'area':
        area = area_cuad(valor)
        print('El area del cuadrado es:', area)
    else:
        perimetro = per_cuad(valor)
        print('El perimetro del cuadrado es:', perimetro)
        
elif tipo == 'cubo':
    calculo = input('Que desea calcular, area o perimetro? ')
    if calculo == 'area':
        area = area_cubo(valor)
        print('El area del cubo es:', area)
    else:
        perimetro = per_cubo(valor)
        print('El perimetro del cubo es:', perimetro)   