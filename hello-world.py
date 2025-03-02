from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, World!'

@app.route('/getdetails')
def get_details():
     return 'Poovarasan - 22IT030'

if __name__=='__main__':
   app.run(debug=True)
