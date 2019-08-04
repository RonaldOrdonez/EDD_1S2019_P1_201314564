from Structures.score import StackScore, NodeScore
from Structures.scoreboard import QueueScoreBoard, NodeScoreBoard
from Structures.users import DoublyLinkedListUser, NodeUser

#EXAMPLE OF List of USERS
print(" ")
print(" ")
print("Hello List of Users")
listUser = DoublyLinkedListUser()
listUser.add(NodeUser("Ana"))
listUser.add(NodeUser("Brenda"))
listUser.add(NodeUser("Carol"))
listUser.printListUsers()

#EXAMPLE OF STACK OF SCORE
print(" ")
print(" ")
print("Hello Stack of Score")

stack = StackScore()
stack.push(NodeScore(1,1))
stack.push(NodeScore(2,2))
stack.push(NodeScore(3,3))
stack.printStackScore()
stack.pop()
stack.printStackScore()

#EXAMPLE OF QUEUE OF SCORE BOARD
print(" ")
print(" ")
print("Hello Queue of Score Board")

queueSB = QueueScoreBoard()
queueSB.queue(NodeScoreBoard("Ana",34))
queueSB.queue(NodeScoreBoard("Berta",54))
queueSB.queue(NodeScoreBoard("Camila",10))
queueSB.printQueueScoreBoard()
queueSB.dequeue()
queueSB.printQueueScoreBoard()






