from models.employee import Employee


class FullTimeEmployee(Employee):
    """
    Nhân viên toàn thời gian.
    Lương = base_salary + bonus.
    """

    employee_type = "Full-time"

    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        """Polymorphism: công thức riêng của Full-time."""
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    """
    Nhân viên bán thời gian.
    Lương = working_hours * hourly_rate.
    """

    employee_type = "Part-time"

    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        """Polymorphism: công thức riêng của Part-time."""
        return self.working_hours * self.hourly_rate


class InternEmployee(Employee):
    """
    Thực tập sinh.
    Lương = allowance (trợ cấp).
    """

    employee_type = "Intern"

    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance

    def calculate_salary(self):
        """Polymorphism: công thức riêng của Intern."""
        return self.allowance