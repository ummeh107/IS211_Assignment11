from flask import Flask, redirect, render_template,request
import re


app = Flask(__name__)

todo_list = []


@app.route("/")
def index():
    return render_template('index.html',todo=todo_list)

# Submit Todo
@app.route("/submit", methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    
    if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
        return redirect("/")
    elif not task:
        return redirect("/")
    elif priority == "Select Priority":
        return redirect("/")

    todo_list.append((task,email,priority))
    return redirect('/')

# Clear Todo
@app.route("/clear", methods=['POST'])
def clear():
    todo_list.clear()
    return redirect("/")

# Delete Todo
@app.route("/delete", methods=['POST'])
def delete():
    id = request.form['deleteId']
    del todo_list[int(id)-1]
    return redirect('/')
    


if __name__=='__main__':
    app.run(debug=True)    

