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
        
    def push(self, new_data):
        """Insert a new node at the beginning of the linked list."""
        
        # create a new node
        new_node = Node(new_data)
        
        new_node.next = self.head
        
        self.head = new_node
        
    def insert_after(self, prev_node, new_data):
        """Insert a new node containing data after the specified node."""
        
        if prev_node is None:
            print("\nNode not found")
            return
            
        new_node = Node(new_data)
        
        new_node.next = prev_node.next
        
        prev_node.next = new_node
    
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
        
    def delete_node(self, key):
        """Remove the first node containing the specified value."""
        
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        
        while temp:
            if temp.data == key:
                break
            
            prev = temp
            temp = temp.next
            
        if temp is None:
            return
        
        prev.next = temp.next
        temp = None
        
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
    students.append("ali")
    
    students.push("anvar")
    students.insert_after(students.head, "zamira")
    students.delete_node("ali")
    
    students.display()