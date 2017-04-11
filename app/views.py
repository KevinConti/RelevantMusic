from flask import render_template
from app import app, models
import sys

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
    parent_button = models.Button.query.get(id) #Button object
    children_query = parent_button.children.all() #ChildrenIds objects
    children_ids = []
    for child in children_query:
        children_ids.append(child.id)
    child_buttons = []
    for x in range(0, len(children_ids)):
        child_buttons.append(models.Button.query.get(children_ids[x]))


    return render_template('index.html',
                           title='RelevantMusic',
                           debug=children_ids,
                           buttons=child_buttons)
