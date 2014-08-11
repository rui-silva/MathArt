from ..ModSpring.mod_spring import ModSpring

import numpy as np
import math

from unittest import TestCase
from nose.tools import assert_equal
from nose.tools import assert_true

class ModSpringTest(TestCase):
    def test_number_points(self):
        height = 2
        height_spacing = 1
        radius = 2
        precision = 0.1
        ms = ModSpring(height=2, height_spacing=1, radius=2, precision=0.1)
        res = ms.compute()

        number_rings = 1.0 * height / height_spacing
        number_points = radius * number_rings
        number_points = number_points / precision + 1
        
        assert_equal(number_points, res.shape[0])

    def test_max_height(self):
        ms5 = ModSpring(height=5)
        ms10 = ModSpring(height=10)

        res5 = ms5.compute()
        res10 = ms10.compute()
        
        assert_equal(res5[-1, 2], 5)
        assert_equal(res10[-1, 2], 10)

    def test_radius(self):
        radius = 4
        ms2 = ModSpring(height=2, height_spacing=1, radius=radius, precision=1)
        res = ms2.compute()

        assert_equal(res[0, 0], radius)
        assert_true(np.allclose(res[0, 1], 0))

        assert_true(np.allclose(res[1, 0], 0))
        assert_equal(res[1, 1], radius)

        assert_equal(res[2, 0], -radius)
        assert_true(np.allclose(res[2, 1], 0))
        
        assert_true(np.allclose(res[3, 0], 0))
        assert_equal(res[3, 1], -radius)
