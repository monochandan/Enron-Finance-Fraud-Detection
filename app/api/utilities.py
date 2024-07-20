import pickle
import numpy as np
import warnings

from sklearn.exceptions import DataConversionWarning

warnings.filterwarnings('ignore', category=UserWarning, module = "sklearn")



with open('models/pipeline.pickle', 'rb') as f:
    loaded_pipe = pickle.load(f)

def prediction_poi(input):
    return predict(loaded_pipe, input)


def predict(model, input):
    sample_input = np.array(input)
    prediction = model.predict(sample_input)

    pred_label = {0: 'Not a Preson Of Interest',
                  1: 'Parson Of Interest'}
    
    data =[]
    for i, predic in zip(input, prediction):
        data.append({'input': i, 'pred': int(predic), 'label': pred_label[predic]})

    return data


if __name__ == '__main__':
    input = [

                    [100000, 50000, 
                     1000, 2000, 10000, 300, 
                     10000, 400, 300],

                     [1000, 500000, 
                     1000, 2000, 10000, 300, 
                     10000, 400, 3000],

                     [100000, 50000, 
                     1000, 2000, 
                     10000, 300, 10000, 400, 
                     300]
                     
                     ]
    prediction = prediction_poi(input)
    print(prediction)