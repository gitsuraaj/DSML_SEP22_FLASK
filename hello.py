from flask import Flask, request, redirect, url_for
import pickle
import sklearn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/ping", methods=['GET'])
def ping_something():
    return "<h1>PINGING .........</H1>"

#to run a flask app
#export FLASK_APP=hello.py
#flask run
lister=[]

@app.route("/success/<name>", methods=['GET'])
def success(name):
    x = 'welcome ' + name + '  total users --' + str(lister)
    return x


@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        lister.append(user)
        return redirect(url_for('success', name=user))


    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

model_pickle=open('./classifier.pkl', 'rb')
clf= pickle.load(model_pickle)

@app.route("/predict", methods=['POST'])
def predictions ():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        gender = 0
    else:
        gender = 1

    if loan_req['Married'] == "No":
        marital_status = 0
    else:
        marital_status = 1

    applicant_income = loan_req['ApplicantIncome']
    loan_amt = loan_req['LoanAmount'] / 1000
    credit_history = loan_req['Credit_History']

    input_data = [[gender, marital_status, applicant_income, loan_amt, credit_history]]
    prediction = clf.predict(input_data)

    if prediction == 0:
        pred = "Rejected"

    else:
        pred = "Accepted"

    return {"loan_approval_status": pred}