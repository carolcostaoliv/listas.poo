class retangulo:
    def __init__(self, b, h):
        self.set_b(b)
        self.set_h(h)
    def set_h (self, v):
        if self.__h < 0: raise ValueError("Altura menor do que 0")
        self.__h = v
    def get_h (self):
        return self.__h
    def set_b (self, v):
        if self.__b < 0: raise ValueError("Altura menor do que 0")
        self.__b = v
    def get_b (self):
        return self.__b
    def calcarea(self):
        return self.__h*self.__b
    def calcdiagonal(self):
        return (self.__b**2+self.__h**2)**0.5
    def __str__(self):
        return f'base: {self.__b} e altura:{self.__h}'
    
x = retangulo(10, 20)

print(x)
print(f'{x.calcdiagonal():.2f}')
print(f'{x.calcarea():.2f}')
    