from sys import stdin

input = stdin.readline

# 이걸 리스트로 만들어야겠다.

total_major = []
for _ in range(20):
    name , unit , grade = input().split()
    total_major.append([float(unit),grade])


mapping = { "A+" : 4.5,
            "A0" : 4.0,
            "B+" : 3.5,
            "B0" : 3.0,
            "C+" : 2.5,
            "C0" : 2.0,
            "D+" : 1.5,
            "D0" : 1.0,
            "P" : 0.0,
            "F" : 0.0,}
total = 0.0
unit_total = 0.0

for unit, grade in total_major:
    if grade == "P":
        continue
    val = unit * mapping[grade]
    unit_total += unit
    total += val

result = total / unit_total
print(f"{result:.6f}")