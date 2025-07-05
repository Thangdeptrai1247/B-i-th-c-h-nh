🔹 Bài 1: Tạo lớp Học Sinh
Viết một lớp Student có các thuộc tính: name, age, grade. Thêm một phương thức introduce() in ra thông tin học sinh.

python
Sao chép
Chỉnh sửa
# Gợi ý kết quả:
# Tôi tên là Nam, 15 tuổi, học lớp 10A1.

Code

class Student:
    # Hàm khởi tạo để gán thuộc tính cho đối tượng
    def __init__(self, name, age, grade):
        self.name = name      # tên học sinh
        self.age = age        # tuổi học sinh
        self.grade = grade    # lớp học hoặc khối lớp

    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f"Tôi tên là {self.name}, {self.age} tuổi, học lớp {self.grade}.")

# Tạo đối tượng học sinh
student1 = Student("Nam", 15, "10A1")
student2 = Student("Linh", 16, "11B")

# Gọi phương thức introduce()
student1.introduce()
student2.introduce()