import numpy as np
import math

from ..utils import Utils

class ModSpring:
    """Implementation of a spring shape, using simple math concepts.

    Creates a spring shape, with several parameters, using the simple concept
    of modular arithmetics.
    """

    def __init__(self, height=10, height_spacing=1, radius=7, precision=0.1):
        """Constructor.
        Args:
          height (float): Height of the spring (unitless).
          height_spacing (float): Spacing between the rings of the spring (unitless).
          radius (float): Radius of the rings of the spring (unitless).
          precision (float): The step between points. The bigger, the better the results.
        Returns:
          Instance of ModSpring
        """
        assert height > precision
        assert height > 0
        assert height >= height_spacing
        assert height_spacing > 0
        assert height_spacing >= precision
        assert radius > precision
        assert radius > 0
        assert precision > 0
        
        self.EPSILON = precision / 100

        self.height = height
        self.height_spacing = height_spacing
        self.radius = radius
        self.precision = precision
    
    def compute(self):
        """Computes the spring shape.
        Args:
        Returns:
          A 3 columns np.ndarray (x, y, z)
        """
        number_rings = 1.0 * self.height / self.height_spacing
        max_number = self.radius * number_rings

        # compute x and y
        points = np.arange(0, max_number + self.EPSILON, self.precision)
        points = points.reshape(-1, 1)
        x = y = Utils.min_max_normalization(points % self.radius, 
                                            self.radius, 0, 
                                            2 * math.pi, 0)
        x = self.radius * np.cos(x)
        y = self.radius * np.sin(y)

        # compute z
        number_points = points.shape[0]
        delta_z = 1.0 * self.height / (number_points - 1)
        z = delta_z * np.arange(0, number_points, 1)
        z = z.reshape(-1, 1)

        return np.hstack((x, y, z))



