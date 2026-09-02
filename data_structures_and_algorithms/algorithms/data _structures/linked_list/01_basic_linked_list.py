class Node:
    """Represent a node in a singly linked list."""
    
    def __init__(self, data: str) -> None:
        """Initialize a node with data and no next node."""
        self.data = data
        self.next = None
        

class LinkedList:
    """Represent a basic singly linked list."""
    
    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.head = None
    
    def append(self, data: str) -> None:
        """Append a new node containing data to the end of the list."""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
            
        current.next = new_node
        
    def display(self) -> None:
        """Print all node values in the linked list."""
        current = self.head
        
        while current is not None:
            print(current.data)
            current = current.next
            
if __name__ == "__main__":
    
    students = LinkedList()
    
    students.append("behruz")
    students.append("mahmut")
    students.append("nuriya")
    
    students.display()