## Project 1: Weather Tracker

A command-line application to fetch and display current weather information for multiple cities using the [WeatherAPI.com](https://www.weatherapi.com/) service.

### Objective

To demonstrate skills in:

- Classes and objects
- Loops and user input
- Modular functions
- API integration with an external service
- Secure management of API keys using a `.env` file

### Features

- Accepts multiple city names as user input
- Fetches real-time weather data for each city
- Stores each city's data in a `Weather` class object
- Displays a clean, formatted weather report
- Securely loads the API key from a `.env` file
- Gracefully handles API and network errors

### Setup and Usage

#### 1. Navigate to the Directory

```bash
cd weather_tracker
````

#### 2. Create `.env` File

Ensure the `.env` file exists in the root `Potoos/` directory with the following content:

```env
WEATHER_API_KEY="YOUR_API_KEY_HERE"
```

Replace `"YOUR_API_KEY_HERE"` with your actual API key from [WeatherAPI.com](https://www.weatherapi.com/).

#### 3. Set Up Virtual Environment

From the root `Potoos/` directory:

```bash
.\.venv\Scripts\Activate.ps1  # On Windows PowerShell
```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 5. Run the Application

```bash
# Ensure you are in Potoos/weather_tracker/
python main.py
```

#### Sample Interaction

```text
Enter city names (type 'done' to finish):
City: London
City: Tokyo
City: done
Fetching weather for London...
Fetching weather for Tokyo...

========================================
               Weather Report
========================================
London: Temp = 15.0°C, Condition = Partly cloudy, Humidity = 77%, Wind = 11.9 km/h, Last Updated = 2025-09-01 12:00
----------------------------------------------------------------------------------------------------
Tokyo: Temp = 28.0°C, Condition = Sunny, Humidity = 65%, Wind = 10.1 km/h, Last Updated = 2025-09-01 20:00
----------------------------------------------------------------------------------------------------
```

---

## Project 2: Employee Salary Manager

A client-server application that manages employee salaries by fetching data from a local API, applying a bonus, and posting the updated data back to the API.

### Objective-1

To demonstrate skills in:

* Building and interacting with a local API using Flask
* Handling GET and POST requests
* Separating client and server logic
* Updating and persisting JSON data

### Features-1

* Local API server (`mock_api.py`) built with Flask
* `GET` endpoint to fetch employee data
* `POST` endpoint to update employee salary
* Separate client app (`main.py`) that:

  * Consumes the API
  * Applies bonuses
  * Sends updates back to the API
  * Prints a final salary report

---

### Setup and Usage (Two-Terminal Process)

> This project requires two active terminals:
> One for the API server and one for the client app.

#### 1. Navigate to the Directory

```bash
cd employee_salary_manager
```

#### 2. Activate Virtual Environment & Install Dependencies

Use the same activated virtual environment from the root `Potoos/` directory:

```bash
pip install -r requirements.txt
```

#### 3. Terminal 1: Start the API Server

```bash
python mock_api.py
```

Leave this terminal running. You should see output indicating the server is live.

#### 4. Terminal 2: Run the Client Application

Open a new terminal, activate the virtual environment, then:

```bash
cd employee_salary_manager
python main.py
```

#### Expected Output

```text
Fetching employee data...
Successfully fetched employee data.

--- Applying Bonuses and Generating Report ---
Successfully updated salary for Alice.
Successfully updated salary for Bob.
Successfully updated salary for Charlie.

--- Final Salary Report ---
Alice   | Final Salary: 33000.0
Bob     | Final Salary: 35200.0
Charlie | Final Salary: 38500.0
```

You can verify that salaries were updated by inspecting `employees.json`.

---