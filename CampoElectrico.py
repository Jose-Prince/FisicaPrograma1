import math

def Ccono():
    pass

def CconoT():
    pass

def Chemisferio(Q,R,d): #Q = carga, R = radio, d = distancia de la figura a la partícula
    constante = (3*Q)/(4*math.pi*(8.85*10**-12)*R**3)
    frac1 = -(d*math.log(abs(2**1/2*(2*R**2-2*(d+2*R)*R+d**2+2*R*d+2*R)**1/2-d)))/(2**3/2)+d/2+R
    frac2 = (d*math.log(abs(2**1/2*(d**2+2*R*d+2*R**2)**1/2-d-2*R)))/(2**3/2)+((-d-R)**2+R**2)**1/2/(2)
    
    resultado = constante*(frac1+frac2)