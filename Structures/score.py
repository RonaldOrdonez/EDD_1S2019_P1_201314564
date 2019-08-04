class Node:
    def __init__(self, axisX, axisY):
        self.axisX = axisX
        self.axisY = axisY
        self.next = None

class StackScore:
    #Constructor class StackScore
    def __init__(self):        
        self.peak = None
    
    #method ADD to add elements to stack
    def add(self, actualNode):
        if self.peak is None:
            self.peak = actualNode            
        else:
            actualNode.next = self.peak
            self.peak = actualNode
                    
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


  
