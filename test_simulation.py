import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time

num_joints = 2
joint_length = 1

snake_y = np.zeros(num_joints) + 6
snake_x = (np.arange(num_joints) * joint_length) + 6

timeee = np.linspace(0, 2*np.pi, 500)
freq = 3.0
amp = 0.5
offset = 0

identity = np.eye(12)

def gait_equation(t, i):
    #return offset + amp * np.sin(2 * np.pi * freq * t)
    if(i % 2 == 0):
        return 1 * np.sin((2 * np.pi * t/ (num_joints) ) + np.pi * (i + 0.5))
    else:
        return 1 * np.sin((2 * np.pi * t/ num_joints) + np.pi * (i - 1))

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


def sin_wave(t):
    global p
    for i in range(1, num_joints):
        angles[i - 1] = gait_equation(t - 0.1 * i, i)
        if(i != num_joints):
            snake_y[i - 1] = snake_y[i] + joint_length * angles[i - 1]
        else:
            snake_y[i - 1] = joint_length * angles[i - 1]

decrease = False
def sin_wave_2(t):
    global p, decrease
    p += 0.05
    for i in range(1, num_joints+1):       

        angles[i - 1] = 0.2 * (i * shift + 0)
        if(i != num_joints):
            x = snake_x[i - 1]
            y = snake_y[i - 1]
            save_x = snake_x[i]
            save_y = snake_y[i]
            snake_x[i - 1] = save_x * np.cos(angles[i - 1]) - save_y * np.sin(angles[i - 1]) 
            + (x * (1 - np.cos(angles[i - 1])) + y * np.sin(angles[i - 1]))

            snake_y[i - 1] = save_x * np.sin(angles[i - 1]) + save_y * np.cos(angles[i - 1])
            (-x * np.sin(angles[i - 1]) + y * (1 - np.cos(angles[i - 1])))
        else:
            snake_y[i - 1] = joint_length * np.sin(angles[i - 1])


def rotation_not_centered(x_c, y_c, c_x, c_y, angle):
    rot = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    first = rot @ np.array([x_c, y_c])
    invert = np.eye(2) - rot
    second = invert @ np.array([c_x, c_y])
    return ((first + second)[0], (first + second)[1])

def sin_3(t):
    global p
    p += 0.05
    for j in range(len(timeee)):
        for i in range(num_joints):
            if(i == 0):
                d = 0
            else:
                av = freq*timeee[j] + i*2 * np.pi/(num_joints-1)
                av = 20 + ((160 - 20)/(180 - 0)) * (av - 20)
                snake_x[i], snake_y[i] = rotation_not_centered(snake_x[i], snake_y[i], snake_x[i - 1], snake_y[i - 1], av)

def angle():

    for i in range(len(timeee)):
        for j in range(num_joints):
            angle_1 = freq*timeee[i] + j*2 * np.pi/(num_joints-1)
            angle_2 = angle_1

            prev_x_0 = snake_x[0] 
            prev_y_0 = snake_y[0]

            prev_x_1 = snake_x[1] 
            prev_y_1 = snake_y[1]

            a_t = np.array([prev_x_0, prev_y_0])
            b_t = np.array([prev_x_1, prev_y_1])

            new_a = (a_t - b_t) * np.cos(angle_1) - (b_t - a_t) * np.sin(angle_2) + b_t
            new_b = (a_t - b_t) * np.sin(angle_1) + (b_t - a_t) * np.cos(angle_2) + a_t

            snake_x[0] = new_a[0]
            snake_y[0] = new_a[1]

            snake_x[1] = new_b[0]
            snake_y[1] = new_b[1]

def animate_snake(i):
    plt.clf()
    #update(i / 100.0)
    #sin_wave(i / 100.0)
    #sin_3(i / 100.0)
    plt.plot(snake_x, snake_y, 'ko-', lw=2)
    time.sleep(2)
    angle()
    plt.xlim([-0.2, joint_length*num_joints+10.2])
    plt.ylim([-0.2, joint_length*num_joints+10.2])
    plt.title('Snake Motion')

fig = plt.figure(figsize=(17,17))
anim = FuncAnimation(fig, animate_snake, interval=50) # 10
plt.show()