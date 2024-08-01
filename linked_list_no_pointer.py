class LinkedList:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def append(self, item):
        self.items.append(item)
    def insert_after(self, prev_item, new_item):
        if prev_item in self.items:
            index = self.items.index(prev_item)
            self.items.insert(index + 1, new_item)
        else:
            raise ValueError(f"{prev_item} not found in stack")
    def print_list(self):
        for item in self.items:
            print(item)
def main():
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.push(8)
    linked_list.insert_after(3, 6)
    print("Linked List:")
    linked_list.print_list()
main()