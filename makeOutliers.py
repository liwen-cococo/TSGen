from helper import loadJSON, checkConfigOutliers
from random import randint, random, uniform


class MakeOutliers(object):
    def __init__(self, data, config_path='./config/outliers.json'):
        self.shape_data = data
        self.config = loadJSON(config_path)
        self.to = self.config['total_outliers']
        self.lld = self.config['lower_limit_duration']
        self.uld = self.config['upper_limit_duration']
        self.sll = self.config['spike_lower_limit']
        self.sul = self.config['spike_upper_limit']
        self.pll = self.config['plunge_lower_limit']
        self.pul = self.config['plunge_upper_limit']
        checkConfigOutliers(self.config)
        self.anomaly = []

    def make_outliers(self):
        length = len(self.shape_data)
        for i in xrange(self.to):
            outlier_begin = randint(0, length-1)       # begin index
            duration = randint(self.lld, self.uld)
            outlier_end = outlier_begin + duration - 1 # end index
            if outlier_begin + duration - 1 >= length - 1:
                outlier_end = length - 1
            s_or_p = random()
            if s_or_p > 0.5:
                for ii in xrange(outlier_begin, outlier_end+1):
                    temp = uniform(self.sll, self.sul)
                    self.shape_data[ii] *= uniform(self.sll, temp)
            else:
                for ii in xrange(outlier_begin, outlier_end+1):
                    temp = uniform(self.pll, self.pul)
                    self.shape_data[ii] *= uniform(self.pll, temp)
            
            self.anomaly += range(outlier_begin, outlier_end+1)
        
        return self.shape_data, self.anomaly
        