#Gustavo Adolfo Cruz 22779
#Joaquín Campos 22155
#Pedro Pablo Guzmán 22111

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as smp
import scipy as sp
from scipy.integrate import quad
import turtle
import math
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_interactions import ioff, panhandler, zoom_factory


turtle.speed(0)
turtle.bgcolor("white")


l1 = 100  # Longitud del primer péndulo
l2 = 100  # Longitud del segundo péndulo
m1 = 1    # Masa del primer objeto
m2 = 1    # Masa del segundo objeto
g = 9.8   # Aceleración debido a la gravedad

theta1 = math.pi / 2  # Ángulo inicial del primer péndulo (90 grados)
theta2 = math.pi / 2  # Ángulo inicial del segundo péndulo (90 grados)
omega1 = 0           # Velocidad angular inicial del primer péndulo
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


# Función para dibujar los péndulos
def draw_pendulum(x1, y1, x2, y2):
    turtle.clear()
    turtle.pendown()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.pensize(1)
    turtle.goto(x1, y1)
    turtle.pensize(5)
    turtle.dot("red")
    turtle.pensize(1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.pensize(5)
    turtle.dot("blue")
    turtle.penup()


# Bucle principal
while True:
    x1 = l1 * math.sin(theta1)
    y1 = -l1 * math.cos(theta1)

    x2 = x1 + l2 * math.sin(theta2)
    y2 = y1 - l2 * math.cos(theta2)

    draw_pendulum(x1, y1, x2, y2)
    update_position()

turtle.done()