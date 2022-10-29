from flask import Flask, redirect, url_for, render_template, jsonify, request
import json
import openai

app = Flask(__name__)

"""
#####################################################
Open AI Function
"""
def gpt_engine(prm):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prm,
        max_tokens=64,
        temperature=0.75,
        top_p=1,
    )
    return response.choices[0].text
"""
#####################################################
"""
user_address_info = dict()
occupation_info = dict()


@app.route('/')
def hello_world():
    return redirect(url_for('homepage'))


@app.route('/homepage')
def homepage():  # put application's code here
    return render_template('homepage.html')


@app.route('/toCityAndState', methods=['GET', 'POST'])
def to_city_State():
    return jsonify(dict(redirect=f'/cityAndState'))


@app.route('/cityAndState')
def render_city_State():
    prompt = "Give me 5 suggested cities and states for living."
    tip = gpt_engine(prompt)
    return render_template('cityAndState.html', tip=tip)


@app.route('/address_info', methods=['POST'])
def address_info():
    global user_address_info
    if request.method == 'POST':
        json_data = request.get_json()
        user_address_info["country"] = json_data["country"]
        user_address_info["state"] = json_data["state"]
        user_address_info["city"] = json_data["city"]

    return jsonify(dict(redirect=f'/toOccupation'))


@app.route('/toOccupation')
def render_occupation():
    city = user_address_info["city"]
    state = user_address_info["state"]
    prompt = "What is the majority occupation of people living in " + city + "," + state + "?"
    tip = gpt_engine(prompt)
    return render_template('occupation.html', tip=tip)


@app.route('/occupation_info', methods=['POST'])
def occupation_info():
    global occupation_info
    if request.method == 'POST':
        json_data = request.get_json()
        occupation_info["occupation"] = json_data["occupation"]
    return jsonify(dict())


@app.route('/callGPT', methods=['GET','POST'])
def call_GPT():
    res = dict()
    json_data = request.get_json()
    prompt = json_data["prompt"]
    re = gpt_engine(prompt)
    res["result"] = re
    return jsonify(res)

if __name__ == '__main__':
    app.run()
