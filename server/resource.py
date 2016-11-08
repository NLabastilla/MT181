from flask import Flask, render_template, redirect, url_for, request,
app = Flask(__name__)
@app.route('/auth/',methods=['POST', 'GET'])
def login():
	if request.method=='POST':
		username = request.form['userid']
		password = request.form['pswrd']
 		return redirect(url_for('auth')
@app.route('/load',method=['GET'])
def subjects():
		if login.username =
 		return render_template("buloy.htm")
		return render_template("kalay.htm")
if __name__ == '__main__':
 app.run(debug=True)