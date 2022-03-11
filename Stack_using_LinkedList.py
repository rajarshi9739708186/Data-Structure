# Stack Implementation using Single Linked List
# Top Node Pointer will always point First Node
# Insert at First
# Delete Always First

class Node:
    def __init__(self, data):
        self.NodeData = data
        self.NextNodePointer = None

class Stack:
    def __init__(self):
        self.TopNodePointer = None

    # Insert at First into Linked List
    def pushDataIntoStack(self, data):
        NewNode = Node(data)

        NewNode.NextNodePointer = self.TopNodePointer # New Node will point to current Top Node
        self.TopNodePointer = NewNode # Ne Node become Top Node

    # Delete First Node from Linked List
    def popDataFromStack(self):
        # No Data in Stack
        if self.TopNodePointer == None:
            print("Stack is Empty")
        else:
            NodeToBeDeleted = self.TopNodePointer
            PoppedOutData = NodeToBeDeleted.NodeData
            self.TopNodePointer = NodeToBeDeleted.NextNodePointer # Top will Point to Current Second Node
            del NodeToBeDeleted # First Node delete and Second Node become Top Node
            print(f"Popped Out : {PoppedOutData}")

    # Print All Node
    def printAllData(self):
        # No Data in Stack
        if self.TopNodePointer == None:
            print("Stack is Empty")
        else:
            TempNodePointer = self.TopNodePointer
            while TempNodePointer != None:
                print(TempNodePointer.NodeData)
                TempNodePointer = TempNodePointer.NextNodePointer

# Initialize Stack
Stack_Object = Stack()

while True:
    print("")
    print("Press 1 to Push data into Stack")
    print("Press 2 to Pop data from Stack")
    print("Press 3 to print all data from Stack")
    print("Press 4 to Quit operation")
    print("")

    user_choice = int(input("Enter your choice : ").strip())

    if user_choice == 1:
        data_to_be_added = int(input("data to be added : ").strip())
        Stack_Object.pushDataIntoStack(data_to_be_added)
    elif user_choice == 2:
        Stack_Object.popDataFromStack()
    elif user_choice == 3:
        Stack_Object.printAllData()
    elif user_choice == 4:
        print("Bye")
        break

