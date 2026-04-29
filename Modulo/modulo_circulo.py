pi = 3.1416

def area_circ(r):
    
    area = pi*(r)**2
    
    return area

def vol_circ(r):
    volumen = (4/3)*pi*(r)**3
    
    return volumen 

def per_cir(r):
    
    permietro = 2*(pi)*(r)    
    
    return permietro

#convertir en modulo ejecutable
if __name__ == '__main__':
    r = float(input('Ingrese el radio del circulo: '))
    area = area_circ(r)
    print('El area del circulo es:', area)
    perimetro = per_cir(r)
    print('El perimetro del circulo es:', perimetro)
    