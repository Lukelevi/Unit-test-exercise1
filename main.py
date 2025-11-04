def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    # TODO: Implement the logic
    nums = [1, 1]

    while len(nums) < n:
        nums.append(nums[-1] + nums[-2])
    return nums

def fibonacci(n):
    """Returns the nth number in the Fibonacci sequence."""
    # TODO: Implement the logic
    if n <= 0:
        return 1
    else:
        return n * fibonacci(n-1)

def fizzbuzz(n):
    """
    Returns a list for the FizzBuzz game up to n.
    - Multiples of 3 are "Fizz"
    - Multiples of 5 are "Buzz"
    - Multiples of both 3 and 5 are "FizzBuzz"
    """
    # TODO: Implement the logic
    fizz_game = []
    multiple_of_3 = [fizz_game.append("Fizz") for count in range(3, n, 3)]
    multiple_of_5 = [fizz_game.append("Buzz") for count in range(5, n, 5)]
    
    if multiple_of_3 and multiple_of_5:
        fizz_game.append("FizzBuzz")
    
    
    return fizz_game