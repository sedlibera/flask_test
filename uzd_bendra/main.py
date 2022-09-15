from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pakartojimai/")
def pakartojimai():
    req = request.url
    sarasas = []
    [sarasas.append(req) for item in range(5)]
    return render_template("pakartojimai.html", zodziai=sarasas)

@app.route("/keliamieji/")
def keliamieji():
    sarasas = []
    for year in range(1900, 2101):
        if ((year % 400 == 0) or
                (year % 100 != 0) and
                (year % 4 == 0)):
            sarasas.append(year)
    return render_template("keliamieji.html", metai=sarasas)

@app.route("/ar_keliamieji_metai/", methods=["GET", "POST"])
def ar_keliamieji_metai():
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

