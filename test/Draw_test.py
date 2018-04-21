import numpy as np

import time
import unittest

import sys
sys.path.append('..')
from util.draw import DrawFigure


class DrawTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_draw(self):
        x = np.linspace(0,3.0)  
        d = DrawFigure(dimension = 2)

        for i in range(5000):
            x +=i
            y = np.square(x)
            d.ax.plot(x,y)
            d.plt.pause(0.01)
           
            


def main():
    unittest.main()

if __name__ == '__main__':
    main()