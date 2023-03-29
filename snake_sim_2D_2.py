import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

num_joints = 12
joint_length = 0.5

snake_x = np.zeros(num_joints) + 2
snake_y = np.arange(num_joints) * joint_length

freq = 1.0
amp = 0.5
offset = 0
wavelenght = 1

def gait_equation(t):
    #return offset + amp * np.sin(2 * np.pi * freq * t)
    return offset + ((3.5 * np.pi) / 40) * np.sin(4 * np.pi * t / 41)

def update_snake_position(t):
    global snake_x, snake_y
    for i in range(1, num_joints):
        snake_y[i] = snake_y[i-1] + joint_length * gait_equation(t - i*0.1)
    snake_x = np.arange(num_joints) * joint_length

def animate_snake(i):
    plt.clf()
    update_snake_position(i/100.0)
    plt.plot(snake_x, snake_y, 'ko-', lw=2)
    plt.xlim([-0.2, joint_length*num_joints+0.2])
    plt.ylim([-0.2, joint_length*num_joints+0.2])
    plt.title('Snake Motion')

fig = plt.figure(figsize=(7,7))
anim = FuncAnimation(fig, animate_snake, interval=10)
plt.show()    