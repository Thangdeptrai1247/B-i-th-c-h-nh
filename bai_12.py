class Skill:
    def __init__(self, name, damage, mana_cost, level_required):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.level_required = level_required

class Mage:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.max_hp = self.hp
        self.mana = mana
        self.max_mana = self.mana
        self.level = 1
        self.exp = 0
        self.exp_to_level_up = 50
        self.skills = []

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
        for skill in self.skills:
            skill.damage += 5
        self.max_hp += 20
        self.hp = self.max_hp
        self.max_mana += 20
        self.mana += self.max_mana
        print(f'{self.name} da duoc thang len cap {self.level}')
        print(f'HP: {self.max_hp} | Mana: {self.max_mana}')

    def  gain_exp(self, amount):
        self.exp += amount
        print(f'{self.name} duoc nhan {amount}({self.exp}/{self.exp_to_level_up} EXP)')
        if self.exp >= self.exp_to_level_up:
            self.level_up()

    def cast(self, enemy, skill):
        if self.exp < skill.level_required:
            print(f'{self.name} ko du cap de dung {skill.name}(Yeu cau {skill.level_required} EXP)')
            return
        if self.mana < skill.mana_cost:
            print(f'{self.name} khong du mana')
            return
        enemy.take_damage(skill.damage)
        self.mana -= skill.mana_cost

    def attack(self, enemy):
        if not self.is_alive():
            print(f'{self.name} da bi danh bai')
            return
        print(f'{self.name}  tan cong {enemy.name} gay 10 sat thuong')
        enemy.take_damage(10)
        self.gain_exp(20)

    def display(self):
        status = 'Song' if self.is_alive()  else 'Chet'
        print(f'Name: {self.name} | HP: {self.hp} | Mana: {self.mana}[{status}]')

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
    
    def display(self):
        status = 'Song' if self.is_alive()  else 'Chet'
        print(f'Name: {self.name} | HP: {self.hp}[{status}]')

fire_ball = Skill('Cau lua', 60, 40, 3)
lighting = Skill('Anh sang', 40, 20, 2)

mage = Mage('Phap su', 100, 200)
enemy = Enemy('Da xanh', 100)

mage.skills.append(fire_ball)
mage.skills.append(lighting)

for i in range(5):
    if mage.level >= 3:
        mage.cast(enemy, fire_ball)
    elif mage.level >= 2:
        mage.cast(enemy, lighting)
    else:
        enemy.take_damage(10)
    print('Tran dau bat dau')
    print(f'\n Vong {i+1}')
    mage.attack(enemy)
    if not enemy.is_alive():
        break

        
        
        