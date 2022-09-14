from flask import Flask
app = Flask(__name__)

@app.route("/<vardas>")
def home(vardas):
    return f"Labas, {vardas}"

if __name__ == "__main__":
    app.run(debug=True)