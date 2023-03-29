import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of segments and joints
n_segments = 12
n_joints = n_segments - 1

# Define the length of each segment
segment_length = 1.0

# Define the initial position of the snake
snake_position = np.zeros((n_segments, 2))

# Define the amplitude, speed, and wavelength of the traveling wave
amplitude = 0.5
speed = 10
wavelength = 10

# Define the phase of the traveling wave
phase = np.pi/2

# Define the time step and simulation time
dt = 0.1
t_max = 10.0

# Define the function to update the snake position
def update_snake_position(snake_position, theta, amplitude, speed, wavelength, t):
    for i in range(1, n_segments):
        x_prev, y_prev = snake_position[i-1]
        x_new = x_prev + segment_length * np.cos(theta[i-1])
        y_new = y_prev + segment_length * np.sin(theta[i-1])
        y_new += amplitude * np.sin(speed * np.deg2rad(i*360/n_joints) + wavelength * np.deg2rad(i*360/n_joints) * t + phase)
        snake_position[i] = np.array([x_new, y_new])
    return snake_position

# Define the function to animate the snake
def animate(i):
    global snake_position, theta, amplitude, speed, wavelength
    # Calculate the joint angles
    offset = 0
    max_angle_displacement = abs(offset) + abs(amplitude)
    while max_angle_displacement > 90:
        amplitude = abs(amplitude) - 1
        max_angle_displacement = abs(offset) + amplitude
    theta = [offset + amplitude * np.sin(speed * np.deg2rad(i*360/n_joints) + wavelength * np.deg2rad(i*360/n_joints) * i * dt) for i in range(n_joints)]
    
    # Update the snake position
    snake_position = update_snake_position(snake_position, theta, amplitude, speed, wavelength, i*dt)
    
    # Clear the previous plot
    plt.clf()
    
    # Plot the snake position
    plt.plot(snake_position[:,0], snake_position[:,1], 'b.-')
    plt.axis('equal')
    plt.title('Snake Simulation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

# Create the animation
ani = FuncAnimation(plt.gcf(), animate, frames=int(t_max/dt), interval=10)

# Show the animation
plt.show()
