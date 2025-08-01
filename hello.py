# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Index!"

# @app.route("/hello")
# def hello():
#     return "Hello World!"

# @app.route("/members")
# def members():
#     return "Members"

# @app.route("/bitswits")
# def bitswits():
#    return "Welcome To BitsWits. Best of luck for the day"

# @app.route("/sum")
# def sum():
#    sum = 2 + 2
#    final_str = "The sum of 2 + 2 is : " + str(sum)
#    return  final_str

# if __name__ == "__main__":
#     app.run()






# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Flask App!"

# @app.route("/hello2/")
# def hello2():
#     return render_template(
#     'WELCOME.html')

# if __name__ == "__main__":
#     app.run()    





from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Flask App!"

# @app.route("/profile")
# def hello2():
#     return render_template(
#     'profile.html')

# @app.route("/members/<string:name>/")
# def getMember(name):
#     return name

# @app.route("/hello/<string:name>/")
# def hello(name):
#     print(name)
#     return render_template(
#     'Dynamic.html',name=name)

# @app.route("/hello2/<string:name>/<string:lastname>/")
# def hello(name,lastname):
#     print(name)
#     return render_template(
#     'Name.html',name=name, lastname=lastname)





# users = {
#     "aaron": {"name": "aaron jhonson", "age": 23, "email": "aaron@example.com"},
#     "mike": {"name": "mike kennedy ", "age": 25, "email": "mike@example.com"},
#     "amy": {"name": "amy william", "age": 29, "email": "amy@example.com"}
# }

# @app.route('/usersbio/')
# def profile():
#     return render_template('usersbio.html', usernames=users.keys())

# @app.route("/hello")
# def hello():
#     return "Hello World!"


@app.route("/hello2/")
def hello2():
    return render_template(
    'quiz.html')

if __name__ == "__main__":
    app.run()    