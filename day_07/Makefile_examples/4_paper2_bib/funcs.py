#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def get_random_numbers(num_of_points, scale):
    """Generate a 1D array of random numbers between 0 and "scales"

    Parameters
    ----------
    num_of_points : int
        Length of the random number array
    scale : float
        Maximum amplitude of the random numbers.

    Returns
    -------
    numpy.array
        1D array of uniform random numbers
    """
    return scale * np.random.random(num_of_points)
