import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the double pendulum system of ODEs
def double_pendulum(t, y, l1, l2, m1, m2, g):
    theta1, omega1, theta2, omega2 = y

    dydt = [
        omega1,
        (-g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2)
         - 2 * np.sin(theta1 - theta2) * m2 * (omega2**2 * l2 + omega1**2 * l1 * np.cos(theta1 - theta2))) /
        (l1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))),
        omega2,
        (2 * np.sin(theta1 - theta2) * (omega1**2 * l1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1)
         + omega2**2 * l2 * m2 * np.cos(theta1 - theta2))) /
        (l2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2)))
    ]

    return dydt

# Set up initial conditions
initial_conditions = [np.pi/2, 0, np.pi, 0]  # [theta1, omega1, theta2, omega2]

# Set up parameters
length1 = 14.0
length2 = 16.0
mass1 = 6.0
mass2 = 1.0
gravity = 9.8

# Set up time span
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Numerically solve the ODEs
solution = solve_ivp(double_pendulum, t_span, initial_conditions, args=(length1, length2, mass1, mass2, gravity),
                     t_eval=t_eval, method='RK45')

# Extract the solution
theta1, omega1, theta2, omega2 = solution.y

# Plot the double pendulum motion
plt.figure(figsize=(8, 6))
plt.plot(t_eval, theta1, label='Theta1')
plt.plot(t_eval, theta2, label='Theta2')
plt.title('Double Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.legend()
plt.show()
