import os
import subprocess

class NodeScoreBoard:    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None

class QueueScoreBoard:    
    
    #Constructor class ScoreBoard
    def __init__(self):        
        self.head = None       
        self.sizeQueue = 0
    
    #return head
    def getHead(self):
        return self.head
    
    #method to add elements to Queue
    def queue(self, nodeInsert):
        if self.sizeQueue < 10:          #only accept 10 elements in queue 
            if self.head is None:
                self.head = nodeInsert
                self.sizeQueue += 1
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = nodeInsert
                self.sizeQueue += 1
        else:
            self.dequeue()
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = nodeInsert
            self.sizeQueue += 1
    
    #method to eliminate a node of queue   
    def dequeue(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            self.head = self.head.next
            self.sizeQueue -= 1
            
                    
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
    
    #function to graph queue score board
    def graphScoreBoard(self):
        if self.head is None:               #verify if queue is empty
            print('The Queue is empty')      
        else:
            f = open('ReportScoreBoard.dot','w')   #name to save .do
            f.write('digraph scoreBoardGraph { \n')
            f.write('node [shape=record]; \n')
            f.write('rankdir = LR; \n')
            temp = self.head
            count = 0
            while temp.next is not None:
                f.write('node{} [label=\" {}, {} \"]; \n'.format(count, temp.name, temp.score)) 
                count +=1
                f.write('node{} -> node{}; \n'.format(count-1,count))                                              
                temp = temp.next              
            f.write('node{} [label=\" {}, {} \"]; \n'.format(count, temp.name, temp.score))
            count +=1
            f.write('node{} -> node{}; \n'.format(count-1,count))                                             
            f.write('node{} [label=\" NULL\"]; \n'.format(count))
            f.write('}')                    
            f.close()
            os.system('dot ReportScoreBoard.dot -Tpng -o ReportScoreBoard.png')
            subprocess.call('ReportScoreBoard.png', shell=True)     # metodo que funciona
            #os.popen('LinkedList.png')                        # para windows
            #subprocess.check_call(['open','LinkedList.png']) 
            
#TEST
"""
scoreb = QueueScoreBoard()
scoreb.queue(NodeScoreBoard("ana",3))
scoreb.queue(NodeScoreBoard("beny",14))
scoreb.queue(NodeScoreBoard("cecy",19))
scoreb.queue(NodeScoreBoard("dany",90))
scoreb.queue(NodeScoreBoard("helen",1))
scoreb.queue(NodeScoreBoard("Julieta",50))
scoreb.printQueueScoreBoard()
scoreb.graphScoreBoard()
"""
