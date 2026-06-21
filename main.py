from models.employees import FullTimeEmployee, PartTimeEmployee, InternEmployee
from features import display_employees, display_salaries


def main():
    employees = [
        FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
        PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
        InternEmployee("E003", "Le Van C", 3000000),
    ]

    while True:
        print("\n=== EMPLOYEE SALARY MANAGER ===")
        print("1. Xem danh sách nhân viên")
        print("2. Tính lương toàn bộ nhân viên")
        print("3. Thoát chương trình")
        print("================================")
        choice = input("Chọn chức năng (1-3): ").strip()

        match choice:
            case "1":
                display_employees(employees)
            case "2":
                display_salaries(employees)
            case "3":
                print("Cảm ơn bạn đã sử dụng Employee Salary Manager!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()