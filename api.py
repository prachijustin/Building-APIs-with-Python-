import flask
from flask import request, jsonify

app = flask.Flask(__name__)

#data to send
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '<h1>Prototype of API work</h1>'


#url on which all the books can be seen
@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


#url to search for a book by its id
#eg: .../api/books?id=0
@app.route('/api/books/', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'No id provided'

    results=[]
    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)



if __name__ == '__main__':
    app.run(debug=True)
