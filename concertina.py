import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time

num_joints = 120
joint_length =1

snake_y = np.zeros(num_joints) + 6
snake_x = (np.arange(num_joints) * joint_length) + 6


wavelength = 5
amplitude = 3.5
offset = 0


def animate_snake(i):
    plt.clf()
    plt.plot(snake_x, snake_y, 'ko-', lw=2)
    plt.xlim([-0.2, joint_length*num_joints+10.2])
    plt.ylim([-0.2, joint_length*num_joints+10.2])
    plt.title('Snake Motion')

    sine_wave_simple()

def wavelength_factor(mult_wave_length, final_wave_length, steps):
    return np.power(steps / (mult_wave_length * final_wave_length), 1 / steps)

def amplitude_factor(ampl, stop_ampl, steps):
    return np.power(ampl / stop_ampl, 1 / steps)


def sine_wave_simple():
    global snake_x, snake_y

    k = 1.2
    l = 1
    for j in range(1, num_joints):
        snake_y[j] = snake_y[j - 1] + offset + l * amplitude * np.sin(k * wavelength * j*2 * np.pi/(num_joints - 1))
        k /= wavelength_factor(wavelength, 1.1, num_joints - 1)
        l /= amplitude_factor(amplitude, 0.5, num_joints - 1)  


    for j in range(1, num_joints):
        snake_y[j] = snake_y[j - 1] + offset + l * amplitude * np.sin(k * wavelength * j*2 * np.pi/(num_joints - 1))
        k *= wavelength_factor(wavelength, 1.1, num_joints - 1)
        l *= amplitude_factor(amplitude, 0.5, num_joints - 1)                  


fig = plt.figure(figsize=(17,17))
anim = FuncAnimation(fig, animate_snake, interval=50) # 10
plt.show()