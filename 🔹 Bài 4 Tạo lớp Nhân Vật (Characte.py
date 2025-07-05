#🔹 Bài 4: Tạo lớp Nhân Vật (Character)
#Tạo lớp Character cho game:

#Thuộc tính: name, hp, power

#Phương thức:

#attack(enemy) → Giảm HP của enemy bằng power.

#is_alive() → Kiểm tra nếu HP > 0.

#📌 Gợi ý:

#hero = Character("Hiệp sĩ", 100, 20)
#enemy = Character("Quái", 50, 10)

#hero.attack(enemy)
#print(enemy.hp)  # còn 30


#Code

class Character:
    def __init__(self, name, hp, power):
        self.name = name      # tên nhân vật
        self.hp = hp          # máu
        self.power = power    # sức tấn công

    def attack(self, enemy):
        # Kiểm tra nếu enemy còn sống mới cho đánh
        if enemy.is_alive():
            enemy.hp -= self.power
            # Đảm bảo HP không âm
            if enemy.hp < 0:
                enemy.hp = 0
            print(f"{self.name} tấn công {enemy.name} gây {self.power} sát thương!")
        else:
            print(f"{enemy.name} đã bị hạ, không thể tấn công.")

    def is_alive(self):
        return self.hp > 0

    def display(self):
        status = "🟢 Sống" if self.is_alive() else "🔴 Bị hạ"
        print(f"{self.name}: HP = {self.hp}, Power = {self.power} [{status}]")

# Tạo hai nhân vật
hero = Character("Hiệp sĩ", 100, 20)
enemy = Character("Quái", 50, 10)

# Trước trận
hero.display()
enemy.display()

# Hiệp sĩ tấn công quái
hero.attack(enemy)

# Sau đòn đánh
enemy.display()
