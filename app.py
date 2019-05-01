from flask import Flask
from pymongo import MongoClient

client= MongoClient('mongodb://database:27017/dockerdemo')
db = client.tododb

@app.route('/')
def todo():
	_items = db.tododb.find()
	items = [item for item in _items]

	return render_template('todo.html', items=items)
