import matplotlib.pyplot as plt
import numpy as np
import os

# set parameter(10/350)
I = 100
k = 0.93
T1 = [10, 1, 0.25]
T2 = [350, 200, 100]
t = np.linspace(0, 50, 100000)

def cal_line(t, k, I, T1, T2):
    h1 = I / k
    h2 = (t / T1) ** 10 / (1 + (t / T1) ** 10)
    h3 = np.exp(-t / T2)

    i = h1 * h2 * h3
    return i


# Create or check data folders
figurepath = '/home/pi/Project_folder/' + 'png/'
# figurepath = 'D:/Project_folder/'+'png/'

if not os.path.exists(figurepath):
    os.mkdir(figurepath)

csvpath = '/home/pi/Project_folder/' + 'csv_original/'
# csvpath = 'D:/Project_folder/'+'csv_original/'

if not os.path.exists(csvpath):
    os.mkdir(csvpath)

fig = plt.figure(figsize=(7, 5), dpi=300)
ax = fig.add_subplot()

ax.grid(color='k', alpha=0.5)

ax.set_xlabel('time (μs)', fontsize=15)
ax.set_ylabel('Current(kA)', fontsize=15)
ax.set_title('Thunder Waveform4 renewal', fontsize=20)

ax.set_xlim([0, 50])
ax.set_ylim([0, 120])

line_color = ['k', 'b', 'r']

for n in range(0, 3, 1):
    value = cal_line(t, k, I, T1[n], T2[n])

    ax.plot(t, value, color=line_color[n])

# set label
name_title = ['10/350 μs', '1/200 μs', '0.25/100 μs']
ax.legend(name_title, loc='lower right', framealpha=1)

filename = 'Heidler_3patterns_Tmax(50)'

fig.savefig(figurepath + filename + '.png', dpi=300)

# save CSV file
t2 = t.T
i = value.T

file = np.stack([t2, i], 1)
np.savetxt(csvpath + filename + '.csv', file)
