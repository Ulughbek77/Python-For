sonlar = list(map(int, input("Sonlarni kiriting: ").split(",")))
minimum = min(sonlar)
maximum = max(sonlar)
ortacha = (minimum + maximum) / 2
print(ortacha)
# Input: 3,5,1,8,7 → Output: 4.5
