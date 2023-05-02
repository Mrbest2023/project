from flask import Flask, request, jsonify

from EE250_Project import main 
from notes import frequency_spectrum, note



app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})
@app.route('/main')
def pro1():
    data=request.get_json()
    return jsonify(main(data))
@app.route('/frequency_spectrum')
def pro2():
    data=request.get_json()
    return jsonify(frequency_spectrum(data))
@app.route('/note')
def pro3():
    data=request.get_json()
    return jsonify(note(data))

if __name__ == '__main__':
    app.run("0.0.0.0")
    while True:
        try: 
            sr=32
            frequency,X=frequency_spectrum(sensor_value, sr)
            type=note(frequency)

        except:



