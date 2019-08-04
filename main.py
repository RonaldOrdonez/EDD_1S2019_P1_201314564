from Structures.score import StackScore, NodeScore

print("Hello Stack")

stack = StackScore()
stack.push(NodeScore(1,1))
stack.push(NodeScore(2,2))
stack.push(NodeScore(3,3))
stack.printStackScore()
stack.pop()
stack.printStackScore()




