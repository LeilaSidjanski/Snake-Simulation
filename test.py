def sin_wave(t):
    global p
    p += 0.5
    for i in range(1, num_joints+1):
        #snake_x = np.arange(num_joints) * joint_length
        angles[i - 1] = 0.1 * (i * shift + p)
        if(i != num_joints):
            #save_x = snake_x[i]
            #save_y = snake_y[i]
            #snake_x[i - 1] = save_x * np.cos(angles[i - 1]) - save_y * np.sin(angles[i - 1])
            #snake_y[i - 1] = save_x * np.sin(angles[i - 1]) + save_y * np.cos(angles[i - 1])
        else:
            #snake_y[i - 1] = joint_length * np.sin(angles[i - 1])