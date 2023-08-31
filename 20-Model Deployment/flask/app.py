from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template( 'index.html')


def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    model = pickle.load(open('ml_model.pkl', 'rb'))
    scaled = pickle.load(open('scaler.pkl', 'rb'))
    prediction = model.predict(scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]]))
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    return 'error'

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST': 
        pclass = int(request.form['pclass'])
        sex = int(request.form['sex'])
        age = int(request.form['age'])
        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])
        fare = int(request.form['fare'])
        embC = int(request.form['embC'])
        embQ = int(request.form['embQ'])
        embS = int(request.form['embS'])

        result = getPredictions(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)
        print(result)
        
    return render_template('result.html', result = result)




if __name__ == '__main__':
	app.run(debug=True)
