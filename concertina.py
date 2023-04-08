import matplotlib.pyplot as plt
import numpy as np


num_joints = 120
joint_length =1

snake_y = np.zeros(num_joints) + 6
snake_x = (np.arange(num_joints) * joint_length) + 6

wavelength = 5
amplitude = 3.5
offset = 0

t = np.linspace(0, 2*np.pi, 250)
freq = 3.0

def amplitude_factor(ampl, stop_ampl, steps):
    return np.power(ampl / stop_ampl, 1 / steps)  

fig, ax = plt.subplots()

ax.set_xlim(0, 100)
ax.set_ylim(-10, 10)

joints = ax.scatter(snake_x, snake_y)


joints.set_offsets(np.c_[snake_x, snake_y])
plt.draw()
plt.pause(2) 

for i in range(len(t)):
    l = 1
    for j in range(num_joints):
        snake_y[j] = offset + l * amplitude * np.sin(freq * t[i] + wavelength * j*2 * np.pi/(num_joints - 1))

        l /= amplitude_factor(amplitude, 0.5, num_joints - 1)

    joints.set_offsets(np.c_[snake_x, snake_y])
    plt.draw()
    plt.pause(0.001)    


for i in range(len(t)):
    l = 0.14
    for j in range(num_joints):
        snake_y[j] = offset + l * amplitude * np.sin(freq * t[i] + wavelength * j*2 * np.pi/(num_joints - 1))

        l *= amplitude_factor(amplitude, 0.5, num_joints - 1)    

    joints.set_offsets(np.c_[snake_x, snake_y])
    plt.draw()
    plt.pause(0.001)
    