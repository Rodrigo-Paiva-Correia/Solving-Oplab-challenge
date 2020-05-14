class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, element):  # Add new element
        if self.head is not None:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.head = Node(element)
        self._size += 1

    def index(self, element):  # Obtains the element index.
        pointer = self.head
        index = 0
        while pointer is not None:
            if pointer.data == element:
                return index
            pointer = pointer.next
            index += 1
        raise ValueError(f'{element} is not in list')

    def insert(self, index, element):  # Insert an element at a specific position in the list.
        global previous_pointer
        node = Node(element)
        index = index if index > -1 else (self._size + 1 + index)

        if(index == 0) or (self.head is None):
            node.next = self.head
            self.head = node
            self._size += 1
        else:
            pointer = self.head
            for i in range(index):
                previous_pointer = pointer
                pointer = pointer.next
                if pointer is None:
                    break
            node.next = pointer
            previous_pointer.next = node

            self._size += 1

    def remove(self, element):  # Remove a element of the list
        if self.head is None:
            raise ValueError(f'{element} is not in list')
        elif self.head.data is element:
            self.head = self.head.next
            self._size -= 1
        else:
            previous_pointer = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == element:
                    previous_pointer.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                previous_pointer = pointer
                pointer = pointer.next

    def __getitem__(self, index):  # Add new element
        pointer = self.head
        index = index if index > -1 else (self._size + index)

        for i in range(index):
            if pointer is not None:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        if pointer is not None:
            return pointer.data
        raise IndexError('list index out of range')

    def __setitem__(self, index, element):  # Set a list element.
        pointer = self.head
        index = index if index > -1 else (self._size + index)

        for i in range(index):
            if pointer is not None:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        if pointer is not None:
            pointer.data = element
        else:
            raise IndexError('list index out of range')

    def __repr__(self):  # Representation of list
        representation = '['
        pointer = self.head
        while pointer.next:
            representation += str(pointer.data) + ', '
            pointer = pointer.next
        representation += str(pointer.data) + ']'
        return representation

    def __str__(self):
        return self.__repr__()

    def __len__(self):  # Obtains the size list.
        return self._size


if __name__ == '__main__':

    list_01 = LinkedList()  # Creating a linked list.

    stuffs = ['a', 1, True, None]

    for stuff in stuffs:
        list_01.append(stuff)

    list_01.insert(-1, 'a')  # Add the number 4 to the end of the list.

    print(f'size list -> {len(list_01)}')
    print(f'element "None" index -> {list_01.index(None)}')
    print(list_01)
