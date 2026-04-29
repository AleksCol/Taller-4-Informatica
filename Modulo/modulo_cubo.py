#Area, perimetro y volumen de un cubo

def area_cubo(l):
    area = 6*(l)**2
    
    return area 

def vol_cubo(l):
    volumen = (l)**3
    
    return volumen  

def per_cubo(l):
    perimetro = 12*(l)
    
    return perimetro

#convertir en modulo ejecutable
if __name__ == '__main__':
    l = float(input('Ingrese el lado del cubo: '))
    area = area_cubo(l)
    print('El area del cubo es:', area)
    perimetro = per_cubo(l)
    print('El perimetro del cubo es:', perimetro)