#!/usr/bin/python
from helper import loadJSON
from helper import checkConfigShape, smoothPoints
import os
import numpy as np


class TSGen(object):
    def __init__(self, config_path='./config/shape.json'):
        self.config_data = loadJSON(config_path)
        self.tp = self.config_data['total_points']  # int
        self.tn = self.config_data['trends_num'] # int
        self.tr = self.config_data['trends']     # list
        self.nm = self.config_data['noise_mean']                # float
        self.nsd = self.config_data['noise_standard_deviation'] # float
        self.smoother = self.config_data['smoother']   # float
        self.base = checkConfigShape(self.config_data) # list(one cycle value)

    def shape_gen(self):
        points = []
        # repeat
        temp = []
        for t in self.tr:
            t_base = [t*k for k in self.base]
            # smooth_1
            if len(temp) > 0:
                a = temp[-1]
                b = t_base[0]
                add_n_points = int(len(self.base) * 0.1)
                temp += smoothPoints(a, b, add_n_points, self.smoother)
            temp = temp + t_base
        quotinent = self.tp / len(temp)
        remainder = self.tp % len(temp)
        # smooth_2
        if quotinent >= 1 and remainder > 0:
            a = temp[-1]
            b = temp[0]
            add_n_points = int(len(self.base) * 0.1)
            temp += smoothPoints(a, b, add_n_points, self.smoother)
        quotinent = self.tp / len(temp)
        remainder = self.tp % len(temp)
        
        self.cycle_len = len(self.base) + int(len(self.base) * 0.1)
        points = quotinent * temp + temp[:remainder]
        
        # add noise
        for i in xrange(self.tp):
            r = np.random.normal(self.nm, self.nsd)
            if r < self.nm - 3 * self.nsd or r > self.nm + 3 * self.nsd:
                r = np.random.uniform(self.nm - 3 * self.nsd, self.nm + 3 * self.nsd)
            points[i] += r
        
        return points, self.cycle_len
        