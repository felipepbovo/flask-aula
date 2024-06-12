from flask import Flask, render_template

app = Flask ("reserva app")

@app.route("/")
def principal():
    return render_template('principal.html')