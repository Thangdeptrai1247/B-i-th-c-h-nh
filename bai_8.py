class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def attack(self, target):
        if self.is_alive():
            print(f'{self.name} attack {target.name} make {self.damage}')
        else:
            print(f'{self.name} is failed')

    def display(self):
        status = 'Lived' if self.is_alive() else 'Failed'
        print(f'Name: {self.name} | HP: {self.hp}[{status}]')

class Dragon(Monster):
    def __init__(self):
        super().__init__('Rong', hp = 100, damage = 680)  

    def roar(self):
        print('Con rong rao len')

class Slime(Monster):
    def __init__(self):
        super().__init__('Slime', hp = 100, damage = 20)      

    def split(self):
        print('Sime hung du tan cong')  
               
class Player:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def attack(self, enemy):
        print(f'{self.name} attack {enemy.name} make {self.name}')
        enemy.take_damage(self.power)
        
    def display(self):
        status = 'Lived' if self.is_alive() else 'Failed'
        print(f'Name: {self.name} | HP: {self.hp}[{status}]')

hero = Player('Hiep si', 100, 60)
dragon = Dragon()
slime = Slime()

hero.display()
dragon.display()
slime.display()

dragon.roar()

hero.attack(dragon)
dragon.display()

slime.split()

hero.attack(slime)
slime.display()

