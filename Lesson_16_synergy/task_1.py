class CashRegister:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount
    
    def top_up(self, x):
        """Пополнить кассу на X"""
        self.amount += x
    
    def count_1000(self):
        """Сколько целых тысяч осталось в кассе"""
        return self.amount // 1000
    
    def take_away(self, x):
        """Забрать X из кассы"""
        if x > self.amount:
            raise ValueError("Недостаточно денег в кассе")
        self.amount -= x