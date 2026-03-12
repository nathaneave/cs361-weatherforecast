# CS361 (Group 17) - Big Pool Microservice: Weather Forecast (Current Weather)

**What does this microservice do?**

This microservice allows the user to get the current weather at a provided zipcode. It will return the feels like temperature, actual temperature, and a description of the current conditions.

**How do I request data from this microservice?**

To request data from this microservice, you will need to make an `HTTP GET request` to the `/weatherforecast` endpoint. You must pass `zipcode` as a string that represents the zipcode that you would like to get the current conditions of. This microservice uses the OpenWeatherMap API, and you must have a .env variable named `OPENWEATHER_API_KEY` (which is your API key) in order to use the microservice.

_Example call:_ `GET http://127.0.0.1:8000/weatherforecast?zipcode=90210`



**How will I receive data from this microservice?**

The microservice will return a `JSON object`. The object will have four name/value pairs. The name/value pairs will be `feels_like` which is an integer representing the current feels like temperature, `temp` which is an integer representing the current actual temperature, `weather` which is a string representing the current conditions, and `weather_desc` which is a string representing a longer description of the current conditions

_Example response_:

Status code: `200`
```yaml
{
"feels_like": 42,
"temp": 48,
"weather": "Rain",
"weather_desc": "moderate rain
}
```
