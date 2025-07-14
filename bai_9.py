#🔸 Bài 9: Hệ thống vật phẩm (Inventory)
$Mô tả:

#Tạo lớp Item: name, type (vũ khí, máu, mana), value

#Thêm vào Player một inventory (list Item)

#Thêm phương thức:

#use_item(item_name) → tăng HP hoặc mana tùy vật phẩm

#📌 Gợi ý: giống các hệ thống như trong Pokémon, Genshin, v.v.

class Item:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.inventory = []
        self.weapon = None

    def is_alvie(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def add_item(self, item):
        self.inventory.append(item)
        print(f'{self.name} da trang bi trong balo: {item.name}')

    def  use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                if item.type == 'Health':
                    self.hp += item.value
                    print(f'{self.name} da dung binh mau tang {item.value} HP(Tong: {self.hp} HP)')
                elif item.type == 'Weapon':
                    self.weapon = item
                    print(f'{self.name} da duoc trang bi {item.name}')
                else:
                    print(f'{self.player} chua co vu khi nao')
                self.inventory.remove(item)
                return
        print(f'{self.name} khong co bat ky thu gi')

class Mage(Player):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def  use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                if item.type == 'Health':
                    self.hp += item.value
                    print(f'{self.name} da dung binh mau tang {item.value} HP(Tong: {self.hp} HP)')
                elif item.type == 'Mana':
                    self.hp += item.value
                    print(f'{self.name} da dung binh mau tang {item.value} HP(Tong: {self.mana} mana)')
                elif item.type == 'Weapon':
                    self.weapon = item
                    print(f'{self.name} da duoc trang bi {item.name}')
                else:
                    print(f'{self.player} chua co vu khi nao')
                self.inventory.remove(item)
                return
        print(f'{self.name} khong co bat ky thu gi')

hero = Mage('Phap su', 100, 200)
        
health = Item('Binh mau', 'Health', 40)
mana = Item('Binh mana', 'Mana', 20)
weapon = Item('Kiem', 'Weapon', 60)

hero.add_item(health)
hero.add_item(mana)
hero.add_item(weapon)

hero.use_item('Binh mau')
hero.use_item('Binh mana')
hero.use_item('Kiem')
        
        
