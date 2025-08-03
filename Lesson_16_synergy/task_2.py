class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s  # шаг перемещения
    
    def go_up(self):
        """Увеличивает y на s"""
        self.y += self.s
    
    def go_down(self):
        """Уменьшает y на s"""
        self.y -= self.s
    
    def go_left(self):
        """Уменьшает x на s"""
        self.x -= self.s
    
    def go_right(self):
        """Увеличивает x на s"""
        self.x += self.s
    
    def evolve(self):
        """Увеличивает s на 1"""
        self.s += 1
    
    def degrade(self):
        """Уменьшает s на 1"""
        if self.s <= 1:
            raise ValueError("Шаг не может быть меньше или равен 0")
        self.s -= 1
    
    def count_moves(self, x2, y2):
        """Возвращает минимальное количество действий для достижения (x2, y2)"""
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        # Вычисляем количество шагов для каждой оси
        x_steps = dx // self.s
        x_remainder = dx % self.s
        
        y_steps = dy // self.s
        y_remainder = dy % self.s
        
        # Если есть остаток, потребуется дополнительный шаг
        total_steps = x_steps + y_steps
        if x_remainder > 0:
            total_steps += 1
        if y_remainder > 0:
            total_steps += 1
        
        return total_steps