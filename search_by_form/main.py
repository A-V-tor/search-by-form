from flask import Flask, request
from .db import collection
from .utils import match_checking, define_field_type
from fill import make_fill


app = Flask(__name__)


# заполнить коллекцию документами
if not collection.find_one():
    make_fill()


@app.post('/get_form')
def indx():
    query_params = request.args.to_dict()
    print(123, query_params)
    response = match_checking(query_params, collection)
    if not response:
        response = define_field_type(query_params)
    return f'{response}'


if __name__ == '__main__':
    app.run(debug=True)
