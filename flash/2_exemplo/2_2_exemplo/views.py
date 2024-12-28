from  main import app

@app.route("/")
def homepage():
    return "Meu site no Flask"

