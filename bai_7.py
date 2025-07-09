class Skill:
    def __init__(self, name, damge, mana_cost):
        self.name = name
        self.damge = damge
        self.mana_cost = mana_cost

class Player:
    def __init__(self, name, hp):
        self.hp = hp
        self.name = name

    def is_alive(self):
        return self.hp > 0
    
    def take_damge(self, damge):
        self.hp -= damge
        if self.hp < 0:
            self.hp = 0

    def display(self):
        status = 'Lived' if self.is_alive() else 'Failed'
        print(f'Name: {self.name} | HP: {self.hp}')

class Mage(Player):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana
        self.skills = []

    def learn_Skill(self, skill):
        self.skills.append(skill)
    
    def cast(self, enemy, skill_name):
        skill = None
        for s in self.skills:
            if s.name == skill_name:
                skill = s

        if not skill:
            print(f'{self.name} is not skill')
            return
        
        if self.mana < skill.mana_cost:
            print(f'{self.name} is not enough mana')
            return

        if not enemy.name:
            print(f'{enemy.name} is failed ')
            return
        
        self.mana -= skill.mana_cost
        enemy.take_damge(skill.damge)
        print(f'{self.name} use skill {skill.name} attack {enemy.name} make {skill.damge} damged')

fire_ball = Skill('Lua', 40, 20)

player1 = Mage('Phap su', 100, 100)
player2 = Player('Quai', 100)

player1.learn_Skill(fire_ball)

player1.display()
player2.display()

player1.cast(player2, 'Lua')
player2.display()
