from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    new_todo = request.form.get('todo')
    if new_todo:
        todos.append({'task': new_todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    todos[todo_id]['done'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    del todos[todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Change the port to 8080 or any available port

