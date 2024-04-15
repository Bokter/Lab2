import datetime
import time

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
        self.carros = parkingSlots("B", "F", 16, P)
        self.discapacitados = parkingSlots("A", "A", 10, P)

        self.plates = []
        self.slots = []
        self.entryTime = []
        self.type = []

        # Lista de vehiculos pq toca hacer 3 listas obligatorias smh

        self.vehicles = []

    def addVehicle(self, vehicle):
        self.plates.append(vehicle.getPlate())
        self.slots.append(vehicle.getSlot())
        self.entryTime.append(vehicle.getTime())
        self.type.append(vehicle.getType())

        # La misma vaina

        self.vehicles.append(vehicle)

    def findVehicle(self, plate): # Se busca el vehiculo en el piso
        for vehicle in self.vehicles:
            if vehicle.getPlate() == plate:
                return vehicle
        return False

    def removeVehicle(self, plate): # Con la placa eliminas el vehiculo del piso
        for vehicle in self.vehicles:
            if vehicle.getPlate() == plate:
                self.vehicles.remove(vehicle)

    def clearVehicle(self, plate, time):
        vehicle = self.findVehicle(plate)
        if vehicle:
            entry_time = vehicle.getTime().split(":")
            exit_time = time.split(":")
            entry_seconds = int(entry_time[0]) * 3600 + int(entry_time[1]) * 60
            exit_seconds = int(exit_time[0]) * 3600 + int(exit_time[1]) * 60
            duration = exit_seconds - entry_seconds

            hours_parked = duration / 3600
            fee = hours_parked * 2000
            self.removeVehicle(plate)
            return fee
        else:
            return None

class Vehicle:

    # Tiempo del vehiculo evaluado de 00:00 hasta 23:59

    def __init__(self, plate, slot, time, type):
        self.plate = plate
        self.slot = slot
        self.time = time
        self.type = type

    def getPlate(self):
        return self.plate

    def getSlot(self):
        return self.slot

    def getTime(self):
        return self.time

    def getType(self):
        return self.type

# Creacion de pisos

Piso_1 = Piso("P1")
Piso_2 = Piso("P2")
Piso_3 = Piso("P3")

# Para la creacion de vehiculos, se necesita PLATE, SLOT, TIME Y TYPE

# Tipos: Moto, Carro, Discapacitados


vehiculo = Vehicle("ABM650", "P1B1", "10:30", "M")
Piso_1.addVehicle(vehiculo)

print("Se tiene que pagar: ", Piso_1.clearVehicle("ABM650", "13:30"))











