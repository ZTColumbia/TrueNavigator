from flask import Flask, redirect, url_for, render_template, jsonify, request

app = Flask(__name__)

user_address_info = dict()
occupation_info = dict()


@app.route('/')
def hello_world():
    return redirect(url_for('homepage'))


@app.route('/homepage')
def homepage():  # put application's code here
    return render_template('homepage.html')

@app.route('/options')
def options():  # put application's code here
    return render_template('Options.html')


@app.route('/toCityAndState', methods=['GET', 'POST'])
def to_city_State():
    return jsonify(dict(redirect=f'/cityAndState'))


@app.route('/cityAndState')
def render_city_State():
    return render_template('cityAndState.html')

@app.route('/address_info', methods=['POST'])
def address_info():
    global user_address_info
    if request.method == 'POST':
        json_data = request.get_json()
        user_address_info["country"] = json_data["country"]
        user_address_info["state"] = json_data["state"]
        user_address_info["city"] = json_data["city"]
        print(user_address_info)

    return jsonify(dict(redirect=f'/toOccupation'))

@app.route('/toOccupation')
def render_occupation():
    return render_template('occupation.html')


@app.route('/occupation_info', methods=['POST'])
def occupation_info():
    global user_address_info
    if request.method == 'POST':
        json_data = request.get_json()
        occupation_info["occupation"] = json_data["occupation"]
        print(occupation_info)

    return jsonify(dict())


if __name__ == '__main__':
    app.run(debug=True)

