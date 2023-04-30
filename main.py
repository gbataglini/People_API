from flask import Flask, jsonify, request
from people_db import get_all_people, search_person, add_person, delete_person

app = Flask(__name__)


@app.route('/')
def greet():
    return 'holy hell'


@app.route('/people')
def get_people():
    res = get_all_people()
    return jsonify(res)


@app.route('/people/<int:id>')
def get_person(id):
    person = search_person(id)
    return jsonify(person)


@app.route('/people', methods=['POST'])
def new_person():
    newperson = request.get_json()
    person = add_person(newperson)
    return person


#@app.route('/people/<int:id>', methods=['PATCH'])
# def update_person(id):
#     deets = request.get_json()
#     index = get_index(id, people)
#
#     return person

@app.route('/people/<int:id>', methods=['DELETE'])
def del_person(id):
    deleted = delete_person(id)
    return jsonify(deleted)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
