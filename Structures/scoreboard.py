class NodeScoreBoard:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None

class QueueScoreBoard:
    #Constructor class ScoreBoard
    def __init__(self):        
        self.head = None       
    
    #method to add elements to Queue
    def queue(self, nodeInsert):
        if self.head is None:
            self.head = nodeInsert
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = nodeInsert
    
    #method to eliminate a node of queue   
    def dequeue(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            self.head = self.head.next
            
                    
    #method print to show queue in console
    def printQueueScoreBoard(self):        
        aux = self.head
        if self.head is None:
            print ("Queue Empty")
        else:
            while aux.next is not None:
                print(aux.name, end="")
                print(":",end="")
                print(aux.score, end="")               
                print("-> ", end = "")
                aux = aux.next
            print(aux.name, end = "")
            print(":",end="")
            print(aux.score, end = "")
            print ("-> NULL")


  
