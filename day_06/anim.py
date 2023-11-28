import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# x, y, vx, vy
# dots = np.array([
#     [0.5, 0.3, 0.02, 0.07],
#     [0.1, 0.6, -0.05, -0.1],
# ])

N = 50000
dots = np.random.rand(N,4)

pos = dots[:, 0:2]
vel = dots[:, 2:4]
vel -= 0.5
vel *= 0.2


xs = dots[:, 0]
ys = dots[:, 1]
vxs = dots[:, 2]
vys = dots[:, 3]


fig, ax = plt.subplots()
viz, = ax.plot(xs, ys, ',')

ax.set_xlim(0,1)
ax.set_ylim(0,1)

def timestep(dt):
    pos[:] += vel[:] * dt

    vxs[ (xs < 0) | (xs > 1) ] *= -1
    vys[ (ys < 0) | (ys > 1) ] *= -1
    
    vys[:] -= 0.02 * dt



def update_frame(number):
    print(number)
    timestep(0.1)
    viz.set_data(xs, ys)


anim = FuncAnimation(
    fig, 
    update_frame,
    interval=20,
)

plt.show()
