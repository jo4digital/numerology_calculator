from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from datetime import datetime
from numerology_brain import NumerBrain
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")
bootstrap = Bootstrap5(app)

brain = NumerBrain()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        birthdate_data = request.form.get("date")  # indexWP: "form_fields[field_cc0ac99]"
        # name = request.form.get("name")
        # email = request.form.get("email")
        birthdate = birthdate_data.replace("-", "")
        month = birthdate_data.split("-")[1]
        year = birthdate_data.split("-")[0]
        age = datetime.now().year - int(year)
        life_path_number = brain.numer_calc(birthdate, age, month)
        life_path_status = brain.numer_dict[life_path_number]
        return render_template("index.html", num=life_path_number, text=life_path_status, sent=True)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
