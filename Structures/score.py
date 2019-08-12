import os
import subprocess

class NodeScore:
    def __init__(self, axisX, axisY):
        self.axisX = axisX
        self.axisY = axisY
        self.next = None

class StackScore:
    #Constructor class StackScore
    def __init__(self):        
        self.peak = None
    
    #method ADD to add elements to stack
    def push(self, actualNode):
        if self.peak is None:
            self.peak = actualNode            
        else:
            actualNode.next = self.peak
            self.peak = actualNode
    
    #method to delete a peak of stack 
    def pop(self):
        if self.peak is None:
            print("Stack Empty, Impossible to POP")
        else:
            self.peak = self.peak.next        
                    
    #method print to show stack in console
    def printStackScore(self):        
        aux = self.peak
        if aux is None:
            print ("Stack Empty")
        else:
            while aux is not None:
                print("(",end="")
                print(aux.axisX, end = "")
                print(",",end="")
                print(aux.axisY, end = "")                
                print(")",end="")
                print("-> ", end = "")
                aux = aux.next            
            print (" NULL")
    
    #function to graph to stack
    def graphStack(self):
        if self.peak is None:               #verify if queue is empty
            print('The Stack is empty')      
        else:
            f = open('ReportScore.dot','w')   #name to save .do
            f.write('digraph scoreGraph { \n')
            f.write('nodesep = 0.5; \n')            
            f.write('rankdir = LR; \n')
            f.write('node [shape=record,width=1.5, height=4.0]; \n')         
            temp = self.peak
            count = 1
            f.write('node0 [label = \"<f0> |')
            while temp.next is not None:
                f.write('<f{}> {},{} | '.format(count, temp.axisY, temp.axisX)) 
                count +=1                
                temp = temp.next              
            f.write('<f{}> {},{}'.format(count, temp.axisY, temp.axisX)) 
            f.write('\" , height=3.0]; \n')                    
            f.write("}")
            f.close()
            os.system('dot ReportScore.dot -Tpng -o ReportScore.png')
            subprocess.call('ReportScore.png', shell=True)     # metodo que funciona
            #os.popen('LinkedList.png')                        # para windows
            #subprocess.check_call(['open','LinkedList.png']) 

#TEST
"""
pila = StackScore()
pila.push(NodeScore(0,1))
pila.push(NodeScore(2,3))
pila.push(NodeScore(4,5))
pila.push(NodeScore(6,7))
pila.push(NodeScore(8,9))
pila.printStackScore()
pila.graphStack()
"""
  
