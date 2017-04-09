from flask import render_template
from app import app, models

@app.route('/')
@app.route('/index')
def index():
    #Get the first three buttons
    buttons = []
    for x in range(1,4):
        button = models.Button.query.get(x)
        buttons.append(button)
    return render_template('index.html',
                           title='RelevantMusic',
                           buttons=buttons)

@app.route('/index/<id>')
def refreshButton(id):
    #Logic that gets children based off of parent's id
    #param: id parent's id
    #returns: render_template('index.html', buttons=[])
    parent_button = models.Button.query.get(id)
    children = parent_button.children
    return render_template('index.html',
                           title='RelevantMusic',
                           buttons=children)
