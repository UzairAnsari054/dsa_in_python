def generate_fibonacci(N):
    fibonacci_series = [0, 1]
    
    for i in range(2, N):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series

N = 10
result = generate_fibonacci(11)
print("First", N, "terms of fibonacci series:", result)