from flask import Flask,request,render_template
import pickle
import numpy as np


flask_app = Flask(__name__)

model = pickle.load(open("crop_recommendation_model.pkl","rb"))


@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict",methods = ["POST"])

def predict():
    float_feature = [float(x) for x in request.form.values()]
    features = [np.array(float_feature)]
    prediction = model.predict(features)
    return render_template("index.html",Prediction_Text = "The Crop : {}".format(prediction[0]))

if __name__ == "__main__":
    flask_app.run(debug=True)
