def display_salaries(employees):
    """
    Tính và hiển thị lương toàn bộ nhân viên.

    Polymorphism thuần túy: gọi calculate_salary() đồng nhất trên mọi loại nhân viên.
    KHÔNG dùng if/elif/match-case để phân loại — Python tự dispatch đúng công thức.
    """
    print("\n--- BẢNG LƯƠNG NHÂN VIÊN ---")
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"{emp.employee_id} | {emp.name:<15}| Lương: {salary:,.0f} VND")