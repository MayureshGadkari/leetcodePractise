def dailyTemperatures(T):
    n = len(T)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index

        stack.append(i)

    return result

# Example usage:
T = [73, 74, 75, 71, 69, 72, 76, 73]
result = dailyTemperatures(T)
print(result)