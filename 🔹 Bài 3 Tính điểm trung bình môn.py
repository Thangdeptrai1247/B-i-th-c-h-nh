🔹 Bài 3: Tính điểm trung bình môn
Tạo lớp Student với thuộc tính: name và scores (là danh sách điểm).

Thêm phương thức:

average_score() → Tính trung bình các điểm trong danh sách.

is_passed() → Nếu điểm TB >= 5 thì trả về True.

Code

class Student:
    # Hàm khởi tạo (constructor)
    def __init__(self, name, scores):
        self.name = name         # tên học sinh (chuỗi)
        self.scores = scores     # danh sách điểm (list)

    # Tính điểm trung bình
    def average_score(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    # Kiểm tra đậu hay rớt
    def is_passed(self):
        return self.average_score() >= 5

    # In thông tin học sinh
    def display(self):
        print(f"Học sinh: {self.name}")
        print(f"Điểm: {self.scores}")
        print(f"Điểm trung bình: {self.average_score():.2f}")
        if self.is_passed():
            print("Kết quả: Đậu ✅")
        else:
            print("Kết quả: Rớt ❌")


# Tạo đối tượng học sinh
student1 = Student("Nam", [7.5, 4.0, 6.5])

# Gọi các phương thức
student1.display()