class Animal:
    def __init__(self, name, tail, height):
        self.name = name
        self.tail = tail
        self.height = height

    def __str__(self):
        return f"it's {self.name}"

class Dogs(Animal):
    def __init__(self, name, tail, height, breed, voice):
        super().__init__(name, tail, height)
        self.breed = breed
        self.voice = voice

    def give_paw(self):
        return f'{self.name} дает лапу'

    def __str__(self):
        return f"this dog's name {self.name}"

class Fish(Animal):
    def __init__(self, name, tail, height, water, color):
        super().__init__(name, tail, height)
        self.water = water
        self.color = color

    def swim(self):
        return f'{self.name} swims in {self.water}'

dog = Dogs('Aktos', 'long', 45, 'brown', 'gav')
sazan = Fish('sazan', 'short', 34, 'ocean', 'black')

print(sazan)