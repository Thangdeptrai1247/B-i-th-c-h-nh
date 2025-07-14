class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Player:
    def __init__(self, name, hp, weapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack(self, enemy):
        print(f'{self.name} dung {self.weapon.name} tan cong {enemy.name} gay {self.weapon.damage}')
        enemy.take_damage(self.weapon.damage)

    def display(self):
        status = 'Song' if self.is_alive() else 'Chet'
        print(f'{self.name} | HP: {self.hp} | Weapon: {self.weapon.name}')

sword = Weapon('Kiem', 60)
axe = Weapon('Riu', 30)

player1 = Player('Hiep si', 100, sword)
player2 = Player('Da xanh', 100, axe)

print('TRan dau bat dau')
player1.display()
player2.display()
print('-'*40)

round_num = 1
while player1.is_alive() and player2.is_alive():
    print(f'\n Vong {round_num}')
    player1.attack(player2)
    if player2.is_alive():
        player2.attack(player1)
    round_num += 1

print('Tran dau ket thuc')

if player1.is_alive():
    print(f'Hiep si da chien thang')
elif player1.is_alive():
    print(f'Da xanh da chien thang')