import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号


# 更新函数
def update_plus_case(frame):
    global x, y, x_0, y_0
    t = frame * dt
    x = x_0 + 0.5 * h_0 * np.sin(t) * x_0
    y = y_0 - 0.5 * h_0 * np.sin(t) * y_0
    # 更新散点图
    scat_plus.set_offsets(np.c_[x, y])
    return scat_plus,

def update_cross_case(frame):
    global x, y, x_0, y_0
    t = frame * dt
    x = x_0 + 0.5 * h_0 * np.sin(t) * y_0
    y = y_0 + 0.5 * h_0 * np.sin(t) * x_0
    # 更新散点图
    scat_cross.set_offsets(np.c_[x, y])
    return scat_cross,


# 初始设置
h_0 = 0.5
particle_num = 50
time_band = (0, 10)  # 时间范围
fps = 30  # 帧率
frames_num = int((time_band[1] - time_band[0]) * fps)  # 总帧数
dt = (time_band[1] - time_band[0])/frames_num

r = 1.0
theta = np.linspace(0, 2 * np.pi, particle_num, endpoint=False)
x_0 = r * np.cos(theta)
y_0 = r * np.sin(theta)
x = x_0
y = y_0 


# 创建画布
fig_plus, pluscase = plt.subplots()
pluscase.set_xlim(-2, 2)
pluscase.set_ylim(-2, 2)
pluscase.set_aspect('equal')
pluscase.set_title("＋模引力波示意图")
scat_plus = pluscase.scatter(x_0, y_0, s=10)

fig_cross, crosscase = plt.subplots()
crosscase.set_xlim(-2, 2)
crosscase.set_ylim(-2, 2)
crosscase.set_aspect('equal')
crosscase.set_title("×模引力波示意图")
scat_cross = crosscase.scatter(x_0, y_0, s=10)

# 生成动画
gif_plus = FuncAnimation(fig_plus, update_plus_case, frames=frames_num, interval=1000/fps, blit=True)
gif_plus.save('pluscase.gif', writer='pillow', fps = 30)

gif_cross = FuncAnimation(fig_cross, update_cross_case, frames=frames_num, interval=1000/fps, blit=True)
gif_cross.save('crosscase.gif', writer='pillow', fps = 30)
