from flask import jsonify, request
from __init__ import app , db
# from . import app, db

from model import Counter


@app.route('/counter', methods=['PUT'])
def increment_counter():
    key_value_pair = request.get_json()['key']
    print(key_value_pair)
    record = Counter.query.get(1)
    if key_value_pair == "a":
        record.a += 1

    elif key_value_pair == "b":
        record.b += 1

    elif key_value_pair == "c":
        record.c += 1

    else:
        return jsonify({'answer': "Invalid : Key_value_pair"}), 400

    db.session.commit()

    return jsonify({'answer': {"record.a": record.a, "record.b": record.b, "record.c": record.c}}), 200

    # if record.a >= 5 or record.b >= 5 or record.c >= 5:
    #     record.a = 0
    #     record.b = 0
    #     record.c = 0
    # db.session.commit()
    #
    # return jsonify({'answer': {"record.a": record.a, "record.b": record.b, "record.c": record.c}}), 200


@app.route('/counter/all', methods=['GET'])
def get_counter():
    record = Counter.query.get(1)
    if not record:
        return jsonify({'answer': " This Record Was not found in this request"}), 404

    return jsonify({'answer': {"record.a": record.a, "record.b": record.b, "record.c": record.c}}), 200


@app.route('/create_counter', methods=['POST'])
def create_counter():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    c = data.get('c', 0)

    new_counter = Counter(a=a, b=b, c=c)

    new_counter.save()

    return jsonify({
        'id': new_counter.id,
        'a': new_counter.a,
        'b': new_counter.b,
        'c': new_counter.c
    }), 201



# @app.route('/b', methods=['PUT'])
# def increment_counter1():
#     global counter_b
#     counter_b += 1
#     return jsonify({'answer': counter_b}) ,200
#
# @app.route('/c', methods=['PUT'])
# def increment_counter2():
#     global counter_c
#     counter_c += 1
#     return jsonify({'answer': counter_c}) ,200


if __name__ == '__main__':
    app.run(debug=True)

