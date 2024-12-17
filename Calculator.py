"""
This module provides basic arithmetic operations and a custom function
to determine the largest of three numbers.
"""

from typing import Union

# Define a reusable type alias for numbers
Number = Union[int, float]

def add(num1: Number, num2: Number) -> Number:
    """Returns the sum of two numbers."""
    return num1 + num2

def subtract(num1: Number, num2: Number) -> Number:
    """Returns the difference between two numbers."""
    return num1 - num2

def multiply(num1: Number, num2: Number) -> Number:
    """Returns the product of two numbers."""
    return num1 * num2

def divide(num1: Number, num2: Number) -> Number:
    """
    Returns the division of two numbers.
    
    Args:
        num1 (Number): The numerator.
        num2 (Number): The denominator.
    
    Raises:
        ValueError: If the denominator is zero.
    
    Returns:
        Number: The result of the division.
    """
    if num2 == 0:
        raise ValueError("Division by zero is not allowed.")
    return num1 / num2

def find_largest(num1: Number, num2: Number, num3: Number) -> Number:
    """
    Returns the largest of three numbers.
    
    Args:
        num1 (Number): The first number.
        num2 (Number): The second number.
        num3 (Number): The third number.
    
    Returns:
        Number: The largest of the three numbers.
    """
    return max(num1, num2, num3)

# Example usage (this could be separated into a test file):
if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    try:
        print("Division:", divide(5, 0))
    except ValueError as e:
        print("Error in division:", e)
    print("Largest:", find_largest(5, 10, 3))
