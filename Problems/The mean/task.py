numbers = []
while True:
    inp = input()
    try:
        numbers.append(int(inp))
    except ValueError:
        break
print(sum(numbers) / len(numbers))