from flask import flask, jsonify
from models import db, Cat

def get_all_cats():
    all_cats = Cat.query.all()
    results = []
    for cat in all_cats:
        results.append(cat.as_dict())
    return jsonify(results)