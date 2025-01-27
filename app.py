from flask import Flask, render_template, request
from get_result import get_photo

app = Flask(__name__)


@app.route("/")
def get_data():
    return render_template("get_data.html")


@app.route("/photo", methods=["POST"])
def photo():
    date = request.form.get("date")

    result = get_photo(date=date)
    if not date:
        return "Ви не ввели дату!", 400
    try:
        if result.status_code == 400:
            return render_template("date_error.html")
        elif result.status_code == 404:
            return render_template("missing_error.html")
        else:
            return render_template("photo.html", photo=result.json()["hdurl"])
    except ValueError:
        return "Невірний формат дати!", 400


if __name__ == "__main__":
    app.run(debug=True)
