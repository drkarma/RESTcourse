from flask import Flask, jsonify, request, render_template


app = Flask(__name__)



stores = [
    {
        'name': 'My own store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }

]

#POST /store data: {name:}
@app.route('/store', methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []

    }
    stores.append(new_store)
    return jsonify(new_store)

#GET all stores
@app.route('/store', methods=["GET"])
def get_all_stores():
    #return jsonify(stores)
    return jsonify({'stores': stores})

#GET /store/<string:name>
@app.route('/store/<string:name>', methods=["GET"])
def get_store(name):
    return name




app.run(port=5000)