from flask import Flask, render_template

app = Flask(__name__)

filespath = __file__.rsplit("\\",1)[0] + "\\files\\"

@app.route('/')
def home():
    return render_template("home.html", title="Webshop")

@app.route('/warenkorb')
def warenkorb():
    return render_template("warenkorb.html", title="Warenkorb")

@app.route('/about')
def about():
    return render_template("about.html", title="Über uns")

@app.route('/produktt')
def produktt():
    return render_template("produkt.html", title="Detailansicht")

@app.route('/produkt/<path:produktname>')
def produkt(produktname):
    file = open(filespath + produktname + ".txt", "r", encoding="UTF-8")
    data = {}
    for line in file.readlines():
        keyword = line[:line.index(":")]
        value = line[line.index(":")+1:]
        data[keyword] = value
        print(f"{keyword=} {value=}")


    return render_template("produkt.html", title=produktname, titel=data['titel'], autor=data['autor'],
                           stichworte=data['stichworte'], beschreibung=data['beschreibung'], bildlink=data['bildlink'])



if __name__ == '__main__':
    app.run()


