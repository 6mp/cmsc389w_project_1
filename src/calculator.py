"""Basic calculator operations."""

def add(a, b):
    """Add two numbers."""
    print(f"[DEBUG] Adding {a} + {b}")
    result = a + b
    print(f"[DEBUG] Result: {result}")
    return result

def subtract(a, b):
    """Subtract b from a."""
    print(f"[DEBUG] Subtracting {a} - {b}")
    result = a - b
    print(f"[DEBUG] Result: {result}")
    return result

def multiply(a, b):
    """Multiply two numbers."""
    print(f"[DEBUG] Multiplying {a} * {b}")
    result = a * b
    print(f"[DEBUG] Result: {result}")
    return result

def divide(a, b):
    """Divide a by b."""
    print(f"[DEBUG] Dividing {a} / {b}")
    if b == 0:
        print(f"[DEBUG] Error: Division by zero!")
        raise ValueError("Cannot divide by zero")
    result = a / b
    print(f"[DEBUG] Result: {result}")
    return result

def factorial(n):
    """Calculate factorial of n."""
    print(f"[DEBUG] Factorial of {n}")
    if n < 0:
        print(f"[DEBUG] Error: Negative number!")
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        print(f"[DEBUG] Base case: returning 1")
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"[DEBUG] Result: {result}")
    return result
