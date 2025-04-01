def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b
  
def intergerDivide(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    print("CN HW2")