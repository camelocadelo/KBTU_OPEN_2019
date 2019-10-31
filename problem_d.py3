input1 = input()
input_a = input()
input_b = input()

a = list(map(int, input_a.split()))
b = list(map(int, input_b.split()))

a.sort(reverse = True)
b.sort()

c = [x + y for x, y in zip(a, b)]

min = min(c)
max = max(c)

result = (abs(max-min))

print(result)

