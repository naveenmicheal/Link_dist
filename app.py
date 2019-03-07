from flask import Flask, url_for, render_template, request
import requests as rq
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method =='POST':
		i_url = request.form.get('url')
		rs = rq.get(i_url)
		d_url = rs.url;
		return render_template('home.html', data=d_url)
	else:	
		return render_template('home.html')
# @app.route('/url/<string:iurl>')
# def url(iurl):
# 	# if (iurl[0:7]) !='http://':
# 	# 	iurl ='http://'+iurl
# 	iurl = 'http://'+iurl
# 	print(iurl)	
# 	rs = rq.get(iurl)
# 	d_url = rs.url;
# 	return 	d_url

@app.route('/about')
def about():
	return '<h3>Hello World</h3>'


if __name__ =='__main__':
	app.run(debug=True, host='0.0.0.0', port=3333)	