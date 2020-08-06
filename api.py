from models import app, Cat
from flask import jsonify, request

@app.route('/')
def home():
    first_cat = Cat.query.first()
    print(f'hello {first_cat}')


@app.route('/cats', methods=['GET', 'POST'])
def cats():
    if request.method == 'GET':
        return get_all_cats()
    else:
        return create_cat()


@app.route('/cats/<int:id>')
def 
