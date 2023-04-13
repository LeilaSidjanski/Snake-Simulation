import numpy as np
import matplotlib.pyplot as plt

num_joints = 12
amplitude = 1.5
wavelength = 3
offset = 0

x = np.zeros(num_joints)
y = np.linspace(0, -amplitude*(num_joints-1), num=num_joints)

t = np.linspace(0, 2*np.pi, 500)
freq = 3.0

# Create the figure and axes
fig, ax = plt.subplots()

# Set the limits of the plot
ax.set_xlim(-8, 8)
ax.set_ylim(-amplitude*(num_joints-1)-amplitude*0.5, amplitude*0.5)

# Initialize the scatter plot for the joints
joints = ax.scatter(x, y)

for i in range(len(t)):
    for j in range(num_joints):
        x[j] = offset + amplitude * \
            np.sin(freq*t[i] + wavelength * j*2 * np.pi/(num_joints-1))

    joints.set_offsets(np.c_[x, y])
    plt.draw()
    plt.pause(0.001)
