from flask import Flask, url_for, render_template, request, jsonify
import requests as rq
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method =='POST':
		i_url = request.form.get('url')
		rs = rq.get(i_url)
		d_url = rs.url
		count = 0
		redirct_count = len(rs.history)

		if redirct_count ==1:
			count = 0
		else:	
			for c in rs.history:
				count = count + 1
		print(count)
		r_url = []	
		for c in range(count):
			r_url.append(rs.history[c].url)
		r_url.append(d_url)

		soup = BeautifulSoup(rs.content,'html.parser')
		soup.prettify()

		title = soup.title.string
		google_url = ("""https://transparencyreport.google.com
			/safe-browsing/search?url={}""".format(d_url))

		nortan =("https://safeweb.norton.com/report/show?url={}".format(d_url))

		wot =("https://www.mywot.com/en/scorecard/{}".format(d_url))
		print(r_url)
		# print(" \n\n\n\n ############ DATA ################# \n\n\n")
		# print(type(data))
		# print('\n\n')
		# print(data)
		# print(d_url)
		# print(title)
		
		return render_template('home.html', d_url=d_url,count=count, 
			r_url =r_url, title=title,google_url=google_url,nortan=nortan,wot=wot )
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