from flask import Flask, redirect, url_for, render_template, jsonify, request

app = Flask(__name__)

user_address_info = dict()
occupation_info = dict()
option_text = ""

@app.route('/')
def hello_world():
    return redirect(url_for('homepage'))


@app.route('/homepage')
def homepage():  # put application's code here
    return render_template('homepage.html')

@app.route('/options')
def options():  # put application's code here
    return render_template('options.html')


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
        occupation_info["occupation"] = json_data['occupation']
        print(occupation_info)

    return jsonify(dict())

@app.route('/results', methods=['GET', 'POST'])
def results():
    global option_text

    if request.method == 'GET':
        option = request.args.get('type')
        if option == 'amenities':
            option_text = f"I want to live somewhere near facilities/infrastructures/amenities in {user_address_info['city']} {user_address_info['state']}, Could you give me any suggestions?"
        elif option == 'education':
            option_text = f"If I want good education environment for my kids, which neighborhood should I live in {user_address_info['city']} {user_address_info['state']}?"
        elif option == 'explore':
            option_text = f"Which neighborhood should people live in {user_address_info['city']} {user_address_info['state']} if they has never been to ?"
        elif option == 'best_overall':
            option_text = f"Recommend neighborhoods to live for the best criteria in {user_address_info['city']}{user_address_info['state']}"
        elif option == 'architecture':
            return render_template('architecture.html')
        elif option == 'hobby':
            return render_template('hobby.html')


    print(option_text)

    return


@app.route('/results/architecture', methods=['POST'])
def architecture():
    global option_text, user_address_info
    if request.method == 'POST':
        json_data = request.get_json()
        session["architecture"] = json_data['architecture']
        option_text = f"If I am a huge fan of {session['architecture']} style housing, which neighborhood in {user_address_info['city']}{user_address_info['state']} I can consider living in?"

    return jsonify(dict())


@app.route('/results/hobby', methods=['POST'])
def hobby():
    global option_text, user_address_info
    if request.method == 'POST':
        json_data = request.get_json()
        session["hobby"] = json_data['hobby']
        option_text = f"Where is the best neighborhood to live if I like {session['hobby']} in {user_address_info['city']}{user_address_info['state']}?"

    return jsonify(dict())


if __name__ == '__main__':
    app.run(debug=True)

