from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name>")
def home(name):
    sarasas = []
    [sarasas.append(name) for item in range(5)]
    return render_template("pakartojimai.html", zodziai=sarasas)

if __name__ == "__main__":
    app.run(debug=True)