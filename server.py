from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.secret_key = 'whale hello there!'

# importing the User class method
from users import User

@app.route('/')
def show_form():
    return render_template('create.html')

@app.route('/read_all')
def show_all():
    users = User.get_all()
    print(users)
    return render_template('read_all.html', all_users = users)

@app.route('/new_user', methods=["POST"])
def new_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.add_user(data)
    return redirect('/read_all')

@app.route('/read_one/<int:id>')
def show_one(id):
    data = {
        'id' : id,
    }
    user_info = User.read_one(data)
    return render_template ('read_one.html', user = user_info)

@app.route('/read_one/<int:id>/edit')
def edit(id):
    data = {
        "id" : id
    }
    user = User.read_one(data)
    return render_template('/edit.html', user = user)

@app.route('/update/<int:id>', methods=["POST"])
def update_user(id):
    data = {
        'id': id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect(f'/read_one/{id}')

@app.route('/read_all/<int:id>/delete')
def delete(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect('/read_all')

if __name__=='__main__':
    app.run(debug=True)