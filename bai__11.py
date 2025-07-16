class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Player:
    def __init__(self, name, hp, weapon):
        self.name = name
        self.hp = hp
        self.max_hp = self.hp
        self.weapon = weapon 
        self.level = 1
        self.exp = 0
        self.exp_to_level_up = 50

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def level_up(self):
        self.level += 1
        self.exp = 0 
        self.exp_to_level_up += 20
        self.max_hp += 20
        self.max_hp = self.hp
        self.weapon.damage += 5
        print(f'{self.name} da duoc thang cap')
        print(f'HP:  {self.hp} | Damage: {self.weapon.damage}')

    def gain_exp(self, amount):
        self.exp += amount
        print(f'{self.name} nhan {amount} EXP({self.exp}/{self.exp_to_level_up})')
        if self.exp >= self.exp_to_level_up:
            self.level_up()

    def attack(self, enemy):
        if not self.is_alive():
            print(f'{self.name} da bi danh bai')
        print(f'{self.name}  dung {self.weapon.name} tan cong {enemy.name} gay {self.weapon.damage}% sat thuong')       
        enemy.take_damage(self.weapon.damage)
        self.gain_exp(30)
        
    def display(self):
        status = 'Song' if  self.is_alive() else ' Chet'
        print(f'Name: {self.name} | HP: {self.max_hp} | Weapon: {self.weapon.name} | EXP: {self.exp}/{self.exp_to_level_up}[{status}]')
        
class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
sword = Weapon('Kiem', 60)

player1 = Player('Hiep si', 100, sword)

slime = Enemy('Slime', 100)

round_num = 1
while slime.is_alive():
    print('Tran dau bat dau')
    print(f'\n Vong {round_num}')
    player1.attack(slime)
    player1.display()
    round_num += 1

