# mock_api.py
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_FILE = "employees.json"


def read_data():
    """Reads the employee data from the JSON file."""
    with open(DB_FILE, "r") as f:
        return json.load(f)


def write_data(data):
    """Writes data back to the JSON file."""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)


@app.route("/employees", methods=["GET"])
def get_employees():
    """Endpoint to get the list of all employees."""
    data = read_data()
    return jsonify(data["employees"])


@app.route("/update-salary", methods=["POST"])
def update_salary():
    """Endpoint to update a single employee's salary."""
    update_request = request.get_json()
    emp_id = update_request.get("id")
    new_salary = update_request.get("new_salary")

    if not emp_id or new_salary is None:
        return jsonify({"error": "Missing id or new_salary"}), 400

    data = read_data()

    # Find the employee and update their salary
    for employee in data["employees"]:
        if employee["id"] == emp_id:
            employee["salary"] = new_salary
            write_data(data)
            return jsonify({"status": "success", "employee": employee})

    return jsonify({"error": "Employee not found"}), 404


if __name__ == "__main__":
    # Runs the API server on http://127.0.0.1:5000
    app.run(debug=True)
