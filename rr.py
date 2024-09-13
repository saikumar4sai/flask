# # from flask import jsonify, request
# # from __init__ import app, db
# # # from . import app, db
# #
# # from model import Counter
# #
# #
# # # counter = 0
# #
# #
# # # @app.route('/counter', methods=['POST'])
# # # def counter():
# # #     global counter
# # #
# # @app.route('/counter', methods=['PUT'])
# # def increment_counter():
# #     # global counter_a
# #     # counter_a += 1
# #     key_value_pair = request.get_json()['key']
# #     print(key_value_pair)
# #     if key_value_pair == "a":
# #         # records = Counter.query.all()
# #         # print(records)
# #         # for record in records:
# #         #     print(record.id, record.a, record.b, record.c)
# #
# #         record = Counter.query.get(1)
# #         print('a', record.a)
# #         print('b', record.b)
# #         print('c', record.c)
# #         record.a += 1
# #         db.session.commit()
# #
# #         return jsonify({'answer': {"record.a": record.a, "record.b": record.b, "record.c": record.c}}), 200
# #
# #     elif key_value_pair == "b":
# #         counter = Counter.query.filter.by(key=key_value_pair).first()
# #         if counter:
# #             counter.count += 1
# #             db.session.commit()
# #             return jsonify({'answer': counter.count}), 200
# #
# #     elif key_value_pair == "c":
# #         counter = Counter.query.filter.by(key=key_value_pair).first()
# #         if counter:
# #             counter.count += 1
# #             db.session.commit()
# #             return jsonify({'answer': counter.count}), 200
# #     else:
# #         return jsonify({'answer': "Invalid : Key_value_pair"}), 400
# #
# #
# # @app.route('/create_counter', methods=['POST'])
# # def create_counter():
# #     # Extract data from the request
# #     data = request.get_json()  # Expecting JSON payload
# #
# #     a = data.get('a', 0)  # Default to 0 if not provided
# #     b = data.get('b', 0)  # Default to 0 if not provided
# #     c = data.get('c', 0)  # Default to 0 if not provided
# #
# #     # Create a new Counter instance
# #     new_counter = Counter(a=a, b=b, c=c)
# #
# #     # Save the instance to the database
# #     new_counter.save()
# #
# #     return jsonify({
# #         'id': new_counter.id,
# #         'a': new_counter.a,
# #         'b': new_counter.b,
# #         'c': new_counter.c
# #     }), 201  # 201 Created status code
# #
# #
# # # @app.route('/b', methods=['PUT'])
# # # def increment_counter1():
# # #     global counter_b
# # #     counter_b += 1
# # #     return jsonify({'answer': counter_b}) ,200
# # #
# # # @app.route('/c', methods=['PUT'])
# # # def increment_counter2():
# # #     global counter_c
# # #     counter_c += 1
# # #     return jsonify({'answer': counter_c}) ,200
# #
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
# @app.route('/counter', methods=['PUT'])
# def increment_counter():
#     key_value_pair = request.get_json()['key']
#     print(key_value_pair)
#     record = Counter.query.get(1)
#     if record:
#         if key_value_pair == "a":
#             record.a += 1
#         elif key_value_pair == "b":
#             record.b += 1
#         elif key_value_pair == "c":
#             record.c += 1
#         else:
#             return jsonify({'answer': "Invalid : Key_value_pair"}), 400
#         db.session.commit()
#         return jsonify({'answer': {"record.a": record.a, "record.b": record.b, "record.c": record.c}}), 200




#
# @app.route('/counter', methods=['PUT'])
# def increment_counter():
#     key_value_pair = request.get_json().get('key')
#     print(key_value_pair)
#     record = Counter.query.get(1)
#     if key_value_pair == "a":
#         record.a += 1
#     elif key_value_pair == "b":
#         record.b += 1
#     elif key_value_pair == "c":
#         record.c += 1
#     else:
#         return jsonify({'answer': "Invalid : Key_value_pair"}), 400
#
#     if record.a >= 5 or record.b >= 5 or record.c >= 5:
#         record.a = 0
#         record.b = 0
#         record.c = 0
#
#     db.session.commit()
#
#     return jsonify({'answer': {"record.a": record.a, "record.b": record.b, "record.c": record.c}}), 200


# number = 7
# for i in range(1,11):
#     print(number, "*", i, "=", number * i)