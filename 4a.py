class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        print(f"{data} inserted at the beginning.")

    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(f"{data} inserted at the end.")

    
    def delete_begin(self):
        if self.head is None:
            print("List is empty.")
            return

        print(f"{self.head.data} deleted from the beginning.")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    
    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        if temp.next is None:
            print(f"{temp.data} deleted.")
            self.head = None
            return

        while temp.next:
            temp = temp.next

        print(f"{temp.data} deleted from the end.")
        temp.prev.next = None

    
    def display_forward(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        print("Forward:", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    
    def display_backward(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        print("Backward:", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")



dll = DoublyLinkedList()

while True:
    print("\n----- Doubly Linked List Menu -----")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Delete from End")
    print("5. Display Forward")
    print("6. Display Backward")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter data: ")
        dll.insert_begin(data)

    elif choice == 2:
        data = input("Enter data: ")
        dll.insert_end(data)

    elif choice == 3:
        dll.delete_begin()

    elif choice == 4:
        dll.delete_end()

    elif choice == 5:
        dll.display_forward()

    elif choice == 6:
        dll.display_backward()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
