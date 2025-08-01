from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    "aaron": {"name": "aaron jhonson", "age": 23, "email": "aaron@example.com"},
    "mike": {"name": "mike kennedy ", "age": 25, "email": "mike@example.com"},
    "amy": {"name": "amy william", "age": 29, "email": "amy@example.com"},
    "alice": {"name": "Alice Smith", "age": 30, "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "age": 25, "email": "bob@example.com"},
    "charlie": {"name": "Charlie Brown", "age": 35, "email": "charlie@example.com"}
}

@app.route("/bitswits/")
def bitswits_main():
    return render_template('bitswits_main.html')


@app.route('/user_selection/', methods=['GET', 'POST'])
def user_selection():
    if request.method == 'POST':
        if 'username' in request.form:
            selected_user = request.form['username']
            user_profile = users.get(selected_user)
            return render_template('profile.html', user=user_profile)

        elif 'max_age' in request.form:
            max_age = int(request.form['max_age'])
            matched_users =[]

            matched_users = [
                user_details for user_details in users.values()
                if user_details['age'] <= max_age
            ]
            return render_template('profile.html', users=matched_users, max_age=max_age)

    return render_template('index.html', usernames=users.keys())


if __name__ == "__main__":
    app.run(debug=True)



    # from flask import Flask, render_template, request
# app = Flask(__name__)

# users = {
#     "aaron": {"name": "aaron jhonson", "age": 23, "email": "aaron@example.com"},
#     "mike": {"name": "mike kennedy ", "age": 25, "email": "mike@example.com"},
#     "amy": {"name": "amy william", "age": 29, "email": "amy@example.com"},
#     "alice": {"name": "Alice Smith", "age": 30, "email": "alice@example.com"},
#     "bob": {"name": "Bob Johnson", "age": 25, "email": "bob@example.com"},
#     "charlie": {"name": "Charlie Brown", "age": 35, "email": "charlie@example.com"}
# }


# @app.route("/bitswits/")
# def bitswits_main():
#     return render_template(
#     'bitswits_main.html')

# # @app.route('/max_age/', methods=['GET', 'POST'])
# # def max_age():
    
# #         max_age = int(request.form['max_age'])
# #         matched_users =[]
     
# #         for  username, user_details in users.items():
# #             print('username : ', username)
# #             print('User details are : ', user_details)
# #             print('User age is : ', user_details['age'])
# #             if user_details['age'] <= max_age:
# #                 matched_users.append(user_details)
# #                 return render_template('profile.html', users=matched_users, max_age=max_age)

# # @app.route('/user_selection/', methods=['GET', 'POST'])
# # def user_selection():
# #      if request.method == 'POST':
# #             selected_user = request.form['username']
# #             user_profile = users.get(selected_user)
# #             return render_template('profile.html', user=user_profile)
# #      else:
# #             return render_template('index.html', usernames=users.keys())



# @app.route('/user_selection/', methods=['GET', 'POST'])
# def user_selection():
#      if request.method == 'POST':
#         if 'username' in request.form:
#             selected_user = request.form['username']
#             user_profile = users.get(selected_user)
#             return render_template('profile.html', user=user_profile)
#         elif 'max_age' in request.form:
#             max_age = int(request.form['max_age'])
#             matched_users =[]
#             for user_details in users.values():
#                 if user_details['age'] <= max_age:
#                     matched_users.append(user_details)
#             return render_template('profile.html', users=matched_users, max_age=max_age)
#      return render_template('index.html', usernames=users.keys())
     
            

# if __name__ == "__main__":
#     app.run()    












# # @app.route('/profile3/', methods=['GET', 'POST'])
# # def profile3():
# #     if request.method == 'POST':
# #         max_age = int(request.form['max_age'])
# #         matched_users =[]

# #         if request.method == 'POST':
# #             selected_user = request.form['username']
# #             user_profile = users.get(selected_user)
# #             return render_template('profile.html', user=user_profile)
        
# #         for  username, user_details in users.items():
# #             print('username : ', username)
# #             print('User details are : ', user_details)
# #             print('User age is : ', user_details['age'])
# #             if user_details['age'] <= max_age:
# #                 matched_users.append(user_details)
# #         return render_template('profile.html', users=matched_users, max_age=max_age)
   



