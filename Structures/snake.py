import os
import subprocess

#Definition of class snake
class NodeSnake:
    #constructor of node snake
    def __init__(self, position_Y, position_X):
        self.position_X = position_X
        self.position_Y = position_Y
        self.next = None
        self.previous = None 

#definition of class Snake, type of List is Double Linked List Simple
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
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = currentNode
            currentNode.previous = temp
            currentNode.next = None          
    
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

    #function to graph actual state of snake
    def graphSnake(self):
        if self.head is None:               #verify if our LinkedList is empty
            print('The list is empty')      #print a warning
        else:
            f = open('ReportSnake.dot','w')   #name to save .do
            f.write('digraph usersGraph { \n')
            f.write('node [shape=record]; \n')
            f.write('rankdir = LR; \n')
            temp = self.head
            count = 0                        
            while temp.next is not None:                  
                f.write('node{} [label=\"({},{})\"]; \n'.format(count, temp.position_Y, temp.position_X)) 
                count +=1
                f.write('node{} -> node{}; \n'.format(count-1,count))                
                f.write('node{} -> node{}; \n'.format(count,count-1))                
                temp = temp.next              
            f.write('node{} [label=\"({},{})\"]; \n'.format(count,temp.position_Y, temp.position_X))             
            f.write('}')                    
            f.close()
            os.system('dot ReportSnake.dot -Tpng -o ReportSnake.png')
            subprocess.call('ReportSnake.png', shell=True)     # metodo que funciona
            #os.popen('LinkedList.png')                        # para windows
            #subprocess.check_call(['open','LinkedList.png']) 

#TEST            
snake = ListSnake()
snake.add(NodeSnake(1,2))
snake.add(NodeSnake(1,3))
snake.add(NodeSnake(1,4))
snake.add(NodeSnake(1,5))
snake.printSnake()
snake.graphSnake()

   