#!/usr/bin/env python
# coding: utf-8

#Modulo y librerías a usar
import MasaResorte as M
import numpy as np
import matplotlib.pyplot as plt

#6  osciladores con diferentes condiciones
a=M.Oscilador(3,2,1)
b=M.Oscilador(3,5,1)
c=M.Oscilador(3,3,1)
d=M.Oscilador(3,2,2)
e=M.Oscilador(0.4,2,1)
f=M.Oscilador(1.4,5.2,-6)

#tiempo de integración cada uno separado en una cantidad igual en 200 intervalos, cada elemento debe tener unidades
#de segundo para que la ecuación tenga sentido con el modulo importado
t=np.linspace(0,30,200)

#Gráficas para el oscilador armónico##########################################
fig, ([ax1, ax2], [ax3, ax4], [ax5, ax6]) = plt.subplots(3, 2,figsize=(15, 15))
ax1.plot(t,a.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(a.k,a.m,a.y0))
ax1.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax1.grid()
ax1.legend(loc="upper right")

ax2.plot(t,b.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(b.k,b.m,b.y0))
ax2.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax2.grid()
ax2.legend(loc="upper right")

ax3.plot(t,c.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(c.k,c.m,c.y0))
ax3.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax3.grid()
ax3.legend(loc="upper right")

ax4.plot(t,d.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(d.k,d.m,d.y0))
ax4.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax4.grid()
ax4.legend(loc="upper right")

ax5.plot(t,e.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(e.k,e.m,e.y0))
ax5.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax5.grid()
ax5.legend(loc="upper right")

ax6.plot(t,f.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(f.k,f.m,f.y0))
ax6.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax6.grid()
ax6.legend(loc="upper right")

#plt.savefig("oscilador.jpg")#Se comenta porque solo se necesita tomar la imagen para el trabajo

plt.show()

fig, ([ax1, ax2], [ax3, ax4], [ax5, ax6]) = plt.subplots(3, 2,figsize=(15, 15))
ax1.plot(a.movimiento_edo(t)[:,0],a.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(a.k,a.m,a.y0))
ax1.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax1.grid()
ax1.legend(loc="upper right")

ax2.plot(b.movimiento_edo(t)[:,0],b.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(b.k,b.m,b.y0))
ax2.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax2.grid()
ax2.legend(loc="upper right")

ax3.plot(c.movimiento_edo(t)[:,0],c.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(c.k,c.m,c.y0))
ax3.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax3.grid()
ax3.legend(loc="upper right")

ax4.plot(d.movimiento_edo(t)[:,0],d.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(d.k,d.m,d.y0))
ax4.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax4.grid()
ax4.legend(loc="upper right")

ax5.plot(e.movimiento_edo(t)[:,0],e.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(e.k,e.m,e.y0))
ax5.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax5.grid()
ax5.legend(loc="upper right")

ax6.plot(f.movimiento_edo(t)[:,0],f.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(f.k,f.m,f.y0))
ax6.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax6.grid()
ax6.legend(loc="upper right")

#plt.savefig("fases_oscilador.jpg")

plt.show()
##############################################################################

#Los mismos 6 osciladores anteriores con diferentes coeficientes de amortiguamiento
a=M.OsciladorAmortiguado(3,2,1,0.1)
b=M.OsciladorAmortiguado(3,5,1,0.5)
c=M.OsciladorAmortiguado(3,3,1,0.4)
d=M.OsciladorAmortiguado(3,2,2,0.1)
e=M.OsciladorAmortiguado(0.4,2,1,0.2)
f=M.OsciladorAmortiguado(1.4,5.2,-6,0.002)

fig, ([ax1, ax2], [ax3, ax4], [ax5, ax6]) = plt.subplots(3, 2,figsize=(15, 15))
ax1.plot(t,a.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(a.k,a.m,a.y0))
ax1.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax1.grid()
ax1.legend(loc="upper right")

ax2.plot(t,b.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(b.k,b.m,b.y0))
ax2.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax2.grid()
ax2.legend(loc="upper right")

ax3.plot(t,c.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(c.k,c.m,c.y0))
ax3.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax3.grid()
ax3.legend(loc="upper right")

ax4.plot(t,d.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(d.k,d.m,d.y0))
ax4.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax4.grid()
ax4.legend(loc="upper right")

ax5.plot(t,e.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(e.k,e.m,e.y0))
ax5.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax5.grid()
ax5.legend(loc="upper right")

ax6.plot(t,f.movimiento_edo(t)[:,0],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(f.k,f.m,f.y0))
ax6.set(title = "Evolución temporal de un oscilador armónico",xlabel = "Tiempo (s)", ylabel = "Posición (m)")
ax6.grid()
ax6.legend(loc="upper right")

#plt.savefig("oscilador_amortiguado.jpg")

plt.show()

fig, ([ax1, ax2], [ax3, ax4], [ax5, ax6]) = plt.subplots(3, 2,figsize=(15, 15))
ax1.plot(a.movimiento_edo(t)[:,0],a.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(a.k,a.m,a.y0))
ax1.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax1.grid()
ax1.legend(loc="upper right")

ax2.plot(b.movimiento_edo(t)[:,0],b.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(b.k,b.m,b.y0))
ax2.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax2.grid()
ax2.legend(loc="upper right")

ax3.plot(c.movimiento_edo(t)[:,0],c.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(c.k,c.m,c.y0))
ax3.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax3.grid()
ax3.legend(loc="upper right")

ax4.plot(d.movimiento_edo(t)[:,0],d.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(d.k,d.m,d.y0))
ax4.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax4.grid()
ax4.legend(loc="upper right")

ax5.plot(e.movimiento_edo(t)[:,0],e.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(e.k,e.m,e.y0))
ax5.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax5.grid()
ax5.legend(loc="upper right")

ax6.plot(f.movimiento_edo(t)[:,0],f.movimiento_edo(t)[:,1],
         label = "Resorete con k = %.2f N/m, masa m = %.2f y con condicion inicial %.2f m "%(f.k,f.m,f.y0))
ax6.set(title = "Espacio de fases de un oscilador armónico",ylabel = "Velocidad (m/s$)", xlabel = "Posición (m)")
ax6.grid()
ax6.legend(loc="upper right")

#plt.savefig("fases_oscilador_amortiguado.jpg")

plt.show()