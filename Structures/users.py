import os
import subprocess
#Definition of class node of User
class NodeUser:
    #constructor od node user qith name like parameter
    def __init__(self, name):
        self.name = name
        self.next = None
        self.previous = None 

#definition of class User where it is defined methods, DOUBLE LINKED CIRCULAR LIST
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
    
    #function to graphic the list with software Graphiz
    def graphicUserList(self):
        if self.head is None:               #verify if our LinkedList is empty
            print('The list is empty')      #print a warning
        else:
            f = open('ReportUsers.dot','w')   #name to save .do
            f.write('digraph usersGraph { \n')
            f.write('node [shape=record]; \n')
            f.write('rankdir = LR; \n')
            temp = self.head
            count = 0

            while temp.next is not self.head:                  
                f.write('node{} [label=\" {} \"]; \n'.format(count,temp.name)) 
                count +=1
                f.write('node{} -> node{}; \n'.format(count-1,count))                
                f.write('node{} -> node{}; \n'.format(count,count-1))                
                temp = temp.next              
            f.write('node{} [label=\" {} \"]; \n'.format(count,temp.name)) 
            f.write('node{} -> node{}; \n'.format(count,0))                
            f.write('node{} -> node{}; \n'.format(0,count))                
            f.write('}')                    
            f.close()
            os.system('dot ReportUsers.dot -Tpng -o ReportUsers.png')
            subprocess.call('ReportUsers.png', shell=True)     # metodo que funciona
            #os.popen('LinkedList.png')                        # para windows
            #subprocess.check_call(['open','LinkedList.png']) 
            

"""
#TEST
print("Hello List of Users")
listUser = DoublyLinkedListUser()
listUser.add(NodeUser("Ana"))
listUser.add(NodeUser("Brenda"))
listUser.add(NodeUser("Carol"))
listUser.add(NodeUser("Daniella"))
listUser.add(NodeUser("Elena"))
listUser.add(NodeUser("Fernanda"))
listUser.add(NodeUser("Gabriela"))
listUser.add(NodeUser("Isabel"))
listUser.printListUsers()
listUser.graphicUserList()
"""

   