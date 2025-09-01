# main.py
from salary_utils import fetch_employees, post_salary_update

BONUS_PERCENTAGE = 10.0 # Define the bonus percentage here

def main():
    """
    Main function to run the employee salary management process.
    """
    print("Fetching employee data...")
    employees = fetch_employees()
    
    if not employees:
        print("No employees found or failed to connect to API. Exiting.")
        return

    print("\n--- Applying Bonuses and Generating Report ---")
    
    final_salaries_report = []

    # Use a for loop to process each employee
    for emp in employees:
        # 1. Apply the bonus
        final_salary = emp.apply_bonus(BONUS_PERCENTAGE)
        
        # 2. Add the result to our report list
        report_line = f"{emp.name} | Final Salary: {final_salary}"
        final_salaries_report.append(report_line)
        
        # 3. Send the POST request to update the salary in the "database"
        post_salary_update(emp, final_salary)

    # 4. Print the final report
    print("\n--- Final Salary Report ---")
    for line in final_salaries_report:
        print(line)

if __name__ == "__main__":
    main()