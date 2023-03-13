
def solution(numbers):
    if numbers == [0]*len(numbers):
        return '0'
    nums = list(map(str,numbers))
    nums = sorted(nums, key = lambda x : x*3, reverse= True)
    return ''.join(nums)




if __name__ == '__main__': 
    # numbers = [3,30,34,5,9]
    numbers = [0,0,0,0] 
    # numbers = [6,10,2]
    print(solution(numbers))