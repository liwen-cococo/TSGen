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
    print 'done 1'
    """
    mb = MakeBehaviorAnomaly(points, cycle_len)
    points_2, anomaly_2 = mb.make_anomaly()
    print 'done 2'
    """
    #points, anomaly = joinAnomaly(points_1, anomaly_1, points_2, anomaly_2)
    #print 'done all'
    name = 'd4-22yw-outliers'
    drawPng(points_1, anomaly_1, name+'.csv', name+'.json', name+'.png')
    