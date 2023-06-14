# from pyexpat import model
# from flask import Flask , render_template
# from matplotlib import scale 
# import pandas as pd 
# from sklearn.model_selection import train_test_split 
# from sklearn.linear_model import LogisticRegression 
# from sklearn.metrics import classification_report, confusion_matrix
# from sklearn.preprocessing import StandardScaler
# import requests 
# import os

# app = Flask(__name__)
# dataset_file = os.path.join(app.root_path, 'static', 'dataset.csv')
# @app.route('/')
# def hello_world():
#    Data = pd.read_csv("dataset_file")
#    X = Data[['Oxygen','PulseRate','Temperature']]
#    y = Data['Result']

#    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
#    logreg = LogisticRegression()
#    logreg.fit(X_train,y_train) 

#    channel_id = ''
#    read_api_key = ''
#    num_entries = 5 # number of latest entries to fetch 

#    url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}'
#    response = requests.get(url)
#    Data = response.json()

#    predict_data = pd.DataFrame(Data['feeds'])
#    predict_X = predict_data[['field1','field2','field3']]
#    data_time = predict_data['created_at']

#    #convert data types and rename colum 
#    predict_X = predict_X.astype(float)
#    predict_X.columns = ['Oxygen','PulseRate','Temperature']

#    predict_X.dropna(inplace=True)
#    predict_X = scale.transform(predict_X)

#    predictions = model.predict(predict_X)
#    predicted_health = {}

#    print("Predicted Health:")
#    for i in range(len(predictions)):
#       predicted_health[data_time[i]] = predictions[i] 

#    return render_template('index.html',predicted_health = predicted_health)

# if __name__ == '__main__':
#    app.run(debug= True) 



import os
import requests
from flask import Flask, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
dataset_file = os.path.join(app.root_path, 'static', 'dataset.csv')

@app.route('/')
def hello_world():
    Data = pd.read_csv(dataset_file)
    X = Data[['Oxygen', 'PulseRate', 'Temperature']]
    y = Data['Result']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    logreg = LogisticRegression()
    logreg.fit(X_train_scaled, y_train)

    channel_id = ''
    read_api_key = ''
    num_entries = 5  # number of latest entries to fetch

    url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}'
    response = requests.get(url)
    data = response.json()

    predict_data = pd.DataFrame(data['feeds'])
    predict_X = predict_data[['field1', 'field2', 'field3']]
    data_time = predict_data['created_at']

    # convert data types and rename columns
    predict_X = predict_X.astype(float)
    predict_X.columns = ['Oxygen', 'PulseRate', 'Temperature']

    predict_X.dropna(inplace=True)
    predict_X_scaled = scaler.transform(predict_X)

    predictions = logreg.predict(predict_X_scaled)
    predicted_health = {}

    print("Predicted Health:")
    for i in range(len(predictions)):
        predicted_health[data_time[i]] = predictions[i]

    return render_template('index.html', predicted_health=predicted_health)

if __name__ == '__main__':
    app.run(debug=True)
