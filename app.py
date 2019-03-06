from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method =='POST':
		return 'ok'
	else:	
		return render_template('home.html')
	
@app.route('/about')
def about():
	return '<h3>Hello World</h3>'


if __name__ =='__main__':
	app.run(debug=True, host='0.0.0.0', port=3333)	