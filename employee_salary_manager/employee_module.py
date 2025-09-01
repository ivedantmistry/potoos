# employee_module.py

class Employee:
    """Represents a single employee and their salary details."""
    def __init__(self, emp_id: int, name: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.salary = float(salary)
        self.bonus = 0.0

    def apply_bonus(self, percentage: float) -> float:
        """
        Calculates the bonus, adds it to the employee's record,
        and returns the new total salary.
        """
        bonus_amount = self.salary * (percentage / 100)
        self.bonus = bonus_amount
        final_salary = self.salary + self.bonus
        return final_salary

    def __repr__(self):
        """A developer-friendly representation of the Employee object."""
        return f"Employee(id={self.emp_id}, name='{self.name}', salary={self.salary})"