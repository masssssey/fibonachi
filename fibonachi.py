fib = [0, 1]
for i in range(2, 101):
    fib.append(fib[-1] + fib[-2])

for idx, num in enumerate(fib, 1):
    print(f"{idx}: {num}")