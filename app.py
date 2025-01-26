from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()
API = os.getenv("API_KEY")

app = Flask(__name__)


@app.route("/")
def get_data():
    return render_template("get_data.html")


@app.route("/photo", methods=["POST"])
def photo():
    date = request.form.get("date")

    if not date:
        return "Ви не ввели дату!", 400

    try:
        url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={API}"
        result = requests.get(url=url)
        if result.status_code == 400:
            return render_template("error.html")
        else:
            return render_template("photo.html", photo=result.json()["hdurl"])
    except ValueError:
        return "Невірний формат дати!", 400


if __name__ == "__main__":
    app.run(debug=True)
