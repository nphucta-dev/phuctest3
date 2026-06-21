def display_employees(employees):
    """
    Duyệt danh sách và gọi display_info() của từng nhân viên.
    Polymorphism: display_info() đọc employee_type từ class attribute của lớp con.
    """
    print("\n--- DANH SÁCH NHÂN VIÊN ---")
    for emp in employees:
        emp.display_info()