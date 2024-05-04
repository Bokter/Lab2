class Piso:

    def __init__(self, P):

        # Listas de vehiculos DISPONIBLES.

        self.motos = []
        self.carros = []
        self.discapacitados = []

        self.fillSpaces(P)

        self.plates = []
        self.slots = []
        self.entryTime = []
        self.VType = []

        self.vehicles = []

    def fillSpaces(self, P):

        # Para motos (de "G1" a "L20", incrementando de 20 en 20)
        for letter in range(ord("G"), ord("L")+1):
            for i in range(1, 21):
                self.motos.append(f"{P}{chr(letter)}{i}")

        # Para carros (de "B1" a "F16", incrementando de 16 en 16)
        for letter in range(ord("B"), ord("F")+1):
            for i in range(1, 17):
                self.carros.append(f"{P}{chr(letter)}{i}")

        # Para discapacitados (de "A1" a "A10", incrementando de 10 en 10)
        for i in range(1, 11):
            self.discapacitados.append(f"{P}A{i}")

        print("Motos:", self.motos)
        print("Carros:", self.carros)
        print("Discapacitados:", self.discapacitados)

    def addVehicle(self, vehicle):

      enc = False

      # Si la placa del vehiculo se encuentra repetida
      for i in self.plates:
        if vehicle.getPlate() == i:
          print("Placa repetida")
          return

      # Si el slot que ocupa se encuentra ya en uso
      for i in self.slots:
        if vehicle.getSlot() == i:
          print("Parqueadero ya ocupado")
          return

      if vehicle.getVType() == "M":  # Para motos
          for i in self.motos:
              if i == vehiculo.getSlot():
                slot_available = True
      elif vehicle.getVType() == "C":  # Para carros
          for i in self.carros:
              if i == vehiculo.getSlot():
                  slot_available = True
      elif vehicle.getVType() == "D":  # Para discapacitados
          for i in self.discapacitados:
              if i == vehiculo.getSlot():
                  slot_available = True

      if slot_available:
          if vehicle.getSlot() not in self.slots:
              self.plates.append(vehicle.getPlate())
              self.slots.append(vehicle.getSlot())
              self.entryTime.append(vehicle.getTime())
              self.VType.append(vehicle.getVType())

              self.vehicles.append(vehicle)
              print("Vehiculo añadido exitosamente.")
          else:
              print("Lugar ocupado. Intentando asignar a otro lugar...")
              # Aquí podrías implementar la lógica para encontrar una ubicación de estacionamiento alternativa
      else:
          print("Lugar no disponible.")



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
# Piso_2 = Piso("P2")
# Piso_3 = Piso("P3")

# Para la creacion de vehiculos, se necesita PLATE, SLOT, TIME Y TYPE

# Tipos: Moto, Carro, Discapacitados


vehiculo = Vehicle("ABM650", "P1B1", "10:30", "C")
Piso_1.addVehicle(vehiculo)

cogoyocar = Vehicle("ABM650", "P1B2", "10:30", "C")
Piso_1.addVehicle(cogoyocar)

# Piso_1.clearVehicle("ABM650","9:30")

juepuchacar = Vehicle("GTZ200", "P1B1", "10:30", "C")
Piso_1.addVehicle(juepuchacar)


