# 시간초과 
# def solution(phone_book):
#     phone_book.sort(key = lambda x : len(x))
#     for one in phone_book:
#         for two in phone_book[1:]:
#             if one != two and one  == two[:len(one)]:
#                 return False 
    
#     return True


# startswith 와 sort를 사용한 방법
def solution(phoneBook):
    phoneBook.sort()
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

if __name__ == '__main__': 

    # p_book = ["119", "97674223", "1195524421"]
    p_book = ["12","135","13543","112","88"]
    # p_book = ["12","123","1235","88","8856"]
    print(solution(p_book))
    