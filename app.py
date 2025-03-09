from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

# Load trained model using pickle

model = pickle.load(open("model.pkl","rb"))
@app.route('/')
def view():
   return render_template('index.html')
@app.route('/home')
def home():
   return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    data1=int(request.form["gender"])
    data2=float(request.form["hemoglobin"])
    data3=float(request.form["mch"])
    data4=float(request.form["mchc"])
    data5=float(request.form["mcv"])
    arr=np.array([[data1,data2, data3,data4,data5]])
    print(data1)
    print(data2)
    print(data3)
    print(data4)
    print(data5)
    output=model.predict(arr)
    print(output)
    if output==[0]:
      result="No Animia"
    elif output==[1]:
       result="Animia"
    else:
       result="You Entered Wrong Input"
    return render_template('predict.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)


