# salary_utils.py
import requests
from employee_module import Employee

API_BASE_URL = "http://127.0.0.1:5000"


def fetch_employees() -> list[Employee]:
    """
    Fetches the list of employees from the local API.
    Returns a list of Employee objects.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/employees")
        response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)

        employees_data = response.json()

        # Convert the raw dictionary data into Employee objects
        return [
            Employee(emp["id"], emp["name"], emp["salary"]) for emp in employees_data
        ]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching employees: {e}")
        return []


def post_salary_update(employee: Employee, final_salary: float):
    """
    Sends a POST request to update an employee's salary.
    """
    payload = {"id": employee.emp_id, "new_salary": final_salary}
    try:
        response = requests.post(f"{API_BASE_URL}/update-salary", json=payload)
        response.raise_for_status()
        print(f"Successfully updated salary for {employee.name}.")
    except requests.exceptions.RequestException as e:
        print(f"Error updating salary for {employee.name}: {e}")
