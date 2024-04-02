class Status:
    def __init__(self, name: str, health: int, attack_power: int):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    def attack(self, target):
        if target.is_alive() == True:
            target.take_damage = self.__attack_power
            print(f'{self.__name} dealt {self.__attack_power} to {target.__name}')
            print(target.take_damage)
            print(f'{target.__name} health: {target.__health}')
        else:
            print(f'{target.__name} is Already Dead')
        
    @property
    def take_damage(self):
        return self.__health

    @take_damage.setter
    def take_damage(self, total_damage):
        self.__health -= total_damage
        
    def is_alive(self):
        if self.__health > 0:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return f'Name: {self.__name}, Health: {self.__health}, Attack Power: {self.__attack_power}'

class Player(Status):
    def __init__(self, name: str, health: int, attack_power: int):
        super().__init__(name, health, attack_power)


class Enemy(Status):
    def __init__(self, name: str, health: int, attack_power: int):
        super().__init__(name, health, attack_power)


goblin1 = Enemy(name='Lesser Goblin', health= 100, attack_power=5)
player1 = Player(name='Hero', health=100, attack_power=10)

# debugging

print(player1)
print(goblin1)


player1.attack(goblin1)
goblin1.attack(player1)

print(player1)
print(goblin1)
