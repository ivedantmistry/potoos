class Weather:
    """A class to represent weather information for a specific city."""

    def __init__(
        self, city, temperature, condition, humidity, wind_speed, last_updated
    ):
       
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.last_updated = last_updated

    def __str__(self):
        """
        Returns a user-friendly, formatted string representation of the weather information.
        This method is automatically called when you try to print an object of this class.
        """
        return (
            f"{self.city}: Temp = {self.temperature}°C, Condition = {self.condition}, "
            f"Humidity = {self.humidity}%, Wind = {self.wind_speed} km/h, "
            f"Last Updated = {self.last_updated}"
        )
