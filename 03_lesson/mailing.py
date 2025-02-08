from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.toadd = to_address
        self.fromadd = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.fromadd}" 
                f" в {self.toadd}. Стоимость {self.cost} рублей.")
