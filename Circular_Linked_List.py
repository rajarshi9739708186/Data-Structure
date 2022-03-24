# Create a Node Object
# Holds Data
# Holds Address of Next Node pointing to
# Every time a new node created, it should point to Nothing
class Node:
    def __init__(self, data):
        self.NodeData = data
        self.NextNodePointer = None

class CircularLinkedList:
    # While we will create Linked list
    # Last Node pointer will be created
    # It suppose to point very Last node of linked list
    def __init__(self):
        self.LastNodePointer = None

    # Traverse entire Linked List
    def traverseLinkedList(self):
        # If Linked List doesn't contain any node
        if self.LastNodePointer == None:
            print("Linked List is Empty")
        else:
            tempNodePointer = self.LastNodePointer.NextNodePointer  # Create a Temporary pointer, which will Point to First Node
            while tempNodePointer != self.LastNodePointer:  # Till Last Node Traversal will be
                print(tempNodePointer.NodeData)
                tempNodePointer = tempNodePointer.NextNodePointer
            print(tempNodePointer.NodeData) # For Last Node

    # Search Data in Linked List
    def searchDataInLinkedList(self, dataToBeSearched):
        # If Linked List doesn't contain any node
        if self.LastNodePointer == None:
            print("Linked List is Empty")
        else:
            tempNodePointer = self.LastNodePointer.NextNodePointer  # Create a Temporary pointer, which will Point to First Node
            while tempNodePointer != self.LastNodePointer:  # Till Last Node Traversal will be
                if tempNodePointer.NodeData == dataToBeSearched:
                    print(f"{dataToBeSearched} exist in Linked List")
                    return
                tempNodePointer = tempNodePointer.NextNodePointer
            if tempNodePointer.NodeData == dataToBeSearched: # For Last Node
                print(f"{dataToBeSearched} exist in Linked List")
                return
            # All Node Traversed. Data Not Found
            print(f"{dataToBeSearched} doesn't exist in Linked List")

    # Add a node at the end of the Linked List
    def addNodeAtLast(self, node_data):
        # Create Node
        New_Node = Node(node_data)

        # If Linked List doesn't contain any node
        if self.LastNodePointer == None:
            # As LastNodePointer is pointing to Nothing
            # Now it will point to created Node
            self.LastNodePointer = New_Node
            self.LastNodePointer.NextNodePointer = self.LastNodePointer # It points to itself only
        else:
            New_Node.NextNodePointer = self.LastNodePointer.NextNodePointer # New Node Points to First Node
            self.LastNodePointer.NextNodePointer = New_Node # Current Last Node will point to New Node and New Node Becomes Last one
            self.LastNodePointer = self.LastNodePointer. NextNodePointer # Last Node Pointer will point to Last Node

    # Add a node at First of Linked List
    def addNodeAtFirst(self, node_data):
        # Create Node
        New_Node = Node(node_data)

        # If Linked List doesn't contain any node
        if self.LastNodePointer == None:
            # As LastNodePointer is pointing to Nothing
            # Now it will point to created Node
            self.LastNodePointer = New_Node
            self.LastNodePointer.NextNodePointer = self.LastNodePointer  # It points to itself only
        else:
            New_Node.NextNodePointer = self.LastNodePointer.NextNodePointer  # New Node Points to First Node
            self.LastNodePointer.NextNodePointer = New_Node  # Current Last Node will point to New Node and New Node Becomes Last one

    # Add a node after a particular node in Linked List
    def addNodeAfterANode(self, node_data_to_be_added, after_node_data):
        # Create Node
        New_Node = Node(node_data_to_be_added)

        # If Linked List doesn't contain any node
        if self.LastNodePointer == None:
            print("Linked List is Empty")
        else:
            # Search that particular node which contains that particular data
            tempNodePointer = self.LastNodePointer.NextNodePointer  # Create a Temporary pointer, It will point to First Node

            while tempNodePointer != self.LastNodePointer:  # Till Last Node Traversal will be
                if tempNodePointer.NodeData == after_node_data:
                    # That Particular Node found
                    New_Node.NextNodePointer = tempNodePointer.NextNodePointer  # New Node will point to First Node
                    tempNodePointer.NextNodePointer = New_Node  # Current Last Node will point to New Node
                    return
                tempNodePointer = tempNodePointer.NextNodePointer

            if tempNodePointer.NodeData == after_node_data: # Last Node is that Particular Node
                New_Node.NextNodePointer = tempNodePointer.NextNodePointer  # New Node will point to First Node
                tempNodePointer.NextNodePointer = New_Node  # Current Last Node will point to New Node
                self.LastNodePointer = self.LastNodePointer.NextNodePointer # New Node become Last Node
                return

            # All Node Traversed. Data Not Found
            print(f"{after_node_data} doesn't exist in Linked List")

    # Delete First Node from Linked List
    def deleteFirstNode(self):
        # If Linked List doesn't contain any node
        if self.LastNodePointer == None:
            print("Linked List is Empty")
        else:
            tempNodePointer = self.LastNodePointer.NextNodePointer  # Point to the First Node by a temporary pointer

            # If List Contains only One Node
            if tempNodePointer == self.LastNodePointer:
                self.LastNodePointer = None # Last Node Pointer will point to Nothing
                del tempNodePointer
            else:
                self.LastNodePointer.NextNodePointer = tempNodePointer.NextNodePointer # Last Node will point to Second Last Node
                del tempNodePointer # Second Last Node become the First

    # Delete Last Node from Linked List
    def deleteLastNode(self):
        # If Linked List doesn't contain any node
        if self.LastNodePointer == None:
            print("Linked List is Empty")
        else:
            tempNodePointer = self.LastNodePointer.NextNodePointer  # Point to the First Node by a temporary pointer

            # If List Contains only One Node
            if tempNodePointer == self.LastNodePointer:
                self.LastNodePointer = None  # Last Node Pointer will point to Nothing
                del tempNodePointer
            else:
                while tempNodePointer.NextNodePointer != self.LastNodePointer: # Reach Till Second Last Node
                    tempNodePointer = tempNodePointer.NextNodePointer
                self.LastNodePointer = tempNodePointer
                tempNodePointer = tempNodePointer.NextNodePointer
                self.LastNodePointer.NextNodePointer = tempNodePointer.NextNodePointer
                del tempNodePointer

    #  Delete a Particular node. Will identify through Node Data
    def deleteParticularNode(self, node_data_to_be_deleted):
        # If Linked List doesn't contain any node
        if self.LastNodePointer == None:
            print("Linked List is Empty")
        else:
            tempNodePointer = self.LastNodePointer.NextNodePointer  # Temporary pointer will point to First Node
            FirstNodePointer = self.LastNodePointer.NextNodePointer  # Specific Pointer for First Node

            # If Linked List contain only one Node
            if tempNodePointer == self.LastNodePointer:
                if tempNodePointer.NodeData == node_data_to_be_deleted:  # That Particular Node found
                    self.LastNodePointer = None  # Start Pointer will point to Nothing
                    del tempNodePointer  # Delete First Node
                else:
                    print(f"{node_data_to_be_deleted} doesn't exist in linked List")
            else:
                # If First Node is that Particular Node
                if tempNodePointer.NodeData == node_data_to_be_deleted:
                    self.LastNodePointer.NextNodePointer = tempNodePointer.NextNodePointer  # Last Node will point to Second Node
                    del tempNodePointer  # First Node deleted. Second Node become First Node
                else:
                    # Check for Rest of the Nodes
                    # In Between First and Last Nodes
                    while tempNodePointer.NextNodePointer.NextNodePointer != FirstNodePointer:  # Temporary Pointer will point to Second Last Node
                        if tempNodePointer.NextNodePointer.NodeData == node_data_to_be_deleted:  # Found that Particular Node
                            NodeToBeDeleted = tempNodePointer.NextNodePointer  # Create another Temporary pointer which points to that Particular Node
                            tempNodePointer.NextNodePointer = tempNodePointer.NextNodePointer.NextNodePointer  # Previous Node of need to be deleted Node will point to that Node which is pointed by Node to be deleted
                            del NodeToBeDeleted
                            return
                        tempNodePointer = tempNodePointer.NextNodePointer

                    # After this while loop Temporary Pointer will point to Second Last Node
                    if tempNodePointer.NextNodePointer.NodeData == node_data_to_be_deleted:  # Data found in Last Node
                        self.LastNodePointer = tempNodePointer
                        tempNodePointer = tempNodePointer.NextNodePointer
                        self.LastNodePointer.NextNodePointer = tempNodePointer.NextNodePointer
                        del tempNodePointer
                        return

                    print(f"{node_data_to_be_deleted} doesn't exist in linked List")

# Start Circular Linked List
CircularLinkedList_object = CircularLinkedList() # StartNodePointer created, pointing to Nothing

while True:
    print("")
    print("Press 1 to add data into Circular Linked List")
    print("Press 2 to print Circular Linked List")
    print("Press 3 to search data in Circular Linked List")
    print("Press 4 to delete data from Circular Linked List")
    print("Press 5 to Quit operation")
    print("")

    user_choice = int(input("Enter your choice : ").strip())

    if user_choice == 2:
        CircularLinkedList_object.traverseLinkedList()
    if user_choice == 3:
        data_to_be_searched = int(input("data to be searched : ").strip())
        CircularLinkedList_object.searchDataInLinkedList(data_to_be_searched)
    if user_choice == 1:
        print("Press 1 to add data at last of Circular Linked List")
        print("Press 2 to add data at first of Circular Linked List")
        print("Press 3 to add data at after any node of Circular Linked List")

        user_choice_to_add_data = int(input("Enter your choice to add data : ").strip())

        if user_choice_to_add_data == 1:
            data_to_be_added = int(input("data to be added : ").strip())
            CircularLinkedList_object.addNodeAtLast(data_to_be_added)

        if user_choice_to_add_data == 2:
            data_to_be_added = int(input("data to be added : ").strip())
            CircularLinkedList_object.addNodeAtFirst(data_to_be_added)

        if user_choice_to_add_data == 3:
            data_to_be_added = int(input("data to be added : ").strip())
            data_to_be_added_after_which_data = int(input("data to be added after which data : ").strip())
            CircularLinkedList_object.addNodeAfterANode(data_to_be_added, data_to_be_added_after_which_data)
    if user_choice == 4:
        print("Press 1 to delete First data from Circular Linked List")
        print("Press 2 to delete Last data from Circular Linked List")
        print("Press 3 to delete Specific data from Circular Linked List")

        user_choice_to_delete_data = int(input("Enter your choice to delete data : ").strip())

        if user_choice_to_delete_data == 1:
            CircularLinkedList_object.deleteFirstNode()
        if user_choice_to_delete_data == 2:
            CircularLinkedList_object.deleteLastNode()
        if user_choice_to_delete_data == 3:
            data_to_be_deleted = int(input("data to be deleted : ").strip())
            CircularLinkedList_object.deleteParticularNode(data_to_be_deleted)
    if user_choice == 5:
        break