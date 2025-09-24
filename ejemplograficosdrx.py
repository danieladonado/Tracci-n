# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 08:12:47 2023

@author: frank
"""

#%% Importamos las librerías necesarias usando los alias apropiados 

import numpy as np # la necesitamos para operar con vectores y cargar el txt
import matplotlib.pyplot as plt # es necesario para graficar

#%% Cargamos los datos 

datos = np.loadtxt('DRX.txt',delimiter='\t') # recibe el nombre del archivo que debe 
#estar en la misma carpeta que el archivo del código, también recibe el tipo de separador 
# de datos, que en este caso es tabulación que se simboliza como \t


#%% Graficamos 

fig, ax = plt.subplots() # se crea una figura (fig) y unos ejes (ax) los cuale son objetos que podemos editar o guardar 

plt.plot(datos[:,0],datos[:,1],color=[22/255,162/255,64/255]) # En la primera columna (0) están los valores de angulo 
# en la segunda columna (1) están los datos correspondientes a la intensidad o los conteos
# el color se recibe en RGB normalizado en 255; pueden consultarse guías de código de color para elegir 

plt.savefig("DRX.jpg", dpi = 1200,bbox_inches = "tight")


# se puede limitar el tamaño de los ejes
plt.xlim(20,60)
plt.ylim(100,6000)
plt.grid() # se puede poner una cuadricula 


# se asigna el titulo a los ejes, se puede definir la fuente de letra, y poner expresiones 
# matemáticas como la letra griega tetha
# las expresiones matemáticas tiene su propia sintaxis, antes de las comillas se debe poner la 
#letra r y luego la expresión que requiera intepretación matemática debe estar entre $$.
ax.set_xlabel(r'2 $ \theta $',fontname = "Arial")

ax.set_ylabel("Counts (a.u.)", fontname="times new roman") # por ejemplo cambiamos la letra del 
#titulo del eje y por times new roman


# se puede definir la fuente de los números de los ejes (ticks)
plt.xticks(fontfamily = "century gothic") # por ejemplo con century gothic
plt.yticks(fontfamily = "calibri") #por ejemplo roboto


# se puede agregar texto o anotaciones sobre la figura definiendo la ubicación 
# y la fuente de letra, así como la orientación  


ax.text(40,3000,'anotación',rotation="vertical",fontfamily = "Arial")

ax.text(45,3000,'anotación',rotation="horizontal",fontfamily = "times new roman")

#La gráfica hecha se puede guardar con excelente calidad (resolución)

plt.savefig("DRX.jpg", dpi = 1200,bbox_inches = "tight")
