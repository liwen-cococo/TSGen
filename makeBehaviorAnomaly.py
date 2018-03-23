from random import uniform, randint
from helper import loadJSON

class MakeBehaviorAnomaly(object, ):
    def __init__(self, data, cycle_len, config_path='./config/behaviorAnomaly.json'):
        self.data = data
        self.cycle_len = cycle_len
        self.config = loadJSON(config_path)
        self.tba = self.config['total_behavior_anomaly']
        self.lld = self.config['lower_limit_duration']
        self.uld = self.config['upper_limit_duration']
        
    def make_anomaly(self):
        anomaly = []
        total_len = len(self.data)
        cycles = total_len / self.cycle_len
        anomaly_num = min(cycles, self.tba+1)
        count = 0
        for i in xrange(1, cycles):
            if uniform(0, 1) >= (anomaly_num + 0.0) / (cycles + 0.0):
                continue
            count += 1
            if count >= anomaly_num:
                break
            begin = i * self.cycle_len
            end = (i+1) * self.cycle_len
            self.interval = self.data[begin:end]
            average = sum(self.interval) / (end-begin+0.0)
            standard_deviation = 0
            for inter in self.interval:
                standard_deviation += (inter - average) ** 2
            standard_deviation = (standard_deviation / (end - begin + 0.0)) ** 0.5
            max_value, min_value = max(self.interval), min(self.interval)
            max_index, min_index = self.interval.index(max_value), self.interval.index(min_value)
            
            duration = randint(self.lld, self.uld)
            if max_index < min_index:
                self.data[begin+max_index] = min_value
                ii = 0
                while max_index + ii < end and ii < duration:
                    self.data[begin+max_index+ii] = average + uniform(-standard_deviation, standard_deviation)
                    ii += 1
                anomaly += range(begin + max_index, begin + max_index+ii)
            
            else:
                self.data[begin+min_index] = max_value
                ii = 0
                while min_index + ii < end and ii < duration:
                    self.data[begin+min_index+ii] = average + uniform(-standard_deviation, standard_deviation)
                    ii += 1
                anomaly += range(begin + min_index, begin + min_index+ii)
        
        return self.data, anomaly
        