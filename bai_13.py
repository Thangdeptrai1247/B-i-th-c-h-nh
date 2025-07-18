class Quest:
    def __init__(self, name, description, required_skill, reward_exp):
        self.name = name
        self.description = description
        self.required_skill = required_skill
        self.reward_exp = reward_exp
        self.current_skill = 0
        self.completed = False
        

    def check_process(self):
        return f'{self.current_skill}/{self.required_skill} quai bi danh bai'
    
    def is_completed(self):
        return self.completed
    
class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.exp_to_level_up = 50
        self.quests = []

    def gain_exp(self,  amount):
        self.exp += amount
        print(f'{self.name} nhan {amount} EXP({self.exp}/{self.exp_to_level_up} EXP)')
        if self.exp >= self.exp_to_level_up:
            self.level += 1
            self.exp = 0
            self.exp_to_level_up += 20

    def accept_quest(self, quest):
        self.quests.append(quest)
        print(f'{self.name} nhan nhiem vu: {quest.name}')

    def killl_enemy(self):
        print(f'{self.name} da danh bai 1 quai')
        for quest in self.quests:
            if not quest.completed:
                quest.current_skill += 1
                print(f'Tien do nhiem vu: {quest.name} {quest.check_process()}')
                if quest.current_skill  >=  quest.required_skill:
                    quest.completed = True
                    self.gain_exp(quest.reward_exp)
                    print(f'Hoan thanh nhiem vu: {quest.name}')

q1 = Quest('Danh slime', 'Tien 3 con slime len duong', required_skill= 3, reward_exp= 30)

player1 = Player('Hiep si')

player1.accept_quest(q1)
        
for i in range(3):
    print(f'\n Vong {i+1}')
    player1.killl_enemy()

        