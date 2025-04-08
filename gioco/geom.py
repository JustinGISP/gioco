'''
geom

This module contains functions for geometry

'''
import math

# Define common errors
missingArgError = "Missing a required argument"


def circle_area(radius):
    """Calculate the area of a circle given the radius."""
    # Check if the argument is missing
    if radius is None:
        raise TypeError(f"{missingArgError}: radius")
    # Check if the argument is a number
    if not isinstance(radius, (int, float)) or isinstance(radius, bool):
        raise TypeError("Radius must be a number")
    # Check if the argument is a greater than zero
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")
    
    return math.pi * (radius ** 2)


def circumference(radius):
    """Calculate the circumference of a circle given the radius."""
     # Check if the argument is missing
    if radius is None:
        raise TypeError(f"{missingArgError}: radius")
    # Check if the argument is a number
    if not isinstance(radius, (int, float)) or isinstance(radius, bool):
        raise TypeError("Radius must be a number")
    # Check if the argument is greater than zero
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")
    
    return 2 * math.pi * radius


def cube_vol(side):
    """Calculate the volume of a cube given the length of a side."""
     # Check if the argument is missing
    if side is None:
        raise TypeError(f"{missingArgError}: side")
    # Check if the argument is a number
    if not isinstance(side, (int, float)) or isinstance(side, bool):
        raise TypeError("Side length must be a number")
    # Check if the argument is greater than zero
    if side <= 0:
        raise ValueError("Side length must be greater than zero.")
    
    return side**3 


def rect_area(b,h):
    """Calculate the area of a rectangle given the base and height."""
    # Check if any arguments are missing
    if b is None or h is None:
        raise TypeError("Missing required arguments: 'b' and 'h'")
    # Check if both arguments are numbers
    if (not isinstance(b, (int, float)) or isinstance(b, bool)) or (not isinstance(h, (int, float)) or isinstance(h, bool)):
        raise TypeError("Both 'b' and 'h' must be numbers")
    # Check if both arguments are greater than zero
    if b <= 0 or h <= 0:
        raise ValueError("Both 'b' and 'h' must be greater than zero")

    return b*h


def sphere_area(radius):
    """Calculate the circumference of a circle given the radius."""
     # Check if the argument is missing
    if radius is None:
        raise TypeError(f"{missingArgError}: radius")
    # Check if the argument is a number
    if not isinstance(radius, (int, float)) or isinstance(radius, bool):
        raise TypeError("Radius must be a number")
    # Check if the argument is greater than zero
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")
    
    return 4 * math.pi * (radius**2)


def sphere_vol(radius):
    """Calculate the circumference of a circle given the radius."""
     # Check if the argument is missing
    if radius is None:
        raise TypeError(f"{missingArgError}: radius")
    # Check if the argument is a number
    if not isinstance(radius, (int, float)) or isinstance(radius, bool):
        raise TypeError("Radius must be a number")
    # Check if the argument is greater than zero
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")
    
    return (4/3) * math.pi * (radius**3)


def tri_area(b,h):
    """Calculate the area of a triangle given the base and height."""
    # Check if any arguments are missing
    if b is None or h is None:
        raise TypeError("tri_area() missing required arguments: 'b' and 'h'")
    # Check if both arguments are numbers
    if (not isinstance(b, (int, float)) or isinstance(b, bool)) or (not isinstance(h, (int, float)) or isinstance(h, bool)):
        raise TypeError("Both 'b' and 'h' must be numbers")
    # Check if both arguments are greater than zero
    if b <= 0 or h <= 0:
        raise ValueError("Both 'b' and 'h' must be greater than zero")

    return (b*h)/2