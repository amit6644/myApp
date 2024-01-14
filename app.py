from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
		return 'Hello this is simple flask app'

if __name__ == '__main__':
	app.run()
