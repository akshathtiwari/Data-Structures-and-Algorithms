class DoubleListNode:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def count_length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def insertAtBeginning(self, data):
        # call insert function with pos = 0
        self.insert(data, 0)

    def insertAtEnd(self, data):
        len = self.count_length()
        print(len)

        if len == 0:
            self.insertAtBeginning(data)
            return

        self.insert(data, len)

    def deleteAtBeginning(self):
        self.delete(0)

    def deleteAtEnd(self):
        len = self.count_length()

        if len == 0:
            self.deleteAtBeginning()
            return

        self.delete(len - 1)

    def insert(self, data, pos):
        dd_node = DoubleListNode(data)

        if pos == 0:

            if self.head is None:
                self.head = dd_node
                self.tail = dd_node
                self.length = 1
                return
            
            else:
                next = self.head
                dd_node.next = next
                next.prev = dd_node
                self.head = dd_node
                self.length += 1
                return

        if self.head is None:
            return

        temp = self.head
        counter = 0

        while temp is not None and counter != pos:
            prev = temp
            temp = temp.next
            counter += 1

        if temp is None:
            if counter < pos:
                print("Index not present")
                return

            if counter == pos:
                prev.next = dd_node
                dd_node.prev = prev
                self.tail = dd_node
                self.length += 1
                return

        # insertion logic with pointers
        # prev = temp.prev
        prev.next = dd_node
        dd_node.prev = prev
        dd_node.next = temp
        temp.prev = dd_node
        self.length += 1

    def delete(self, pos):
        print(f"pos: {pos}")
        if self.head is None:
            return

        temp = self.head

        if pos == 0:
            if temp.next is None:
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                next = temp.next
                temp.next = None
                next.prev = None
                self.head = next
                self.length -= 1
            return

        counter = 0

        # loop to make the counter reach the pos without None attr error

        while temp is not None and counter != pos:
            prev = temp
            temp = temp.next
            # print(temp.data)
            counter += 1

        if temp.next is None and counter == pos:
            print("last node removal case")
            prev = temp.prev
            prev.next = None
            temp.prev = None
            temp.next = None
            self.tail = prev
            self.length -= 1
            return

        if temp is None:

            if pos > counter:
                print("index out of range")
                return

        prev = temp.prev
        next = temp.next
        prev.next = next
        next.prev = prev
        temp.prev = None
        temp.next = None
        self.length -= 1
        return

    def traverse(self):
        if self.head is None:
            return
        temp = self.head

        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next

        print("None")

    def dedup(self):
        if self.head is None:
            return

        temp = self.head

        if temp.next is None:   # only one element return as is
            return

        temp_idx = 0

        while temp:
            current = temp.next
            current_idx = temp_idx + 1

            while current:
                if temp.data == current.data:
                    # print(f"temp: {temp.data}, idx {temp_idx}")
                    # print(f"current: {current.data}, idx {current_idx}")
                    self.traverse()
                    # print(f"to delete: {current_idx}")
                    self.delete(current_idx)

                    self.traverse()
                else:
                    pass
                current_idx += 1
                current = current.next

            temp_idx += 1
            temp = temp.next

    def dedup_sorted(self):


        pass


if __name__ == "__main__":

    # problem -1

    input_list = [1, 1, 1]
    dll = DoublyLinkedList()

    for val in input_list:
        dll.insertAtEnd(val)

    dll.traverse()
    print(f"length before dedup: {dll.length}")
    dll.dedup()
    print(f"length after dedup: {dll.length}")
    dll.traverse()