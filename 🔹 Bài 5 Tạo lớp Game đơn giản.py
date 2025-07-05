🔹 Bài 5: Tạo lớp Game đơn giản
Tạo lớp Game:

Thuộc tính: player và level

Phương thức:

level_up() → tăng level lên 1

show_status() → in thông tin người chơi


Code

class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

class Game:
    def __init__(self, player):
        self.player = player
        self.level = 1

    def level_up(self):
        self.level += 1
        self.player.power += 5
    
    def shoow_status(self):
        print(f'Người chơi {self.player.name}')
        print(f'Level hiện tại {self.level} ')
        print(f'HP: {self.player.hp}')
        print(f'Power: {self.player.power}')

g1 = Character('Hiệp sĩ rồng', 100, 20)

game = Game(g1)
game.shoow_status()
game.level_up()
game.level_up()
game.shoow_status()

