# Create a Node Object
# Holds Data
# Holds Address of Next Node pointing to
# Every time a new node created, it should point to Nothing
class Node:
    def __init__(self, data):
        self.NodeData = data
        self.NextNodePointer = None

class SingleLinkedList:
    # While we will create Linked list
    # Start Node pointer will be created
    # It suppose to point very first node of linked list
    def __init__(self):
        self.StartNodePointer = None

    # Traverse entire Linked List
    def traverseLinkedList(self):
        tempNodePointer = self.StartNodePointer  # Create a Temporary pointer, Using this will traverse List

        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            print("Linked List is Empty")
        else:
            while tempNodePointer != None: # Till Last Node Traversal will be
                print(tempNodePointer.NodeData)
                tempNodePointer = tempNodePointer.NextNodePointer

    # Search Data in Linked List
    def searchDataInLinkedList(self, dataToBeSearched):
        tempNodePointer = self.StartNodePointer  # Create a Temporary pointer, Using this will traverse List

        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            print("Linked List is Empty")
        else:
            while tempNodePointer != None:  # Till Last Node Traversal will be
                if tempNodePointer.NodeData == dataToBeSearched:
                    print(f"{dataToBeSearched} exist in Linked List")
                    return
                tempNodePointer = tempNodePointer.NextNodePointer
            # All Node Traversed. Data Not Found
            print(f"{dataToBeSearched} doesn't exist in Linked List")

    # Add a node at the end of the Linked List
    def addNodeAtLast(self, node_data):
        # Create Node
        New_Node = Node(node_data)

        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            # As StartNodePointer is pointing to Nothing
            # Now it will point to created Node
            self.StartNodePointer = New_Node
        else:
            tempNodePointer = self.StartNodePointer # Create a Temporary pointer, Using this will traverse List

            # Traverse till last node of the list
            while tempNodePointer.NextNodePointer != None:
                tempNodePointer = tempNodePointer.NextNodePointer

            # Now tempNodePointer is pointing to Last Pointer
            tempNodePointer.NextNodePointer = New_Node #Last node of the existing list will be pointing to New Node. New Node becomes last

    # Add a node at First of Linked List
    def addNodeAtFirst(self, node_data):
        # Create Node
        New_Node = Node(node_data)

        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            # As StartNodePointer is pointing to Nothing
            # Now it will point to created Node
            self.StartNodePointer = New_Node
        else:
            New_Node.NextNodePointer = self.StartNodePointer # New Node will point to Existing First Node which is pointed by StartNodePointer
            self.StartNodePointer = New_Node # NextNodePointer will be pointing to New Node. It become the First One

    # Add a node after a particular node in Linked List
    def addNodeAfterANode(self, node_data_to_be_added, after_node_data):
        # Create Node
        New_Node = Node(node_data_to_be_added)

        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            print("Linked List is Empty")
        else:
            # Search that particular node which contains that particular data
            tempNodePointer = self.StartNodePointer # Create a Temporary pointer, Using this will traverse List

            while tempNodePointer != None: # Till Last Node Traversal will be
                if tempNodePointer.NodeData == after_node_data:
                    # That Particular Node found
                    New_Node.NextNodePointer = tempNodePointer.NextNodePointer # New Node will point to Next Node which was pointed by that Particular Node (which found)
                    tempNodePointer.NextNodePointer = New_Node # That Particular founded node will point to New Node
                    return
                tempNodePointer = tempNodePointer.NextNodePointer
            # All Node Traversed. Data Not Found
            print(f"{after_node_data} doesn't exist in Linked List")

    # Delete First Node from Linked List
    def deleteFirstNode(self):
        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            print("Linked List is Empty")
        else:
            tempNodePointer = self.StartNodePointer  # Point to the First Node by a temporary pointer
            self.StartNodePointer = tempNodePointer.NextNodePointer  # Start will point to Second Node
            del tempNodePointer  # First Node deleted. Second Node become First Node

    # Delete Last Node from Linked List
    def deleteLastNode(self):
        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            print("Linked List is Empty")
        else:
            tempNodePointer = self.StartNodePointer  # Create a Temporary pointer, Using this will traverse List

            # If Linked List contain only one Node
            if tempNodePointer.NextNodePointer == None:
                self.StartNodePointer = None # Start Pointer will point to Nothing
                del tempNodePointer # Delete First Node
            else:
                while tempNodePointer.NextNodePointer.NextNodePointer != None:  # Temporary Pointer will point to Second Last Node
                    tempNodePointer = tempNodePointer.NextNodePointer

                del tempNodePointer.NextNodePointer  # Delete Last Node
                tempNodePointer.NextNodePointer = None  # Second Last Node points to None and Become Last Node

    #  Delete a Particular node. Will identify through Node Data
    def deleteParticularNode(self, node_data_to_be_deleted):
        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            print("Linked List is Empty")
        else:
            tempNodePointer = self.StartNodePointer  # Create a Temporary pointer, Using this will traverse List

            # If Linked List contain only one Node
            if tempNodePointer.NextNodePointer == None:
                if tempNodePointer.NodeData == node_data_to_be_deleted: # That Particular Node found
                    self.StartNodePointer = None # Start Pointer will point to Nothing
                    del tempNodePointer # Delete First Node
                else:
                    print(f"{node_data_to_be_deleted} doesn't exist in linked List")
            else:
                # If First Node is that Particular Node
                if tempNodePointer.NodeData == node_data_to_be_deleted:
                    self.StartNodePointer = tempNodePointer.NextNodePointer  # Start will point to Second Node
                    del tempNodePointer  # First Node deleted. Second Node become First Node
                else:
                    # Check for Rest of the Nodes
                    while tempNodePointer.NextNodePointer.NextNodePointer != None:  # Temporary Pointer will point to Second Last Node
                        if tempNodePointer.NextNodePointer.NodeData == node_data_to_be_deleted: # Found that Particular Node
                            NodeToBeDeleted = tempNodePointer.NextNodePointer # Create another Temporary pointer which points to that Particular Node
                            tempNodePointer.NextNodePointer = tempNodePointer.NextNodePointer.NextNodePointer # Previous Node of need to be deleted Node will point to that Node which is pointed by Node to be deleted
                            del NodeToBeDeleted
                            return
                        tempNodePointer = tempNodePointer.NextNodePointer

                    # After this while loop Temporary Pointer will point to Second Last Node
                    if tempNodePointer.NextNodePointer.NodeData == node_data_to_be_deleted:  # Data found in Last Node
                        LastNode = tempNodePointer.NextNodePointer  # Create a pointer which points to Last Node
                        tempNodePointer.NextNodePointer = None  # Second Last Node will point to Nothing
                        del LastNode
                        return

                    print(f"{node_data_to_be_deleted} doesn't exist in linked List")

    # Reverse the Linked List
    def reverseLinkedList(self):
        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            print("Linked List is Empty")
        else:
            FirstNode = self.StartNodePointer # Pointer for First Node

            # If List contain only one node
            if FirstNode.NextNodePointer == None:
                print("Linked list contain only One data")
            else:
                SecondNode = FirstNode.NextNodePointer # Pointer for Second Node
                ThirdNode = SecondNode.NextNodePointer # Pointer for Third Node

                FirstNode.NextNodePointer = None
                SecondNode.NextNodePointer = FirstNode

                while ThirdNode != None:
                    FirstNode = SecondNode
                    SecondNode = ThirdNode
                    ThirdNode = ThirdNode.NextNodePointer
                    SecondNode.NextNodePointer = FirstNode

                self.StartNodePointer = SecondNode

# Start Single Linked List
SingleLinkedList_object = SingleLinkedList() # StartNodePointer created, pointing to Nothing

while True:
    print("")
    print("Press 1 to add data into Single Linked List")
    print("Press 2 to print Single Linked List")
    print("Press 3 to search data in Single Linked List")
    print("Press 4 to delete data from Single Linked List")
    print("Press 5 to Reverse Single Linked List")
    print("Press 6 to Quit operation")
    print("")

    user_choice = int(input("Enter your choice : ").strip())

    if user_choice == 2:
        SingleLinkedList_object.traverseLinkedList()
    if user_choice == 3:
        data_to_be_searched = int(input("data to be searched : ").strip())
        SingleLinkedList_object.searchDataInLinkedList(data_to_be_searched)
    if user_choice == 5:
        SingleLinkedList_object.reverseLinkedList()
    if user_choice == 1:
        print("Press 1 to add data at last of Single Linked List")
        print("Press 2 to add data at first of Single Linked List")
        print("Press 3 to add data at after any node of Single Linked List")

        user_choice_to_add_data = int(input("Enter your choice to add data : ").strip())

        if user_choice_to_add_data == 1:
            data_to_be_added = int(input("data to be added : ").strip())
            SingleLinkedList_object.addNodeAtLast(data_to_be_added)

        if user_choice_to_add_data == 2:
            data_to_be_added = int(input("data to be added : ").strip())
            SingleLinkedList_object.addNodeAtFirst(data_to_be_added)

        if user_choice_to_add_data == 3:
            data_to_be_added = int(input("data to be added : ").strip())
            data_to_be_added_after_which_data = int(input("data to be added after which data : ").strip())
            SingleLinkedList_object.addNodeAfterANode(data_to_be_added, data_to_be_added_after_which_data)
    if user_choice == 4:
        print("Press 1 to delete First data from Single Linked List")
        print("Press 2 to delete Last data from Single Linked List")
        print("Press 3 to delete Sepecific data from Single Linked List")

        user_choice_to_delete_data = int(input("Enter your choice to delete data : ").strip())

        if user_choice_to_delete_data == 1:
            SingleLinkedList_object.deleteFirstNode()
        if user_choice_to_delete_data == 2:
            SingleLinkedList_object.deleteLastNode()
        if user_choice_to_delete_data == 3:
            data_to_be_deleted = int(input("data to be deleted : ").strip())
            SingleLinkedList_object.deleteParticularNode(data_to_be_deleted)
    if user_choice == 6:
        break