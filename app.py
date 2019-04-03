from flask import Flask, url_for, render_template, request
import requests as rq
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method =='POST':
		i_url = request.form.get('url')
		rs = rq.get(i_url)
		d_url = rs.url
		soup = BeautifulSoup(rs.content,'html.parser')
		soup.prettify()
		data = {
		'title':soup.title.string,
		'google_url':("""https://transparencyreport.google.com
			/safe-browsing/search?url={}""".format(d_url)),
		'norton' :("https://safeweb.norton.com/report/show?url={}".format(d_url)),
		'wot' :("https://www.mywot.com/en/scorecard/{}".format(d_url))
		}

		# title = soup.title.string
		# google_url = ("""https://transparencyreport.google.com
		# 	/safe-browsing/search?url={}""".format(d_url))
		# nortan =("https://safeweb.norton.com/report/show?url={}".format(d_url))
		# wot =("https://www.mywot.com/en/scorecard/{}".format(d_url))
		print(" \n\n\n\n ############ DATA ################# \n\n\n")
		# print(d_url)
		# print(title)
		
		return render_template('home.html', data=data)
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