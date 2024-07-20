from flask import Flask, jsonify, request, send_from_directory
from utilities import prediction_poi
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.post('/predict')
def predict():
    data = request.get_json()
    print("data = request.get_json(): ",data)
    try:
        sample = data['input'] # jsonfile with key sample_input
    except KeyError:
        return jsonify({'error': 'No input sent'})
    
    # sample = [sample]
    ## reshape input array
    sample = np.array(sample).reshape(1, -1)
    print("app.py, sample:",sample)
    prediction = prediction_poi(sample)
    # convert the prediction to a list to ensure it is a JSON serializable
    for i in prediction:
        if isinstance(i['input'], np.ndarray):
            i['input'] = i['input'].tolist()
    # print(prediction)
    # try:
    #     result = jsonify(prediction = prediction_list[0])
    # except TypeError as e:
    #     result = jsonify({'error': str(e)})
    # print(prediction_list)
    # result = jsonify(prediction_list[0])
    # if isinstance(prediction, np.ndarray):
    #     prediction = prediction.tolist()
    # response = {
    #     'prediction': prediction[0]
    # }
    # response = {
    #         'prediction': prediction_list[0],  # or str(prediction[0]) if the label is a string
    #         'label': 'Not a Person Of Interest' if prediction_list[0] == 0 else 'Person Of Interest'
    #     }
    result = jsonify(prediction)
    print("app.py,result: ",result)
    return result

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000, debug = True)

