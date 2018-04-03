try:
    import simplejson as json
except ImportError:
    import json
import matplotlib.pyplot as plt
import random
import csv


def loadJSON(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def checkConfigShape(data):
    # TO DO
    base = []
    with open(data['one_cycle_values'], 'r') as f:
        text = f.readlines()
        for t in text:
            base.append(float(t[:-1]))
    return base

def checkConfigOutliers(data):
    # TO DO
    pass

def smoothPoints(a, b, n, smoother):
    """ return a list of n elements """
    jump = (b-a+0.0) / (n+1.0)
    results = []
    for i in xrange(n):
        results.append(a+(i+1)*jump+random.uniform(-smoother*jump, smoother*jump))
    return results

def joinAnomaly(points_1, anomaly_1, points_2, anomaly_2):
    points = []
    anomaly = []
    leng = len(points_1)
    for i in xrange(leng):
        if i in anomaly_2:
            points.append(points_2[i])
            anomaly.append(i)
        elif i in anomaly_1:
            points.append(points_1[i])
            anomaly.append(i)
        else:
            points.append(points_1[i])
    return points, anomaly

def drawPng(data, anomaly, csv_filename, ano_filename, png_filename):
    lines = [['timestamp', 'value']]
    for i in xrange(len(data)):
        s = [i, data[i]]
        lines.append(s)
    with open(csv_filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(lines) 
    with open(ano_filename, 'w') as f:
        json.dump({csv_filename: anomaly}, f, indent=4)
        
    plt.plot(range(len(data)), data)
    y_ab = [data[i] for i in anomaly]
    plt.scatter(anomaly, y_ab, marker='o', color='r', s=20)
    plt.savefig(png_filename)
    plt.show()
