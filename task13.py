narxlar = list(map(int, input("5 ta telefon narxini kiriting: ").split(",")))
minimum = min(narxlar)
maximum = max(narxlar)
print(f"{minimum}, {maximum}")
# Input: 300,450,150,720,620 → Output: 150, 720
