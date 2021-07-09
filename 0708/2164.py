from collections import deque 

deq = deque() 

for x in range(1, int(input())+1): 
    deq.append(x)
print("original deque : " , deq)


print(deq.popleft())
deq = deq.append(deq[0])
print(deq[0])
# while True:
#     if len(deq) > 1 :
#         deq.popleft()
#         deq.append(deq[0])
#         deq.remove(deq[0])
#         print(deq)
    
#     elif len(deq) == 1:
#         print(deq)