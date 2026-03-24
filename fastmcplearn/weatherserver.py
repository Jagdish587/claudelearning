from fastmcp import FastMCP
import requests

mcp = FastMCP("Weather MCP Server")


@mcp.tool
def get_current_weather(city: str) -> str:
    """
    Get current weather information for a given city, including temperature,
    weather condition, humidity, and wind speed.
    """
    try:
        # wttr.in API (simple weather service)
        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        condition = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]
        wind_speed = current["windspeedKmph"]

        # Clean formatted response
        return (
            f"Weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Condition: {condition}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} km/h"
        )

    except Exception as e:
        return f"Unable to fetch weather for {city}. Error: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")