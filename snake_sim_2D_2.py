import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time

num_joints = 4
joint_length = 0.4

snake_y = np.zeros(num_joints)
snake_x = np.arange(num_joints) * joint_length

freq = 1.0
amp = 0.5
offset = 0

identity = np.eye(12)

def gait_equation(t, i):
    #return offset + amp * np.sin(2 * np.pi * freq * t)
    if(i % 2 == 0):
        return 1 * np.sin((2 * np.pi * t/ (2) ) + 0 * (i + 0.5))
    else:
        return 1 * np.sin((2 * np.pi * t/ 2) + 0 * (i - 1))

k = 1
vector_g = np.zeros(num_joints)
second = np.zeros(num_joints)
G_matrix = np.zeros(num_joints ** 2).reshape((num_joints, num_joints))

def update(t):
    global snake_x, snake_y, vector_g, k, second
    k = k % num_joints
    for i in range(num_joints):
        second[i] = gait_equation(t - 0.1*i, i)

    vector_g = np.diag(np.outer(second, identity[k - 1]).T)
    print(vector_g)

    k = k + 1
    for j in range(1, num_joints): # column j of G
        #for i in range(1, num_joints): # servo i
            #snake_x[i] = snake_x[i-1] + np.cos(G_matrix[j][i]) * joint_length
            #snake_y[i] = snake_y[i-1] + np.sin(G_matrix[j][i]) * joint_length
        snake_y[j] = snake_y[j-1] + joint_length * vector_g[j]

    snake_x = np.arange(num_joints) * joint_length

angles = np.zeros(num_joints)
phases = np.array([0, 1, 2, 3, 4])
shift = (2 * np.pi) / num_joints
p = 0


def rotate(angle, position):
    return np.array([
    [np.cos(1)]
])

def sin_wave(t):
    global p
    p += 0.5
    for i in range(1, num_joints):
        snake_x = np.arange(num_joints) * joint_length
        angles[i - 1] = np.sin(0.5 * (i * shift + p))
        if(i != num_joints):
            snake_y[i - 1] = snake_y[i] + joint_length * angles[i - 1]
        else:
            snake_y[i - 1] = joint_length * angles[i - 1]


def angle():
    print(snake_x)
    print(snake_y)
    save_x = snake_x[1]
    save_y = snake_y[1]
    snake_x[1] = save_x * np.cos(np.pi / 2) - save_y * np.sin(np.pi / 2)
    snake_y[1] = save_x * np.sin(np.pi / 2) + save_y * np.cos(np.pi / 2)
    print(snake_x)
    print(snake_y)

#def update_snake_position(t):
 #   global snake_x, snake_y
  #  for i in range(1, num_joints):
   #     snake_y[i] = snake_y[i-1] + joint_length * gait_equation(t - i*0.1, i)
    #snake_x = np.arange(num_joints) * joint_length

def animate_snake(i):
    plt.clf()
    #update_snake_position(i/100.0)
    #update(i / 5.0)
    sin_wave(i / 100.0)
    plt.plot(snake_x, snake_y, 'ko-', lw=2)
    plt.xlim([-0.2, joint_length*num_joints+0.2])
    plt.ylim([-0.2, joint_length*num_joints+0.2])
    plt.title('Snake Motion')

fig = plt.figure(figsize=(7,7))
anim = FuncAnimation(fig, animate_snake, interval=50) # 10
plt.show()    