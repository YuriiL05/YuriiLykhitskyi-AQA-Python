# Створіть класс з описом будь-якої компанії чи організації. Додайте 1 classmethod
class Company:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 10_000

    def get_total_price(self):
        return self.price * self.stock

    @classmethod
    def from_name(cls, name):
        # Get price from DB using name
        return cls(name, 101.5)


magicCompany = Company.from_name('Magic Company')
print(magicCompany.get_total_price())
