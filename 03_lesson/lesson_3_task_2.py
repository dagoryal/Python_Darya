from smartphone import Smartphone

catalog = [
    Smartphone("IPhone", "X", "+7-800-55-35-35"),
    Smartphone("IPhone", "16 ProMax", "+7-999-987-76-54"),
    Smartphone("Samsung", "Galaxy Z", "+7-123-456-78-89"),
    Smartphone("Redmi", "Note 12", "+7-894-756-52-14"),
    Smartphone("Xiaomi", "Redmi A3", "+7-826-765-86-93")
]
for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model}. {Smartphone.number}")