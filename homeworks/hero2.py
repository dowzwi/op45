class SuperHero:
    people = 'people'  # Свойство класса

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"{self.nickname} with power {self.superpower} has {self.health_points} health points"

    def __len__(self):
        return len(self.catchphrase)

# Создание объекта класса SuperHero
hero = SuperHero("Bruce Wayne", "Batman", "Stealth", 100, "I am the night")

# Применение методов
print(hero.get_name())  # Вывод имени героя
hero.double_health()   # Умножение здоровья героя на 2
print(hero)            # Вывод информации о герое с использованием __str__
print(len(hero))       # Вывод длины коронной фразы с использованием __len__
