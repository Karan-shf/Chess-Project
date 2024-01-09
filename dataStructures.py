class Stack:

    def __init__(self,max) -> None:
        self.top = -1
        self.max = max
        self.properties = []
        for i in range(max):
            self.properties.append(None)

    def push(self,value):
        
        if self.isFull():
            raise Exception('Stack is Full')
        else:
            self.top += 1
            self.properties[self.top] = value
            
    def pop(self):

        if self.isEmpty():
            raise Exception('Stack is Empty')
        else:
            index = self.top
            self.top -=1
            return self.properties[index]

    def isFull(self):

        if self.max-1 == self.top:
            return True
        else:
            return False
        
    def isEmpty(self):

        if self.top==-1:
            return True
        else:
            return False
        
    def printProperties(self):
        
        for i in range(self.top,-1,-1):
            print(self.properties[i])

    def clear(self):
        self.properties.clear()
        for i in range(self.max):
            self.properties.append(None)
        self.top = -1

    def count(self):
        return self.top + 1

class Queue:

    def __init__(self,max) -> None:

        self.rear = -1
        self.front = -1
        self.max = max
        self.properties = []
        for i in range(max):
            self.properties.append(None)

    def add(self,value):

        if self.isFull():
            raise Exception('Queue is Full')
        else:
            self.rear +=1
            self.properties[self.rear]=value

    def dequeue(self):

        if self.isEmpty():
            raise Exception('Queue is Empty')
        else:
            self.front+=1
            return self.properties[self.front]

    def isFull(self):

        if self.max-1 == self.rear:
            return True
        else:
            return False
        
    def isEmpty(self):

        if self.front==self.rear:
            return True
        else:
            return False
        
    def printProperties(self):

        for i in range(self.front+1,self.rear+1):
            print(self.properties[i])

    def clear(self):
        self.properties.clear()
        for i in range(self.max):
            self.properties.append(None)
        self.rear = -1
        self.front = -1


game_moves = Queue(12000)

game_moves_stack = Stack(12000)
game_moves_temp_stack = Stack(12000)