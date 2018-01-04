from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

tasks = []

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template('todo.html', title='Get It Done!', tasks=tasks)

app.run()