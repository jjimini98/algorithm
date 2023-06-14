from sys import stdin

input = stdin.readline

y = -999
a,b,c,d,e,f = list(map(int, input().split()))

while y <= 999:
    formula = f"{c * d} + ({a * e} - {b * d}) * {y} - {a * f} "

    if eval(formula) == 0:
        try:
            x = f"({c} - {b*y}) // {a}"
            print(eval(x), y)
        except:
            x = f"({f} - {e * y}) // {d}"
            print(eval(x),y)
        break
    else:
        y += 1
