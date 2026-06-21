from abc import ABC, abstractmethod


class Employee(ABC):
    """
    Lớp cha trừu tượng đại diện cho nhân viên nói chung.
    Không thể khởi tạo trực tiếp Employee(...).
    Mọi lớp con BẮT BUỘC override calculate_salary().
    """

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        """In thông tin cơ bản. Lấy loại từ class attribute của lớp con."""
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: {self.employee_type}")

    @abstractmethod
    def calculate_salary(self):
        """
        Abstract Method — Polymorphism:
        Mỗi loại nhân viên tự định nghĩa công thức tính lương riêng.
        """
        pass