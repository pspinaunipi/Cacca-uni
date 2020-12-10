# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:47:17 2020


@author: mauri
"""

import unittest


from smartsquare.core import square

class TestCore (unittest.TestCase):
    ''' unittest for the core module '''
    def test_float (self):
        ''' ma che cazo ne so'''
        self.assertAlmostEqual (square(2.),4.)
if __name__ == '__main__':
    unittest.main()
    