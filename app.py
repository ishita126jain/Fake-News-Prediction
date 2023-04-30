from flask import Flask, request, render_template, url_for
import pickle

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/predict', methods=['POST'])
def predict():
	sentence = request.form['news']
	
	vector_form = pickle.load(open('vector.pkl', 'rb'))
	load_model = pickle.load(open('model.pkl', 'rb'))
	
	prediction = load_model.predict(vector_form.transform([sentence]))
	
	if prediction ==[1]:
		return render_template('warning.html')
	
	else:
		return render_template('sucess.html')
	
        	
if __name__ == "__main__":
	app.run(debug=True)
