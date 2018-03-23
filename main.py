#!/usr/bin/python
from tsGen import TSGen
from makeOutliers import MakeOutliers
from makeBehaviorAnomaly import MakeBehaviorAnomaly
from helper import drawPng, joinAnomaly


if __name__ == '__main__':
    sg = TSGen()
    points, cycle_len = sg.shape_gen()
    mo = MakeOutliers(points)
    points_1, anomaly_1 = mo.make_outliers()
    mb = MakeBehaviorAnomaly(points, cycle_len)
    points_2, anomaly_2 = mb.make_anomaly()
    points, anomaly = joinAnomaly(points_1, anomaly_1, points_2, anomaly_2)
    
    drawPng(points, anomaly, 'data.csv', 'anomaly.json', 'data.png')
    