# student solution
import math
import numpy as np
def largest_triangle_proof(n, radius):
    """
    Prove the pattern of largest area of a triangle that can be 
    inscribed inside a give circle. 
    
    This function returns the height of largest area of a triangle 
    that can be inscribed inside a circle with the given radius, 
    and base of the triangle is the diameter of the circle

    Args:
      radius: radius of the circle
      n: gradient

    Returns:
      height of the largest triangle
    """
    # set the centre of the circle to (0,0)
    origin_x = 0.0
    origin_y = 0.0

    radian_t = np.linspace(0, np.pi, n+1)
    sin_t = np.sin(radian_t)
    h = radius * sin_t
    triangle_area = radius * h
    positions = np.array([radius * np.cos(radian_t), h]).T
    largest_area_idx = np.argmax(triangle_area)
    return positions[largest_area_idx, 1]



def largest_triangle_area(n, radius, h=0.0):
    """
    Returns the largest area of a triangle that can be inscribed inside a
    circle with the given radius.

    Args:
      radius: radius of the circle
      h: the starting height of triangle found after the proof of max area based on diameter as the base of triangle
      n: gradient

    Returns:
      Area of the largest inscribed triangle
    """
    h = largest_triangle_proof(n, radius)

    d = np.linspace(0, radius, n+1)
    base_length = 2 * np.sqrt(radius**2 - d**2)
    area = 0.5 * base_length * (d + h)
    largest_A = np.max(area)

    return largest_A