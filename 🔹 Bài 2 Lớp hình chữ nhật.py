🔹 Bài 2: Lớp hình chữ nhật
Viết lớp Rectangle có thuộc tính width và height.
Thêm phương thức:

area() → Trả về diện tích.

perimeter() → Trả về chu vi.

📌 Gợi ý:

python
Sao chép
Chỉnh sửa
rect = Rectangle(10, 5)
print(rect.area())       # 50
print(rect.perimeter())  # 30

Code

# Bước 1: Định nghĩa lớp Rectangle
class Rectangle:
    # Bước 2: Hàm khởi tạo để gán chiều rộng và chiều cao
    def __init__(self, width, height):
        self.width = width      # thuộc tính chiều rộng
        self.height = height    # thuộc tính chiều cao

    # Bước 3: Phương thức tính diện tích
    def area(self):
        return self.width * self.height

    # Bước 4: Phương thức tính chu vi
    def perimeter(self):
        return 2 * (self.width + self.height)

    # Bổ sung (tùy chọn): In ra hình chữ nhật dễ hiểu
    def display(self):
        print(f"Hình chữ nhật: rộng {self.width}, cao {self.height}")
        print(f"  - Diện tích: {self.area()}")
        print(f"  - Chu vi: {self.perimeter()}")

# Tạo một đối tượng hình chữ nhật
rect1 = Rectangle(10, 5)

# Gọi các phương thức
rect1.display()