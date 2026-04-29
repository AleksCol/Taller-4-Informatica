pi = 3.1416

def area_esf(r):
    area = pi*(r)**2
    
    return area

def diametro_esf(r):
    diametro_esf = (2)*(r)
    
    return diametro_esf 

def circ_max(r):
    circunferencia = 2*(pi)*(r)
    
    return circunferencia

#convertir en modulo ejecutable
if __name__ == '__main__':
    r = float(input('Ingrese el radio de la esfera: '))
    area = area_esf(r)
    print('El area de la esfera es:', area)
    diametro = diametro_esf(r)
    print('El diametro de la esfera es:', diametro)
    circunferencia = circ_max(r)
    print('La circunferencia maxima de la esfera es:', circunferencia)
    