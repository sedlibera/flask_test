from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def metai():
    if request.method == "POST":
        metai = int(request.form["metai"])
        if ((metai % 400 == 0) or
                (metai % 100 != 0) and
                (metai % 4 == 0)):
            atsakymas = f"{metai} metai yra keliamieji"
        else:
            atsakymas = f"{metai} metai yra ne keliamieji"
        return render_template("atsakymas.html", vardas=atsakymas)
    else:
        return render_template("uzklausa.html")

if __name__ == "__main__":
    app.run(debug=True)