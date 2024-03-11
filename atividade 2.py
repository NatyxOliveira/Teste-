def fibonacci_sequence(n):
    a, b = 0, 1
    fibonacci_numbers = [a]

    while b <= n:
        fibonacci_numbers.append(b)
        a, b = b, a + b

    if n in fibonacci_numbers:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."


fibonacci_sequence(21)