# Queue implementation using Single Linked List
# Start Pointer Will point to FIrst Node Always
# Insert Node always at Last
# Delete Node always from First

class Node:
    def __init__(self, data):
        self.NodeData = data
        self.NextNodePointer = None

class Queue:
    def __init__(self):
        self.StartNodePointer = None

    # Insert Node at Last
    def insertIntoQueue(self, data):
        NewNode = Node(data)

        # Queue is empty
        if self.StartNodePointer == None:
            self.StartNodePointer = NewNode
        else:
            TempNodePointer = self.StartNodePointer
            while TempNodePointer.NextNodePointer != None: # Temp Node Pointer pointing to last Node
                TempNodePointer = TempNodePointer.NextNodePointer
            TempNodePointer.NextNodePointer = NewNode # Node inserted at Lat

    # Delete Node from First
    def deleteFromQueue(self):
        # No Data in Queue
        if self.StartNodePointer == None:
            print("Queue is Empty")
        else:
            NodeToBeDeleted = self.StartNodePointer # Current First Node will be deleted
            DeletedData = NodeToBeDeleted.NodeData
            self.StartNodePointer = NodeToBeDeleted.NextNodePointer # Start will point to current Second Node
            del NodeToBeDeleted # First Node deleted and Second node become first node
            print(f"Deleted Data : {DeletedData}")

    # Print all data from Queue
    def printAllData(self):
        # No Data in Queue
        if self.StartNodePointer == None:
            print("Queue is Empty")
        else:
            TempNodePointer = self.StartNodePointer
            while TempNodePointer != None:
                print(TempNodePointer.NodeData)
                TempNodePointer = TempNodePointer.NextNodePointer

# Initialize Queue
Queue_Object = Queue()

while True:
    print("")
    print("Press 1 to Insert data into Queue")
    print("Press 2 to Delete data from Queue")
    print("Press 3 to print all data from Queue")
    print("Press 4 to Quit operation")
    print("")

    user_choice = int(input("Enter your choice : ").strip())

    if user_choice == 1:
        data_to_be_added = int(input("data to be added : ").strip())
        Queue_Object.insertIntoQueue(data_to_be_added)
    elif user_choice == 2:
        Queue_Object.deleteFromQueue()
    elif user_choice == 3:
        Queue_Object.printAllData()
    elif user_choice == 4:
        print("Bye")
        break


