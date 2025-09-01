from weather_utils import fetch_weather

def get_user_cities():
    """
    Returns:
        list: A list of city names entered by the user.
    """
    cities = []
    print("Enter city names (type 'done' to finish):")
    while True:
        city = input("City: ").strip()
        if city.lower() == "done":
            break
        if city:  # Ensure the input is not empty
            cities.append(city)
    return cities


def main():
    """
    The main function to run the weather tracker application.
    It gets cities from the user, fetches their weather data,
    and prints a formatted report.
    """
    cities = get_user_cities()
    weather_reports = []

    if not cities:
        print("No cities were entered. Exiting application.")
        return

    # Loop through each city provided by the user
    for city in cities:
        print(f"Fetching weather for {city}...")
        weather_data = fetch_weather(city)
        # Only add to the report if data was successfully fetched
        if weather_data:
            weather_reports.append(weather_data)

    # Display the final report if any data was collected
    if weather_reports:
        print("\n" + "=" * 40)
        print("           Weather Report")
        print("=" * 40)
        for report in weather_reports:
            print(
                report
            )  # This automatically calls the __str__ method of the Weather object
            print("-" * 100)


if __name__ == "__main__":
    main()
