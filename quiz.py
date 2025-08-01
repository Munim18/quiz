from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello2/")
def hello2():
    return render_template(
    'quiz.html')

if __name__ == "__main__":
    app.run()    