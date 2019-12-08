from flask import Flask, redirect, render_template,request
import re
import os.path
from os import path

app = Flask(__name__)

todo_list = []


@app.route("/")
def index():
    todo_list.clear()
    if not path.exists('todolist.txt'):
        open("todolist.txt", "w+")
    with open("todolist.txt", 'r') as tasks:
        # print(tasks)
        for task in tasks:
            # print(task)
            todo_list.append(tuple(task.split(',')))        
         
    return render_template('index.html',todo=todo_list)

# Submit Todo
@app.route("/submit", methods=['POST'])
def submit():
    todo_list.clear()
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    
    if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
        return redirect("/")
    elif not task:
        return redirect("/")
    elif priority == "Select Priority":
        return redirect("/")
    
    f = open("todolist.txt", "a+")
    f.write(task +','+ email + ','+ priority+ '\n')
    f.close()

    todo_list.append((task,email,priority))
    print(todo_list)

    return redirect('/')

# Clear Todo
@app.route("/clear", methods=['POST'])
def clear():
    f = open('todolist.txt', 'r+')
    f.truncate(0)
    return redirect("/")

# Delete Todo
@app.route("/delete", methods=['POST'])
def delete():
    todo_list.clear()
    with open("todolist.txt", 'r') as tasks:
        for task in tasks:
            todo_list.append(tuple(task.split(',')))
    f = open('todolist.txt', 'r+')
    f.truncate(0)

    id = request.form['deleteId']
    del todo_list[int(id)-1]
    
    for item in todo_list:
        f = open("todolist.txt", "a+")
        f.write(item[0]+', '+item[1]+', '+ item[2])
        f.close()

    return redirect('/')
    


if __name__=='__main__':
    app.run(debug=True)    