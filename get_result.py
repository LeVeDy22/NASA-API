from dotenv import load_dotenv
import requests
import os

load_dotenv()
API = os.getenv("API_KEY")

def get_photo(date):
    url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={API}"
    result = requests.get(url=url)
    return result