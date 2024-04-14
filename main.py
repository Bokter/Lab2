class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class parkingSlots:

    def __init__(self, start, end, index, P):
        self.head = None
        self.fillSpaces(start, end, index, P)

    def fillSpaces(self, start, end, index, P):
        for letter in range(ord(end), ord(start) - 1, -1):  # Desde el valor ASCII de end hasta el valor ASCII de start
            for number in range(index, 0, -1):  # Desde index hasta 1
                slot = f"{P}{chr(letter)}{number}"
                newNode = Node(data=slot)
                newNode.next = self.head
                self.head = newNode

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end=", ")
            node = node.next

class Piso:
    def __init__(self, P):
        self.motos = parkingSlots("G", "L", 20, P)
        self.carros = parkingSlots("B", "F", 14, P)
        self.discapacitados = parkingSlots("A", "A", 10, P)

        self.plates = []
        self.slots = []
        self.entryTime = []

        # Lista de vehiculos pq toca hacer 3 listas obligatorias smh

        self.vehicles = []

    def addVehicle(self, vehicle):
        self.plates.append(vehicle.getPlate())
        self.slots.append(vehicle.getSlot())
        self.entryTime.append(vehicle.getTime())

        # Añadir Vehiculo

        self.vehicles.append(vehicle)

class Vehicle:
    def __init__(self, plate, slot, time):
        self.plate = plate
        self.slot = slot
        self.time = time

    def getPlate(self):
        return self.plate

    def getSlot(self):
        return self.slot

    def getTime(self):
        return self.time

# Creacion de pisos

Piso_1 = Piso("P1")
Piso_2 = Piso("P2")
Piso_3 = Piso("P3")

# Pisos YAY

# print("Piso 1: ")
# Piso_1.discapacitados.print_list()
# print("")
# Piso_1.carros.print_list()
# print("")
# Piso_1.motos.print_list()

def searchVehicle(plate):
    encontrado = False
    if len(Piso_1.plates)+len(Piso_2.plates)+len(Piso_3.plates) == 0:
        return "Las listas estan vacias"
    else:
        for i in range(len(Piso_1.plates)):
            if Piso_1.plates[i] == plate:
                encontrado = True
                a = Piso_1.slots[i]
        for i in range(len(Piso_2.plates)):
            if Piso_2.plates[i] == plate:
                encontrado = True
                a = Piso_2.slots[i]
        for i in range(len(Piso_3.plates)):
            if Piso_3.plates[i] == plate:
                encontrado = True
                a = Piso_3.slots[i]

    if encontrado:
       return True
    else:
       return False

# Por Optimizar
def addVehicle(plate, slot, time, piso):

    if searchVehicle(plate) == False: # Si no se encontro el vehiculo, significa que no esta repetido GG WP
        if piso == 1:
            Piso_1.addPlates(plate, slot, time)
        elif piso == 2:
            Piso_2.addPlates(plate, slot, time)
        elif piso == 3:
            Piso_3.addPlates(plate, slot, time)
    else:
        return "Vehiculo repetido"

# def montoPago(plate):

    # Lo hago mañana jijijija



