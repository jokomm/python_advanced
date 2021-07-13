"""Calculating the Circumference and Area of a Circle"""

import math


def calculate_circle(R):
    if R >= 0:
        C = round(2 * math.pi * R, 2)
        S = round(math.pi * R * R, 2)
        return C, S
