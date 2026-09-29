class Resident:
    def __init__(self, Resident_Name, Flat_Number, Maintenance_Fee):
        self.Resident_Name = Resident_Name
        self.Flat_Number = Flat_Number
        self.Maintenance_Fee = Maintenance_Fee

    def get_status(self):
        if self.Maintenance_Fee >= 1:
            return "Paid"
        else:
            return "Pending"

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.Resident_Name} | {self.Flat_Number} | {self.Maintenance_Fee} | {self.get_status()}"


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)

    def display_all(self):
        for resident in self.residents:
            print(resident)


n = int(input())

society = Society()

for _ in range(n):
    data = input().split(",")

    name = data[0]
    flat_number = data[1]
    maintenance_fee = int(data[2])

    resident = Resident(name, flat_number, maintenance_fee)
    society.add_resident(resident)

society.display_all()