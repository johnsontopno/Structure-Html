from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

# print(__name__)
if __name__ == '__main__':
  # print('Johnson Topno')
  app.run('0.0.0.0', debug=True)