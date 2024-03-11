def main(x,y,z):
    return x+y+z



if __name__ == "__main__":
    a,b,c = map(int, input().split())
    print(main(a,b,c))