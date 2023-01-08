from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", title="Webshop")

@app.route('/warenkorb')
def warenkorb():
    return render_template("warenkorb.html", title="Warenkorb")

@app.route('/about')
def about():
    return render_template("about.html", title="Über uns")

if __name__ == '__main__':
    app.run()
