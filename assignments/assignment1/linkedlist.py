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
        # length is maintained by insert and delete so no traversal is needed here
        length = self.length

        if length == 0:
            self.insertAtBeginning(data)
            return

        self.insert(data, length)

    def deleteAtBeginning(self):
        self.delete(0)

    def deleteAtEnd(self):
        # length is maintained by insert and delete so no traversal is needed here
        length = self.length

        if length == 0:
            self.deleteAtBeginning()
            return

        self.delete(length - 1)

    def insert(self, data, pos):
        dd_node = DoubleListNode(data)

        if pos == 0: #

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

        # pos 0 on an empty list returned above, so reaching here with an empty
        # list means pos was greater than 0 which is not a valid position
        if self.head is None:
            print("Index not present")
            return

        # appending at the end is O(1) because tail is maintained,
        # pos 0 already returned above so length is at least 1 here
        if pos == self.length:
            prev = self.tail
            prev.next = dd_node
            dd_node.prev = prev
            self.tail = dd_node
            self.length += 1
            return

        temp = self.head
        counter = 0

        while temp is not None and counter != pos:
            prev = temp
            temp = temp.next
            counter += 1

        # the loop can only end with temp as None by running off the end, and pos == length is already handled by the tail branch above, so anything landing here is not a valid position and the list must be left untouched
        if temp is None:
            print("Index not present")
            return

        # insertion logic with pointers
        # prev = temp.prev
        prev.next = dd_node
        dd_node.prev = prev
        dd_node.next = temp
        temp.prev = dd_node
        self.length += 1

    def delete(self, pos):
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

        # removing the last node is O(1) because tail is maintained and its prev
        # is already there, pos 0 returned above so length is at least 2 here
        if pos == self.length - 1:
            temp = self.tail
            prev = temp.prev
            prev.next = None
            temp.prev = None
            self.tail = prev
            self.length -= 1
            return

        counter = 0

        # loop to make the counter reach the pos without None attr error

        while temp is not None and counter != pos:
            prev = temp
            temp = temp.next
            # print(temp.data)
            counter += 1

        # the loop can only end with temp as None by running off the end, and at that point counter holds the length, so pos was never a valid position
        if temp is None:
            print("index out of range")
            return

        # last node case, there is no next node to link back so tail has to move
        if temp.next is None:
            prev = temp.prev
            prev.next = None
            temp.prev = None
            self.tail = prev
            self.length -= 1
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

        # newline so two traversals in a row do not run into each other
        print()

    def search(self, val):
        if self.head is None:
            return -1

        temp = self.head
        idx = 0

        # walk the list and return the position of the first match
        while temp is not None:
            if temp.data == val:
                return idx

            temp = temp.next
            idx += 1

        # -1 because positions start at 0 so it can never be a valid position
        return -1

    def dedup(self):
        if self.head is None:
            return

        t1 = self.head
        if t1.next is None:
            return

        # outer pointer t1 fixes one node, inner pointer t2 scans every node after it
        while t1:
            t2 = t1.next

            while t2:
                if t1.data == t2.data:
                    next = t2.next
                    prev = t2.prev
                    prev.next = next

                    if next is None:
                        # the duplicate was the last node so tail moves back to prev
                        t2.prev = None
                        t2.next = None
                        self.tail = prev
                        self.length -= 1

                    else:
                        # the duplicate was in the middle so prev and next get linked
                        next.prev = prev
                        t2.prev = None
                        t2.next = None
                        self.length -= 1

                    # t2 is unlinked now so carry on from the node that followed it
                    
                    t2 = next

                else:
                    # no match so just move the inner pointer forward
                    t2 = t2.next

            t1 = t1.next

    def unique_sorted(dll1, dll2):
        # both inputs are already sorted without duplicates so a new dll is better to build and maintain
        # no input list is modified in this op
        new_dll = DoublyLinkedList()

        t1 = dll1.head   # walks dll1
        t2 = dll2.head   # walks dll2

        # run till one of the two lists is finished
        while t1 and t2:
            if t1.data < t2.data:
                # t1 is smaller so it goes in and only t1 moves
                new_dll.insertAtEnd(t1.data)
                t1 = t1.next

            elif t1.data > t2.data:
                # t2 is smaller so it goes in and only t2 moves
                new_dll.insertAtEnd(t2.data)
                t2 = t2.next

            else:
                # both are equal so take one copy and move both to keep it unique
                new_dll.insertAtEnd(t1.data)
                t1 = t1.next
                t2 = t2.next

        # whichever list is left over is already sorted and unique so it can just
        # be appended as is, at most one of these two loops will actually run
        while t1:
            new_dll.insertAtEnd(t1.data)
            t1 = t1.next

        while t2:
            new_dll.insertAtEnd(t2.data)
            t2 = t2.next

        return new_dll

if __name__ == "__main__":

    # part 1, list operations

    print("part 1: list operations")
    dll = DoublyLinkedList()

    # insert at a given position, 15 goes in between 10 and 20
    dll.insert(10, 0)
    dll.insert(20, 1)
    dll.insert(30, 2)
    dll.insert(15, 1)
    print("after insert of 10, 20, 30 and then 15 at pos 1")
    dll.traverse()
    print(f"head: {dll.head.data}, tail: {dll.tail.data}, length: {dll.length}")

    # position that does not exist, the list is left untouched
    print("insert at pos 50 on a list of length 4")
    dll.insert(99, 50)
    dll.traverse()

    # search returns the position of the first match, -1 when the value is absent
    print(f"search(20) -> {dll.search(20)}")
    print(f"search(10) -> {dll.search(10)}")
    print(f"search(99) -> {dll.search(99)}")

    # delete at a given position, pos 1 is the 15 that was inserted above
    dll.delete(1)
    print("after delete at pos 1")
    dll.traverse()

    # position that does not exist
    print("delete at pos 50 on a list of length 3")
    dll.delete(50)
    dll.traverse()

    print()
    print("part 1: helper operations")

    # the helpers only call insert and delete, they do not touch pointers themselves
    dll.insertAtBeginning(5)
    dll.insertAtEnd(40)
    print("after insertAtBeginning(5) and insertAtEnd(40)")
    dll.traverse()
    print(f"head: {dll.head.data}, tail: {dll.tail.data}, length: {dll.length}")

    dll.deleteAtBeginning()
    dll.deleteAtEnd()
    print("after deleteAtBeginning() and deleteAtEnd()")
    dll.traverse()
    print(f"head: {dll.head.data}, tail: {dll.tail.data}, length: {dll.length}")

    # deleting everything to show the list goes back to empty cleanly
    dll.deleteAtEnd()
    dll.deleteAtEnd()
    dll.deleteAtEnd()
    print("after deleting every remaining node")
    dll.traverse()
    print(f"head: {dll.head}, tail: {dll.tail}, length: {dll.length}")

    print()
    print("part 2, problem 1: remove duplicates from an unsorted list")

    input_list = [3, 1, 2, 1, 5, 3]
    dll1 = DoublyLinkedList()

    for val in input_list:
        dll1.insertAtEnd(val)

    print(f"input: {input_list}")
    print("list before dedup")
    dll1.traverse()
    print(f"length before dedup: {dll1.length}")

    dll1.dedup()

    print("list after dedup, expected 3 -> 1 -> 2 -> 5")
    dll1.traverse()
    print(f"length after dedup: {dll1.length}")
    print(f"head: {dll1.head.data}, tail: {dll1.tail.data}")

    print()
    print("part 2, problem 2: merge two sorted lists without duplicates")

    input_list_a = [1, 2, 3]
    input_list_b = [2, 5, 7]

    dll_a = DoublyLinkedList()
    dll_b = DoublyLinkedList()

    # both lists are built in sorted order without duplicates, which is the precondition the problem gives

    for val in input_list_a:
        dll_a.insertAtEnd(val)

    for val in input_list_b:
        dll_b.insertAtEnd(val)

    print(f"input: {input_list_a} and {input_list_b}")
    print("list a")
    dll_a.traverse()
    print("list b")
    dll_b.traverse()

    merged = DoublyLinkedList.unique_sorted(dll_a, dll_b)

    print("merged list, expected 1 -> 2 -> 3 -> 5 -> 7")
    merged.traverse()
    print(f"length: {merged.length}")
    print(f"head: {merged.head.data}, tail: {merged.tail.data}")

    # neither input list was modified by the merge
    print("list a after the merge")
    dll_a.traverse()
    print("list b after the merge")
    dll_b.traverse()