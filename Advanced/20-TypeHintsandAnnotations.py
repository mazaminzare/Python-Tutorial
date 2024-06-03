def greet(name: str) -> str:
    """
    Greets the person with the given name.

    :param name: The name of the person to greet.
    :return: A greeting string.
    """
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.

    :param a: The first integer to add.
    :param b: The second integer to add.
    :return: The sum of the two integers.
    """
    return a + b

# Example usage
print(greet("Amin"))  # Output: Hello, Alice
print(add(5, 10))      # Output: 15
