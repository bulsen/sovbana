# -*- encoding: utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import dbconn as db
import random
import newfuckfuck as fuckfuck


def taunt():
	""" random taunt """
	asd = db.sovmeaq()
	return asd



from flask import Flask, render_template, request, redirect, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/<que>')
def sovbana(que):
	if len(que)>=200:
		que = que[0:400]
	else:
		pass
	ip = request.remote_addr
	db.push(que,ip)
	data = taunt()
	return render_template("/hizimialamadim.html",data=data)

# adding favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

# 404 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# main page
@app.route('/')
def main():
	return render_template("main.html")

@app.route('/', methods=['GET','POST'])
def my_form_post():
	if request.method == "POST":
	    return redirect("/%s"%request.form['search'])

@app.route('/donbebegim/bool/<pre>')
def donbebegim(pre):
	""" rates shit and checks if they are bad words"""
	asd = " ".join(pre.split("_"))
	return jsonify(response=fuckfuck.strip(asd))

@app.route('/partile/listele/')
def partiler():
	""" returns array chunks of databases """
	data = db.listele()
	return render_template("listele.html",data=data)

if __name__ == '__main__':
	app.run(host ="0.0.0.0", port=80, processes=15, debug=True)





