def solution(s):

    count, zero_count = 0 , 0

    while True:

        if s == "1":

            return [count, zero_count] 
        
        zero_count += s.count("0")
        s = s.replace("0",'')

        s = str(bin(len(s)))[2:]

        count += 1



if __name__ == '__main__': 
    s = "01110"
    print(solution(s))