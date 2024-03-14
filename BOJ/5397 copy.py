# 링크드 리스트로 해보면 어떨까!
from sys import stdin 


input = stdin.readline

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0 

    def append(self,node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def insertNodeAtIndex(self,idx,node):
        curn = self.head
        prevn = None
        cur_i = 0

        if idx == 0 :
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node

        else:
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = curn 
                prevn.next = node
            else:
                return -1
    
    def deleteAtIndex(self,idx):
        curn_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.next
        
        if idx == 0:
            self.head = nextn
        else:
            while curn_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next
                else:
                    break
                curn_i +=1 
            if curn_i == idx:
                prevn.next = nextn
            else:
                return -1 
            
    def getlength(self):
        # if data == 0: return -1 
        curn = self.head
        idx = 0
        while curn:
            idx += 1
        return idx
    
    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += ""
            curn = curn.next
    
        return len(string), string


## 답코드 
for _ in range(int(input())):
    logger = input().rstrip()
    lis = LinkedList()
    idx = 0 
    for log in logger:
        print("log : ", log , "idx : ", idx)

        if log == "<" :
            if idx <= 0 : 
                idx = 0
            else: 
                idx = idx - 1 

        elif log == ">":
            idx += 1 
            length , answer = lis.print()

        elif log == "-":
            lis.deleteAtIndex(idx-1)
            length , answer = lis.print()


        else : 
            length , answer = lis.print()
            if idx <  length:
                lis.insertNodeAtIndex(idx-1 , Node(log))
            else: 
                lis.insertNodeAtIndex(idx,Node(log))
                idx += 1 
        
    _, an = lis.print()
    print(an)