from flask import Flask, request,render_template
import nltyty as aks



app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    summary=""
    if request.method == "POST":
        url = request.form["url"]
        summary = aks.scrrr(url)
    return render_template('index.html', summary=summary)


if __name__ == '__main__':
    app.run()
