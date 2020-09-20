#!/usr/bin/env python
# coding: utf-8

print ("Tener en cuenta que todas las medidas deben entregarse en el sistema internacional y en el orden constante elástica, masa y elongación inicial")

class Oscilador:

#La forma de comentar se debe a varios errores de identacion al usar """ """, se optó por el 
#metodo __init__ no comentado porque causa una comodidad en la ejecución para ser calificado

#al inicializar la clase Oscilador se tendrá que dar los valores k,m,y0 con los cuales se podrá calcular la frecuencia 
#del sistema (frecuencia angular que en literatura varia se le llama simplemente frecuencia pero hay que diferencialas) 

    def __init__(self,k,m,y0):
        from numpy import sqrt
        self.k = k
        self.m = m
        self.y0 = y0
        self.omega = sqrt(self.k/self.m)


#    def __init__(self):
#        from numpy import sqrt
#        self.k = float(input("ingrese el valor de la constante k del resorte en N/m: "))
#        self.m = float(input("ingrese el valor de la masa del cuerpo que cuelga del resorte en Kg: "))
#        self.y0 = float(input("ingrese el valor de la elongacion respeccto al equilibrio del resorte al iniciar en m: "))
#        self.omega = sqrt(self.k/self.m)

#########################################################################################################################

#Se crea un método que calcula el movimiento con los atributos anteriores (k,m,y0,frecuencia) el cual suponiendo 
#la velocidad inicial nula nos entrega la ecuación y = y_0 cos(wt)

#Usando la librería scipy se deriva el anterior modulo para hallar la velocidad, usando dx = 10^-10(tercer entrada de 
#derivative)se halla una buena aproximación entre la velocidad y ella misma por integración de la EDO


    def movimiento (self,t):
        
        from numpy import cos
        return self.y0 * cos(self.omega * t)
    
    def velocidad (self,t):
        
        from scipy.misc import derivative
        return derivative(self.movimiento,t,10**-10)
####################################################################################################################################

#Se hace lo mismo que en el método anterior pero por medio de integrar la EDO de un oscilador armónico bajos
#las mismas condiciones
    def movimiento_edo (self,t):
        
        from scipy.integrate import odeint
        self.Y0=[self.y0,0]
        def osc(x,t):
            return [x[1],-(self.omega**2)*x[0]]
        
        return odeint (osc,self.Y0,t)
    
class OsciladorAmortiguado:
    
    def __init__(self,k,m,y0,Lambda):
        from numpy import sqrt
        self.k = k
        self.m = m
        self.y0 = y0
        self.Lambda = Lambda
        self.omega = sqrt(self.k/self.m)

#Tomando la ecuación  25.3 del libro "mecánica" de "Lev Landau" se tiene la ecuación diferencia del oscilador amortiguado 
#que causa una comodidad a la hora de manipularla, el caso subamortiguado se da cuando lambda es menor omega, el analisis
#en dicho libro se hace con lambda mucho menor a omega, en plots anteriores a la entrega se observa que se debe que en 
#casos cercanos no hay diferencia al caso críticamente amortiguado

#Análogo al caso del oscilador libre se soluciona con scipy la EDO del oscilador amortiguado teniendo en cuenta
#lo anterior mencionado para el caso deseado(el subamortiguado)

    def movimiento_edo (self,t):
        
        from scipy.integrate import odeint
        self.Y0=[self.y0,0]
        
        def osc(x,t):
            return [x[1],-((self.omega**2)*x[0] + 2*self.Lambda*x[1]/self.m)]
        
        return odeint (osc,self.Y0,t)
#########################################################################################################

#Los métodos elegidos son los preferidos para el graficar y vs v que en el caso libre a diferencia de una constante es el espacio de fases cosa que no es necesariamente igual en el caso subamortiguado (o hasta mi memoria llega)