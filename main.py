import random


# Класс героя
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Атака другого героя, уменьшая его здоровье."""
        if self.is_alive():
            other.health -= self.attack_power
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")
        else:
            print(f"{self.name} слишком слаб для атаки.")

    def is_alive(self):
        """Проверка, жив ли герой."""
        return self.health > 0


# Класс игры
class Game:
    def __init__(self, player_name, computer_name="Computer"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        """Основной цикл игры."""
        print("Игра начинается!")
        print(f"{self.player.name} VS {self.computer.name}\n")

        while self.player.is_alive() and self.computer.is_alive():
            # Случайный выбор, кто атакует первым
            if random.choice([True, False]):
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            # Печать текущего состояния
            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}\n")

        # Определение победителя
        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")

game = Game("Игрок")
game.start()
