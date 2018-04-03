import matplotlib.pyplot as plt

def drawPng(data):
    plt.plot(range(len(data)), data)
    plt.show()

name = "base.txt"
png = "base.png"

with open(name, 'r') as f:
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(float(line[:9]))
plt.plot(range(len(data)), data)
plt.savefig(png)
plt.show()
