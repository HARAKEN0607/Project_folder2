import os
import matplotlib.pyplot as plt
import numpy as np

# set parameter
I = 100
k = 0.93
T1 = [10, 1, 0.25]
T2 = [350, 200, 100]
datasize = 1000
name_title = ['10/350 μs', '1/200 μs', '0.25/100 μs']
file_name = ['10-350', '1-200', '0.25-100']


def cal_line(I, k, T1, T2, t):
    h1 = I / k
    h2 = (t / T1) ** 10 / (1 + (t / T1) ** 10)
    h3 = np.exp(-t / T2)

    i = h1 * h2 * h3
    return i


# Create or check data folders
# figurepath = '/home/pi/Project_folder/' + 'png/'
# csvpath = '/home/pi/Project_folder/' + 'csv_original/'

# figurepath = 'D:/Project_folder/'+'png/'
# csvpath = 'D:/Project_folder/'+'csv_original/'

figurepath = os.getcwd() + '/png/'
csvpath = os.getcwd() + '/csv_original/'

if not os.path.exists(figurepath):
    os.mkdir(figurepath)

if not os.path.exists(csvpath):
    os.mkdir(csvpath)

for n in range(0, 3, 1):
    # Create time axis
    t = np.linspace(0, T2[n], datasize)

    # Calculate heidler
    value = cal_line(I, k, T1[n], T2[n], t)

    # Set figure
    fig = plt.figure(figsize=(7, 5), dpi=300)
    ax = fig.add_subplot()

    ax.grid(color='k', alpha=0.5)

    ax.set_xlabel('time (μs)', fontsize=15)
    ax.set_ylabel('Current (kA)', fontsize=15)
    ax.set_title(name_title[n], fontsize=20)

    ax.set_xlim([0, T2[n]])
    ax.set_ylim([0, 120])

    ax.plot(t, value)
    # plt.show()
    name = file_name[n] + '_T2(' + str(T2[n]) + ')_N' + str(datasize)

    fig.savefig(figurepath + name + '.png', dpi=300)

    # Save data to csv
    data = np.stack([t.T, value.T], 1)
    np.savetxt(csvpath + name + '.csv', data)
