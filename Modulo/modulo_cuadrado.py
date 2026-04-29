#Area, perimetro y volumen de un cuadrado 

def area_cuad(l):
    area = (l)**2
    
    return area

def vol_cuad(l):
    volumen = (l)**3
    
    return volumen

def per_cuad(l):
    perimetro = 4*(l)
    
    return perimetro


#convertir en modulo ejecutable
if __name__ == '__main__':
    l = float(input('Ingrese el lado del cuadrado: '))
    area = area_cuad(l)
    print('El area del cuadrado es:', area)
    perimetro = per_cuad(l)
    print('El perimetro del cuadrado es:', perimetro)