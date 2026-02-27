import flask as fk

app = fk.Flask(__name__)

@app.route("/")
def iniciar():
    return 'Olá primeiro flask !'

if __name__ == '__main__':
    app.run(debug=True)