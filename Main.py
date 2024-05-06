from Ventana import MainFrame
from tkinter import Tk, messagebox

plates = []
globalVehicles = []

def main():
    root = Tk()
    root.wm_title("ParkEase")
    root.geometry("1280x720")
    root.resizable(False, False)
    root.iconbitmap("icono.ico")
    app = MainFrame(root)
    app.mainloop()


if __name__ == "__main__":
    main()

# Main Code

# Main Code

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
                slot = f"{P}{chr(letter)}{number}"  # Añadir prefijo P1, P2, o P3
                newNode = Node(data=slot)
                newNode.next = self.head
                self.head = newNode

    def verifySlot(self, slot):
        temp = self.head
        while temp:
          if temp.data == slot:
            return True
          temp = temp.next
        return False

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

        self.slots = []
        self.entryTime = []
        self.VType = []

        self.vehicles = []
        self.current = [0,0,0,0,0,0,0,0,0,0,0,0] # Cantidad actual de carros segun el bloque iniciando desde la A - L

    def addVehicle(self, vehicle):

      slot_available = False

      # Si la placa del vehiculo se encuentra repetida
      for i in plates:
          if vehicle.getPlate() == i:
              messagebox.showinfo(title="Agregar Vehiculo",message="El vehiculo no se pudo añadir\nPlaca repetida")
              return

      # Si el slot que ocupa se encuentra ya en uso
      for i in self.slots:
          if vehicle.getSlot() == i:
              messagebox.showinfo(title="Agregar Vehiculo",message="El vehiculo no se pudo añadir\nLugar ya ocupado")
              return


      if vehicle.getVType() == "M":  # Para motos
          slot_available = self.motos.verifySlot(vehicle.getSlot())
      elif vehicle.getVType() == "C":  # Para carros
          slot_available = self.carros.verifySlot(vehicle.getSlot())
      elif vehicle.getVType() == "D":  # Para discapacitados
          slot_available = self.discapacitados.verifySlot(vehicle.getSlot())

      if slot_available:
          if vehicle.getSlot() not in self.slots:
              plates.append(vehicle.getPlate())
              self.slots.append(vehicle.getSlot())
              self.entryTime.append(vehicle.getTime())
              self.VType.append(vehicle.getVType())

              self.vehicles.append(vehicle)
              globalVehicles.append(vehicle)

              return True
          else:
              return False
      else:
          messagebox.showinfo(title="Agregar Vehiculo",
                              message="El vehiculo no se pudo añadir\nLugar no disponible")

    def findVehicle(self, plate): # Se busca el vehiculo en el piso
        for vehicle in self.vehicles:
            if vehicle.getPlate() == plate:
                return vehicle
        return False

    def removeVehicle(self, plate):  # Con la placa eliminas el vehiculo del piso
        i = 0
        for vehicle in self.vehicles:
            if vehicle.getPlate() == plate:
                self.vehicles.remove(vehicle)
                self.slots.remove(i)
                self.entryTime.remove(i)
                self.VType.remove(i)
            i += 1

        for p in plates:
            if p == plate:
                plate.remove(p)

    def clearVehicle(self, plate, time):
        vehicle = self.findVehicle(plate)
        if vehicle:
            entry_time = vehicle.getTime().split(":")
            exit_time = time.split(":")
            entry_seconds = int(entry_time[0]) * 3600 + int(entry_time[1]) * 60
            exit_seconds = int(exit_time[0]) * 3600 + int(exit_time[1]) * 60
            duration = exit_seconds - entry_seconds

            if entry_seconds < exit_seconds:
              hours_parked = duration / 3600
              fee = hours_parked * 2000
              self.removeVehicle(plate)
              return fee
            else:
              return print("Tiempo Invalido")
        else:
            return print("Vehiculo no encontrado")

class Vehicle:

    # Tiempo del vehiculo evaluado de 00:00 hasta 23:59

    def __init__(self, plate, slot, time, vType):
        self.plate = plate
        self.slot = slot
        self.time = time
        self.vType = vType

    def getPlate(self):
        return self.plate

    def getSlot(self):
        return self.slot

    def getTime(self):
        return self.time

    def getVType(self):
        return self.vType

# Creacion de pisos

Piso_1 = Piso("P1")
Piso_2 = Piso("P2")
Piso_3 = Piso("P3")

# Para la creacion de vehiculos, se necesita PLATE, SLOT, TIME Y TYPE

# Tipos: Moto, Carro, Discapacitados / M, C, D

v1= Vehicle("AAA111","P1D1","10:20","C")
v2= Vehicle("BBB222", "P2B2", "12:30","C")
v3= Vehicle("CCC333", "P3G1", "10:05","M")
v4= Vehicle("DDD444", "P1H2", "13:09", "M")
v5= Vehicle("EEE555", "P1A2", "15:15", "D")
v6= Vehicle("FFF666", "P2D3", "23:59", "C")
v7= Vehicle("GGG777", "P3I5", "12:30", "M")
v8= Vehicle("HHH888", "P1K6", "9:30","M")
v9= Vehicle("III999", "P3A9", "6:30", "D")


Piso_1.addVehicle(v1)
Piso_1.addVehicle(v4)
Piso_1.addVehicle(v5)
Piso_1.addVehicle(v8)

Piso_2.addVehicle(v2)
Piso_2.addVehicle(v6)

Piso_3.addVehicle(v3)
Piso_3.addVehicle(v7)
Piso_3.addVehicle(v9)
