🔸 Bài 6: Tạo hệ thống vũ khí
Lớp Weapon: thuộc tính name, damage

Lớp Player: có name, weapon, hp

Phương thức attack(enemy) → gây sát thương = weapon.damage

Code

class Player:
    def __init__(self, name, weapon, hp):
        self.name = name
        self.weapon = weapon    # Vũ khí là một đối tượng Weapon
        self.hp = hp

    def attack(self, enemy):
        if self.weapon is None:
            print(f"{self.name} không có vũ khí!")
            return

        if not enemy.is_alive():
            print(f"{enemy.name} đã bị hạ, không thể tấn công.")
            return

        # Gây sát thương lên địch
        enemy.hp -= self.weapon.damage
        if enemy.hp < 0:
            enemy.hp = 0

        print(f"{self.name} dùng {self.weapon.name} tấn công {enemy.name} gây {self.weapon.damage} sát thương!")

    def is_alive(self):
        return self.hp > 0

    def display(self):
        status = "🟢 Sống" if self.is_alive() else "🔴 Bị hạ"
        weapon_name = self.weapon.name if self.weapon else "Không có"
        print(f"{self.name} | HP: {self.hp} | Vũ khí: {weapon_name} [{status}]")

sword = Weapon("Kiếm Rồng", 25)
axe = Weapon("Rìu Chiến", 30)

# Tạo người chơi
player1 = Player("Hiệp sĩ", sword, 100)
player2 = Player("Quái vật", axe, 80)

# Hiển thị trước trận
player1.display()
player2.display()

# Tấn công
player1.attack(player2)
player2.attack(player1)

# Hiển thị sau đòn đánh
player1.display()
player2.display()
