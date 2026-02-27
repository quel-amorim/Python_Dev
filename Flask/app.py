from flask import Flask , template_rendered

app = Flask(__name__)

@app.route("/")

def inicial():
    return "Finalmente tem o modulo Mundo 4 em Python do Guanabara !!!! "

if __name__ == "__main__":
    app.run()