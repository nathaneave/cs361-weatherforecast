from fastapi import FastAPI, HTTPException
import requests
from datetime import datetime, timezone, timedelta
import os
from dotenv import load_dotenv
import pgeocode
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
load_dotenv()


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.get("/weatherforecast")
def root(zipcode: str):
    latitude, longitude = convert_zipcode(zipcode)
    request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial"
    response = requests.get(request_url)
    data = response.json()

    feels_like = int(data['main']['feels_like'])
    temp = int(data['main']['temp'])
    weather = data['weather'][0]['main']
    weather_desc = data['weather'][0]['description']

    return {"feels_like": feels_like, "temp": temp, "weather": weather, "weather_desc": weather_desc}


def convert_zipcode(zipcode):
    if zipcode == "null":
        raise HTTPException(status_code=400, detail="Missing zipcode. Please provide a valid zipcode.")
    
    n = pgeocode.Nominatim('US')
    location = n.query_postal_code(zipcode)

    return location.latitude, location.longitude
