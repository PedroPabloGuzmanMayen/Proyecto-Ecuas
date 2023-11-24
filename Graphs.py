import numpy as np
import matplotlib.pyplot as plt
import turtle
import math


l1 = 16  # Longitud del primer péndulo
l2 = 16  # Longitud del segundo péndulo
m1 = 3   # Masa del primer objeto
m2 = 1    # Masa del segundo objeto
g = 9.8   # Aceleración debido a la gravedad

theta1 = 1  # Ángulo inicial del primer péndulo (90 grados)
theta2 = -1  # Ángulo inicial del segundo péndulo (90 grados)
omega1 = 0          # Velocidad angular inicial del primer péndulo
omega2 = 0           # Velocidad angular inicial del segundo péndulo

# Función para actualizar las posiciones de los péndulos
def update_position():
    global theta1, theta2, omega1, omega2
    dt = 0.05  # Incremento de tiempo

    # Fórmulas de movimiento angular
    alpha1 = (-g * (2 * m1 + m2) * math.sin(theta1) - m2 * g * math.sin(theta1 - 2 * theta2) -
              2 * m2 * math.sin(theta1 - theta2) * (omega2 ** 2 * l2 + omega1 ** 2 * l1 * math.cos(theta1 - theta2))) / \
             (l1 * (2 * m1 + m2 - m2 * math.cos(2 * theta1 - 2 * theta2)))

    alpha2 = (2 * math.sin(theta1 - theta2) * (omega1 ** 2 * l1 * (m1 + m2) + g * (m1 + m2) * math.cos(theta1) +
                                               omega2 ** 2 * l2 * m2 * math.cos(theta1 - theta2))) / \
             (l2 * (2 * m1 + m2 - m2 * math.cos(2 * theta1 - 2 * theta2)))

    # Actualizar velocidades angulares
    omega1 += alpha1 * dt
    omega2 += alpha2 * dt

    # Actualizar ángulos
    theta1 += omega1 * dt
    theta2 += omega2 * dt



#Listas para almacenar los valores de theta1 y theta2
theta1_values = []
theta2_values = []

#Bucle principal
for _ in range(500):  
    x1 = l1 * math.sin(theta1) #Obtener coordenadas x e y de los péndulos
    y1 = -l1 * math.cos(theta1)

    x2 = x1 + l2 * math.sin(theta2)
    y2 = y1 - l2 * math.cos(theta2)

    # Guardar los desplazamientos angulares actuales
    theta1_values.append(theta1)
    theta2_values.append(theta2)

    update_position() #Actualizar las posiciones de los péndulos

# Graficar los desplazamientos angulares a través del tiempo
time_values = np.arange(0, len(theta1_values) * 0.05, 0.05)  #Obtener los valores del tiempo

plt.plot(time_values, theta1_values, label='Theta1')
plt.plot(time_values, theta2_values, label='Theta2')
plt.title('Angular Displacement of Double Pendulum')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (radians)')
plt.legend()
plt.show()