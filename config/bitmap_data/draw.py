import matplotlib.pyplot as plt

def drawPng(data):
    plt.plot(range(len(data)), data)
    plt.show()

name = "ecg_normal.txt"
png = "ecg_normal.png"

with open(name, 'r') as f:
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(float(line[:9]))
plt.plot(range(len(data)), data)
plt.savefig(png)
plt.show()
