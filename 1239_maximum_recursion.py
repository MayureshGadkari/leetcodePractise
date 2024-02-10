# def maxLength(arr):
#     def is_unique(combination):
#         return len(combination) == len(set(combination))
#
#     def backtrack(start, current):
#         nonlocal max_length
#         if is_unique(current):
#             max_length = max(max_length, len(current))
#         else:
#             return
#
#         for i in range(start, len(arr)):
#             backtrack(i + 1, current + arr[i])
#
#     max_length = 0
#     backtrack(0, "")
#     return max_length
#
# # Example usage
# arr = ["un", "iq", "ue"]
# result = maxLength(arr)
# print(result)

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Example: Generate the first 10 Fibonacci numbers
result = fibonacci(10)
print(result)