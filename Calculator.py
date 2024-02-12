def add(x, y):
    """Addition operation."""
    return x + y

def subtract(x, y):
    """Subtraction operation."""
    return x - y

def multiply(x, y):
    """Multiplication operation."""
    return x * y

def divide(x, y):
    """Division operation."""
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Example usage
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operator"

print(f"Result: {result}")
