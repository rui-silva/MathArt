import numpy as np

class Utils:
    @staticmethod
    def min_max_normalization(value, old_max, old_min, new_max, new_min):
        return ((1.0 * value - old_min) / (old_max - old_min)) * (new_max - new_min)

