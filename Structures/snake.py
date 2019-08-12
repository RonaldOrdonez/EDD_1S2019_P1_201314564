#Definition of class snake
class NodeSnake:
    #constructor of node snake
    def __init__(self, position_X, position_Y):
        self.position_X = position_X
        self.position_Y = position_Y
        self.next = None
        self.previous = None 

#definition of class Snake
class ListSnake:

    #constructor of class
    def __init__(self):
        self.head = None
    
    #function to add size to snake
    def add(self, currentNode):
        if self.head is None:            
            self.head = currentNode
            self.head.next = None
            self.head.previous = None
        else:
            currentNode.next = self.head
            currentNode.previous = None
            self.head.previous = currentNode            
            self.head = currentNode     
    
    #function to print all list
    def printSnake(self):
        aux = self.head

        if self.head is None:
            print ("List Empty")
        else:
            print(aux.position_X ,end="")                
            print(":")
            print("Next ->", end = "")
            print(aux.next.position_X)
            print("Previous ->", end = "")
            print("NULL")
            print("")  
            aux = aux.next

            while aux.next is not None:
                print(aux.position_X,end="")                
                print(":")
                print("Next ->", end = "")
                print(aux.next.position_X)
                print("Previous ->", end = "")
                print(aux.previous.position_X)
                print("")                
                aux = aux.next
            print(aux.position_X,end="")    
            print(":")
            print("Next ->", end = "")
            print("NULL")
            print("Previous ->", end = "")
            print(aux.previous.position_X)
            print("")  
            
snake = ListSnake()
snake.add(NodeSnake(1,2))
snake.add(NodeSnake(3,4))
snake.add(NodeSnake(5,6))
snake.printSnake()

   