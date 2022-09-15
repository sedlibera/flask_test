from flask import Flask, render_template
app = Flask(__name__)

@app.route("/keliamieji")
def keliamieji():
    sarasas = []
    for year in range(1900, 2101):
        if ((year % 400 == 0) or
                (year % 100 != 0) and
                (year % 4 == 0)):
            sarasas.append(year)
    return render_template("keliamieji.html", metai=sarasas)

if __name__ == "__main__":
    app.run(debug=True)