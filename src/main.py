from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
	return "Hey, This jimmy juhu on work"


if __name__ == '__main__':
   app.run(debug = True)


