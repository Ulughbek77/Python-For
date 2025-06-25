n = int(input("N ni kiriting: "))
juft = 0
toq = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        juft += i
    else:
        toq += i
print(f"{juft}, {toq}")
# Input: 6 → Output: 12, 9
