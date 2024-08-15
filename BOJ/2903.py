
dot_count = [i for i in range(1, int(input()) + 1)]

dot = 0
inital = 1

for i  in dot_count:
    inital = (2**i) +1  # 1일때 3 , 2일 때 , 5(2**2 +1 )  3일때 , 8
    dot = inital * inital
print(dot)

