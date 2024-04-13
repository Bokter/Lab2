
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class parkingSlots:

    def __init__(self):
        self.head = None

    def fillSpaces(self, space):
        for i in range(space, 0, -1):  # Desde space hasta 1 (inclusive)
            slot = f"A{i}"
            newNode = Node(data=slot)
            newNode.next = self.head
            self.head = newNode

    def print_list(self):
        """Prints all elements in the linked list."""
        node = self.head
        while node is not None:
            print(node.data, end=" -> ")  # Print with an arrow separator
            node = node.next

class Piso:
    def __init__(self):
        self.moto = parkingSlots() # 120
        self.carros = parkingSlots() # 70
        self.discapacitados = parkingSlots() # 10

# Creacion de pisos

Piso_1 = Piso()
Piso_2 = Piso()
Piso_3 = Piso()

Piso_1.moto.fillSpaces(120)
Piso_1.moto.print_list()



