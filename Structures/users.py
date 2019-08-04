#Definition of class node of User
class NodeUser:
    #constructor od node user qith name like parameter
    def __init__(self, name):
        self.name = name
        self.next = None
        self.previous = None 

#definition of class User where it is defined methods
class DoublyLinkedListUser:

    #constructor of class
    def __init__(self):
        self.head = None
    
    #function to add users to list
    def add(self, currentNode):
        if self.head is None:            
            self.head = currentNode
            self.head.next = self.head
            self.head.previous = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = currentNode
            currentNode.previous = temp
            currentNode.next = self.head
            self.head.previous = currentNode
    
    #function to print all list
    def printListUsers(self):
        aux = self.head

        if self.head is None:
            print ("List Empty")
        else:
            while aux.next is not self.head:
                print(aux.name,end="")                
                print(":")
                print("Next ->", end = "")
                print(aux.next.name)
                print("Previous ->", end = "")
                print(aux.previous.name)
                print("")                
                aux = aux.next
            print(aux.name,end="")    
            print(":")
            print("Next ->", end = "")
            print(aux.next.name)
            print("Previous ->", end = "")
            print(aux.previous.name)
            print("")  
            

   