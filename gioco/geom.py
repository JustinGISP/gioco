'''
geom

This module contains functions for geometry

'''
import math

# Define common errors
missingArgError = "Missing a required argument"

def circle_area(radius):
    """Calculate the area of a circle given the radius."""
    if radius is None:
        raise TypeError(f"{missingArgError}: radius")
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius <= 0:
        raise ValueError("Radius must be a positive number")
    
    return math.pi * (radius ** 2)

def circumference(radius):
    """Calculate the circumference of a circle given the radius."""
    if radius is None:
        raise TypeError(f"{missingArgError}: radius")
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius <= 0:
        raise ValueError("Radius must be a positive number")
    
    return 2 * math.pi * radius