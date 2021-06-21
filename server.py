from flask import Flask, render_template, request, redirect

from models.dojo import Dojo

app = Flask(__name__)
app.secret_key = "I expect nothing and i am still disappointed"

@app.route('/')
def index():
    dojos = Dojo.show_all_dojos()

    return render_template("index.html", all_dojos = dojos)

@app.route('/ninja/new')
def new_ninja_form():
    return render_template("new_ninja.html")


@app.route('/ninja', methods = [ "POST" ] )
def create_ninja():
    print(request.form)
    Ninja.create(request.form)

    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)